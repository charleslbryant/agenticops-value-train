"""
Tests for check_todo.py script.
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import scripts after path modification
from check_todo import check_unchecked_items  # noqa: E402
from check_todo import find_active_checklist  # noqa: E402
from check_todo import main  # noqa: E402
from check_todo import (find_active_session_file,  # noqa: E402
                        parse_active_session)


@pytest.mark.unit
class TestFindActiveSessionFile:
    """Test finding active session file."""

    def test_find_existing_session_file(self, temp_project_root):
        """Test finding existing ACTIVE_SESSION.md file."""
        # Create the file
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text("# Active Session")

        result = find_active_session_file(temp_project_root)

        assert result == session_path
        assert result.exists()

    def test_find_missing_session_file(self, temp_project_root):
        """Test error when ACTIVE_SESSION.md file is missing."""
        with pytest.raises(SystemExit) as exc_info:
            find_active_session_file(temp_project_root)

        assert exc_info.value.code == 1


@pytest.mark.unit
class TestParseActiveSession:
    """Test parsing active session content."""

    def test_parse_valid_active_session(self, temp_project_root, sample_active_session):
        """Test parsing valid ACTIVE_SESSION.md content."""
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(sample_active_session)

        result = parse_active_session(session_path)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"
        assert result["task"]["issue_number"] == 1
        assert result["task"]["title"] == "Test task"

    def test_parse_invalid_yaml(self, temp_project_root):
        """Test error handling for invalid YAML."""
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(
            """# Active Session

## Current Work
```yaml
mode: build
phase: enablement
invalid_yaml: [unclosed bracket
```"""
        )

        with pytest.raises(SystemExit) as exc_info:
            parse_active_session(session_path)

        assert exc_info.value.code == 1

    def test_parse_missing_current_work(self, temp_project_root):
        """Test parsing when Current Work section is missing."""
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(
            """# Active Session

## Session Metadata
```yaml
session_id: "test"
```"""
        )

        result = parse_active_session(session_path)

        # Should return empty dict or None when no Current Work section
        assert result is None or result == {}


@pytest.mark.unit
class TestFindActiveChecklist:
    """Test finding active checklist file."""

    def test_find_existing_checklist(self, temp_project_root):
        """Test finding existing checklist file."""
        checklist_path = (
            temp_project_root / "docs" / "rules" / "checklists" / "build-checklist.md"
        )
        checklist_path.write_text("# Build Checklist")

        result = find_active_checklist(temp_project_root, "build")

        assert result == checklist_path
        assert result.exists()

    def test_find_missing_checklist(self, temp_project_root):
        """Test error when checklist file is missing."""
        with pytest.raises(SystemExit) as exc_info:
            find_active_checklist(temp_project_root, "nonexistent")

        assert exc_info.value.code == 1


@pytest.mark.unit
class TestCheckUncheckedItems:
    """Test checking for unchecked items."""

    def test_find_unchecked_items(
        self, temp_project_root, sample_checklist_with_unchecked
    ):
        """Test finding unchecked items in checklist."""
        checklist_path = temp_project_root / "test-checklist.md"
        checklist_path.write_text(sample_checklist_with_unchecked)

        result = check_unchecked_items(checklist_path)

        assert len(result) == 8  # 8 unchecked items total
        line_numbers = [item[0] for item in result]
        assert 5 in line_numbers  # "- [ ] Data access confirmed"
        assert 6 in line_numbers  # "- [ ] Team ready"
        assert 10 in line_numbers  # "- [ ] Write code"
        assert 11 in line_numbers  # "- [ ] Run tests"

    def test_no_unchecked_items(self, temp_project_root, sample_checklist_all_checked):
        """Test when all items are checked."""
        checklist_path = temp_project_root / "test-checklist.md"
        checklist_path.write_text(sample_checklist_all_checked)

        result = check_unchecked_items(checklist_path)

        assert len(result) == 0

    def test_different_checkbox_formats(self, temp_project_root):
        """Test different checkbox formats."""
        content = """# Test Checklist

