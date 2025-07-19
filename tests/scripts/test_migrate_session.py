"""
Tests for migrate_session.py script.
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import scripts after path modification
from migrate_session import detect_legacy_format  # noqa: E402
from migrate_session import (generate_new_session_content, main,  # noqa: E402
                             parse_json_format, parse_key_value_format,
                             parse_markdown_format, parse_yaml_frontmatter)


@pytest.mark.unit
class TestDetectLegacyFormat:
    """Test detecting legacy session formats."""

    def test_detect_json_format(self, sample_legacy_json):
        """Test detecting JSON format."""
        result = detect_legacy_format(sample_legacy_json)

        assert result == "json"

    def test_detect_yaml_frontmatter(self, sample_legacy_yaml_frontmatter):
        """Test detecting YAML frontmatter format."""
        result = detect_legacy_format(sample_legacy_yaml_frontmatter)

        assert result == "yaml_frontmatter"

    def test_detect_markdown_format(self):
        """Test detecting markdown format."""
        content = """# Session Context

## Mode
build

## Phase
enablement

## Agent
conductor

## Decisions
- Decision 1
- Decision 2
"""

        result = detect_legacy_format(content)

        assert result == "markdown"

    def test_detect_key_value_format(self):
        """Test detecting key=value format."""
        content = """mode=build
phase=enablement
agent=conductor
task.issue_number=1
task.title=Test task
decisions=Decision 1,Decision 2
"""

        result = detect_legacy_format(content)

        assert result == "key_value"

    def test_detect_unknown_format(self):
        """Test detecting unknown format."""
        content = "This is some random content that doesn't match any format"

        result = detect_legacy_format(content)

        assert result == "unknown"

    def test_detect_invalid_json(self):
        """Test detecting invalid JSON."""
        content = "{ invalid json content"

        result = detect_legacy_format(content)

        assert result == "unknown"


@pytest.mark.unit
class TestParseJsonFormat:
    """Test parsing JSON format."""

    def test_parse_valid_json(self, sample_legacy_json):
        """Test parsing valid JSON format."""
        result = parse_json_format(sample_legacy_json)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"
        assert result["task"]["issue_number"] == 1
        assert result["task"]["title"] == "Legacy task"
        assert "Legacy decision 1" in result["decisions"]
        assert "Legacy step 1" in result["next_steps"]

    def test_parse_minimal_json(self):
        """Test parsing minimal JSON format."""
        content = '{"mode": "build"}'

        result = parse_json_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"  # default value
        assert result["agent"] == "conductor"  # default value
        assert result["decisions"] == []
        assert result["next_steps"] == []

    def test_parse_invalid_json(self):
        """Test parsing invalid JSON."""
        content = "{ invalid json }"

        result = parse_json_format(content)

        assert result == {}

    def test_parse_json_with_null_values(self):
        """Test parsing JSON with null values."""
        content = """{
    "mode": "build",
    "phase": null,
    "agent": "conductor",
    "task": null,
    "decisions": null,
    "next_steps": []
}"""

        result = parse_json_format(content)

        assert result["mode"] == "build"
        assert result["phase"] is None
        assert result["agent"] == "conductor"
        assert result["task"] is None
        assert result["decisions"] is None
        assert result["next_steps"] == []


@pytest.mark.unit
class TestParseYamlFrontmatter:
    """Test parsing YAML frontmatter format."""

    def test_parse_valid_yaml_frontmatter(self, sample_legacy_yaml_frontmatter):
        """Test parsing valid YAML frontmatter."""
        result = parse_yaml_frontmatter(sample_legacy_yaml_frontmatter)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"
        assert result["task"]["issue_number"] == 1
        assert result["task"]["title"] == "Legacy task"
        assert "Legacy decision 1" in result["decisions"]
        assert "Legacy step 1" in result["next_steps"]

    def test_parse_minimal_yaml_frontmatter(self):
        """Test parsing minimal YAML frontmatter."""
        content = """---
mode: build
---

# Content
"""

        result = parse_yaml_frontmatter(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"  # default value
        assert result["decisions"] == []

    def test_parse_invalid_yaml_frontmatter(self):
        """Test parsing invalid YAML frontmatter."""
        content = """---