- [ ] Hyphen unchecked
- [x] Hyphen checked
* [ ] Asterisk unchecked
* [x] Asterisk checked
"""
        checklist_path = temp_project_root / "test-checklist.md"
        checklist_path.write_text(content)

        result = check_unchecked_items(checklist_path)

        assert len(result) == 2  # 2 unchecked items
        unchecked_lines = [item[1] for item in result]
        assert "- [ ] Hyphen unchecked" in unchecked_lines
        assert "* [ ] Asterisk unchecked" in unchecked_lines

    def test_file_read_error(self, temp_project_root):
        """Test error handling when file cannot be read."""
        nonexistent_path = temp_project_root / "nonexistent.md"

        with pytest.raises(SystemExit) as exc_info:
            check_unchecked_items(nonexistent_path)

        assert exc_info.value.code == 1


@pytest.mark.integration
class TestMainFunction:
    """Integration tests for main function."""

    def test_main_with_unchecked_items_non_strict(
        self, temp_project_root, sample_active_session, sample_checklist_with_unchecked
    ):
        """Test main function with unchecked items in non-strict mode."""
        # Setup test files
        from tests.conftest import create_test_checklist, create_test_files

        create_test_files(temp_project_root, {}, sample_active_session)
        create_test_checklist(
            temp_project_root, "build", sample_checklist_with_unchecked
        )

        with patch(
            "sys.argv", ["check_todo.py", "--project-root", str(temp_project_root)]
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

    def test_main_with_unchecked_items_strict(
        self, temp_project_root, sample_active_session, sample_checklist_with_unchecked
    ):
        """Test main function with unchecked items in strict mode."""
        # Setup test files
        from tests.conftest import create_test_checklist, create_test_files

        create_test_files(temp_project_root, {}, sample_active_session)
        create_test_checklist(
            temp_project_root, "build", sample_checklist_with_unchecked
        )

        with patch(
            "sys.argv",
            ["check_todo.py", "--project-root", str(temp_project_root), "--strict"],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_with_all_checked(
        self, temp_project_root, sample_active_session, sample_checklist_all_checked
    ):
        """Test main function with all items checked."""
        # Setup test files
        from tests.conftest import create_test_checklist, create_test_files

        create_test_files(temp_project_root, {}, sample_active_session)
        create_test_checklist(temp_project_root, "build", sample_checklist_all_checked)

        with patch(
            "sys.argv", ["check_todo.py", "--project-root", str(temp_project_root)]
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

    def test_main_missing_mode(self, temp_project_root):
        """Test main function when mode is missing from session."""
        session_content = """# Active Session

## Current Work
```yaml
phase: "enablement"
agent: "conductor"
```"""

        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(session_content)

        with patch(
            "sys.argv", ["check_todo.py", "--project-root", str(temp_project_root)]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_with_custom_project_root(
        self, temp_project_root, sample_active_session, sample_checklist_all_checked
    ):
        """Test main function with custom project root."""
        # Setup test files
        from tests.conftest import create_test_checklist, create_test_files

        create_test_files(temp_project_root, {}, sample_active_session)
        create_test_checklist(temp_project_root, "build", sample_checklist_all_checked)

        with patch(
            "sys.argv", ["check_todo.py", "--project-root", str(temp_project_root)]
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()


@pytest.mark.unit
class TestErrorHandling:
    """Test error handling scenarios."""

    def test_permission_error_handling(self, temp_project_root):
        """Test handling of permission errors."""
        # This test would require special setup to trigger permission errors
        # In a real scenario, you might use mock to simulate permission errors
        pass

    def test_yaml_parsing_edge_cases(self, temp_project_root):
        """Test edge cases in YAML parsing."""
        session_content = """# Active Session

## Current Work
```yaml
mode: "build"
phase: "enablement"
agent: "conductor"
task:
  issue_number: 1
  title: "Test with special characters: @#$%^&*()"
  description: |
    Multi-line description
    with special characters
```"""

        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(session_content)

        result = parse_active_session(session_path)

        assert result["mode"] == "build"
        assert result["task"]["title"] == "Test with special characters: @#$%^&*()"
        assert "Multi-line description" in result["task"]["description"]


if __name__ == "__main__":
    pytest.main([__file__])