mode: build
invalid_yaml: [unclosed
---

# Content
"""

        result = parse_yaml_frontmatter(content)

        assert result == {}

    def test_parse_yaml_frontmatter_no_delimiters(self):
        """Test parsing YAML frontmatter without delimiters."""
        content = """mode: build
phase: enablement

# Content
"""

        result = parse_yaml_frontmatter(content)

        assert result == {}


@pytest.mark.unit
class TestParseMarkdownFormat:
    """Test parsing markdown format."""

    def test_parse_valid_markdown(self):
        """Test parsing valid markdown format."""
        content = """# Session Context

## Mode
build

## Phase
enablement

## Agent
conductor

## Task
issue_number: 1
title: Test task
status: In progress

## Decisions
- Decision 1
- Decision 2

## Next Steps
- Step 1
- Step 2
"""

        result = parse_markdown_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"
        assert result["task"]["issue_number"] == "1"
        assert result["task"]["title"] == "Test task"
        assert "Decision 1" in result["decisions"]
        assert "Step 1" in result["next_steps"]

    def test_parse_minimal_markdown(self):
        """Test parsing minimal markdown format."""
        content = """# Session Context

## Mode
build
"""

        result = parse_markdown_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"  # default value
        assert result["decisions"] == []

    def test_parse_markdown_with_empty_sections(self):
        """Test parsing markdown with empty sections."""
        content = """# Session Context

## Mode

## Phase
enablement

## Agent
conductor
"""

        result = parse_markdown_format(content)

        assert result["mode"] == "build"  # default value
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"


@pytest.mark.unit
class TestParseKeyValueFormat:
    """Test parsing key=value format."""

    def test_parse_valid_key_value(self):
        """Test parsing valid key=value format."""
        content = """mode=build
phase=enablement
agent=conductor
task.issue_number=1
task.title=Test task
task.status=In progress
decisions=Decision 1,Decision 2
next_steps=Step 1,Step 2
"""

        result = parse_key_value_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"
        assert result["task"]["issue_number"] == "1"
        assert result["task"]["title"] == "Test task"
        assert "Decision 1" in result["decisions"]
        assert "Step 1" in result["next_steps"]

    def test_parse_key_value_with_quotes(self):
        """Test parsing key=value with quoted values."""
        content = """mode="build"
phase='enablement'
agent="conductor"
task.title="Task with special chars: @#$%"
"""

        result = parse_key_value_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"
        assert result["task"]["title"] == "Task with special chars: @#$%"

    def test_parse_minimal_key_value(self):
        """Test parsing minimal key=value format."""
        content = """mode=build
"""

        result = parse_key_value_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"  # default value
        assert result["decisions"] == []

    def test_parse_key_value_with_empty_values(self):
        """Test parsing key=value with empty values."""
        content = """mode=build
phase=
agent=conductor
decisions=
"""

        result = parse_key_value_format(content)

        assert result["mode"] == "build"
        assert result["phase"] == ""
        assert result["agent"] == "conductor"
        assert result["decisions"] == [""]  # Empty string in list


@pytest.mark.unit
class TestGenerateNewSessionContent:
    """Test generating new session content."""

    def test_generate_basic_session_content(self, temp_project_root):
        """Test generating basic session content."""
        legacy_data = {
            "mode": "build",
            "phase": "enablement",
            "agent": "conductor",
            "task": {"issue_number": 1, "title": "Test task", "status": "In progress"},
            "decisions": ["Decision 1", "Decision 2"],
            "next_steps": ["Step 1", "Step 2"],
        }

        result = generate_new_session_content(legacy_data, temp_project_root)

        assert "# Active Session Context" in result
        assert 'mode: "build"' in result
        assert 'phase: "enablement"' in result
        assert 'agent: "conductor"' in result
        assert 'title: "Test task"' in result
        assert '"Decision 1"' in result
        assert '"Step 1"' in result
        assert "Schema Definition" in result

    def test_generate_session_with_minimal_data(self, temp_project_root):
        """Test generating session with minimal data."""
        legacy_data = {
            "mode": "build",
            "phase": "enablement",
            "agent": "conductor",
            "task": {},
            "decisions": [],
            "next_steps": [],
        }

        result = generate_new_session_content(legacy_data, temp_project_root)

        assert 'mode: "build"' in result
        assert 'phase: "enablement"' in result
        assert 'agent: "conductor"' in result
        assert '"Migrated from legacy session format"' in result
        assert '"Review and update session context"' in result

    def test_generate_session_with_string_task(self, temp_project_root):
        """Test generating session when task is a string instead of dict."""
        legacy_data = {
            "mode": "build",
            "phase": "enablement",
            "agent": "conductor",
            "task": "String task description",
            "decisions": ["Decision 1"],
            "next_steps": ["Step 1"],
        }

        result = generate_new_session_content(legacy_data, temp_project_root)

        assert 'mode: "build"' in result
        assert 'title: "Migrated from legacy session"' in result
        assert "issue_number: unknown" in result

    def test_generate_session_with_special_characters(self, temp_project_root):
        """Test generating session with special characters."""
        legacy_data = {
            "mode": "build",
            "phase": "enablement",
            "agent": "conductor",
            "task": {
                "title": "Task with special chars: @#$%^&*()",
                "description": "Multi-line\ndescription",
            },
            "decisions": ['Decision with quotes "quoted"'],
            "next_steps": ["Step with: colon"],
        }

        result = generate_new_session_content(legacy_data, temp_project_root)

        assert "Task with special chars: @#$%^&*()" in result
        assert '"Decision with quotes \\"quoted\\""' in result
        assert '"Step with: colon"' in result


@pytest.mark.integration
class TestMainFunction:
    """Integration tests for main function."""

    def test_main_json_migration(self, temp_project_root, sample_legacy_json):
        """Test main function with JSON migration."""
        # Create legacy file
        legacy_file = temp_project_root / "legacy.json"
        legacy_file.write_text(sample_legacy_json)

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that new session was created
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        assert session_path.exists()

        content = session_path.read_text()
        assert 'mode: "build"' in content
        assert 'phase: "enablement"' in content
        assert 'agent: "conductor"' in content
        assert '"Legacy decision 1"' in content

    def test_main_yaml_frontmatter_migration(
        self, temp_project_root, sample_legacy_yaml_frontmatter
    ):
        """Test main function with YAML frontmatter migration."""
        # Create legacy file
        legacy_file = temp_project_root / "legacy.md"
        legacy_file.write_text(sample_legacy_yaml_frontmatter)

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that new session was created
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        assert session_path.exists()

        content = session_path.read_text()
        assert 'mode: "build"' in content
        assert '"Legacy decision 1"' in content

    def test_main_dry_run(self, temp_project_root, sample_legacy_json):
        """Test main function in dry run mode."""
        # Create legacy file
        legacy_file = temp_project_root / "legacy.json"
        legacy_file.write_text(sample_legacy_json)

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
                "--dry-run",
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that new session was NOT created
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        assert not session_path.exists()

    def test_main_with_custom_output_file(self, temp_project_root, sample_legacy_json):
        """Test main function with custom output file."""
        # Create legacy file
        legacy_file = temp_project_root / "legacy.json"
        legacy_file.write_text(sample_legacy_json)

        output_file = temp_project_root / "custom_session.md"

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
                "--output-file",
                str(output_file),
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that custom output file was created
        assert output_file.exists()

        content = output_file.read_text()
        assert 'mode: "build"' in content

    def test_main_with_backup(self, temp_project_root, sample_legacy_json):
        """Test main function with backup of existing file."""
        # Create legacy file
        legacy_file = temp_project_root / "legacy.json"
        legacy_file.write_text(sample_legacy_json)

        # Create existing session file
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text("# Existing Session")

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
                "--backup",
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that backup was created
        backup_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md.backup"
        )
        assert backup_path.exists()
        assert backup_path.read_text() == "# Existing Session"

        # Check that new session was created
        content = session_path.read_text()
        assert 'mode: "build"' in content

    def test_main_missing_legacy_file(self, temp_project_root):
        """Test main function with missing legacy file."""
        legacy_file = temp_project_root / "nonexistent.json"

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
            ],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_unknown_format(self, temp_project_root):
        """Test main function with unknown format."""
        # Create legacy file with unknown format
        legacy_file = temp_project_root / "legacy.txt"
        legacy_file.write_text("Unknown format content")

        with patch(
            "sys.argv",
            [
                "migrate_session.py",
                "--project-root",
                str(temp_project_root),
                "--legacy-file",
                str(legacy_file),
            ],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_failed_parsing(self, temp_project_root):
        """Test main function with failed parsing."""
        # Create legacy file that looks like JSON but parses to empty
        legacy_file = temp_project_root / "legacy.json"
        legacy_file.write_text("{}")

        # Mock parse function to return empty dict
        with patch("migrate_session.parse_json_format", return_value={}):
            with patch(
                "sys.argv",
                [
                    "migrate_session.py",
                    "--project-root",
                    str(temp_project_root),
                    "--legacy-file",
                    str(legacy_file),
                ],
            ):
                with pytest.raises(SystemExit) as exc_info:
                    main()

                assert exc_info.value.code == 1


@pytest.mark.unit
class TestErrorHandling:
    """Test error handling scenarios."""

    def test_file_permission_errors(self, temp_project_root):
        """Test handling of file permission errors."""
        # This test would require special setup to trigger permission errors
        # In a real scenario, you might use mock to simulate permission errors
        pass

    def test_yaml_generation_with_none_values(self, temp_project_root):
        """Test YAML generation with None values."""
        legacy_data = {
            "mode": None,
            "phase": None,
            "agent": None,
            "task": None,
            "decisions": None,
            "next_steps": None,
        }

        result = generate_new_session_content(legacy_data, temp_project_root)

        # Should handle None values gracefully
        assert 'mode: "build"' in result  # Should use default
        assert 'phase: "enablement"' in result  # Should use default
        assert 'agent: "conductor"' in result  # Should use default

    def test_unicode_handling(self, temp_project_root):
        """Test handling of unicode characters."""
        legacy_data = {
            "mode": "build",
            "phase": "enablement",
            "agent": "conductor",
            "task": {"title": "Task with unicode: αβγ δεζ 中文 🚀"},
            "decisions": ["Decision with unicode: αβγ"],
            "next_steps": ["Step with emoji: 🚀"],
        }

        result = generate_new_session_content(legacy_data, temp_project_root)

        assert "Task with unicode: αβγ δεζ 中文 🚀" in result
        assert "Decision with unicode: αβγ" in result
        assert "Step with emoji: 🚀" in result


if __name__ == "__main__":
    pytest.main([__file__])
