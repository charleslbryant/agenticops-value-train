"""
Tests for conductor_update.py script.
"""

import sys
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from conductor_update import (
    get_next_phase,
    get_phase_info,
    load_active_session,
    load_pipeline_config,
    main,
    replace_yaml_section,
    save_active_session,
    update_session_phase,
)


@pytest.mark.unit
class TestLoadPipelineConfig:
    """Test loading pipeline configuration."""

    def test_load_existing_config(self, temp_project_root, sample_pipeline_config):
        """Test loading existing pipeline configuration."""
        config_path = temp_project_root / "config" / "pipeline.yml"
        with open(config_path, "w") as f:
            yaml.dump(sample_pipeline_config, f)

        result = load_pipeline_config(temp_project_root)

        assert result["metadata"]["name"] == "Test Pipeline"
        assert len(result["phases"]) == 3
        assert result["phases"][0]["name"] == "enablement"

    def test_load_missing_config(self, temp_project_root):
        """Test error when pipeline config is missing."""
        with pytest.raises(SystemExit) as exc_info:
            load_pipeline_config(temp_project_root)

        assert exc_info.value.code == 1


@pytest.mark.unit
class TestLoadActiveSession:
    """Test loading active session."""

    def test_load_existing_session(self, temp_project_root, sample_active_session):
        """Test loading existing active session."""
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(sample_active_session)

        sections, content = load_active_session(temp_project_root)

        assert "Current Work" in sections
        assert "Session Metadata" in sections
        assert "Session Notes" in sections
        assert 'mode: "build"' in sections["Current Work"]
        assert len(content) > 0

    def test_load_missing_session(self, temp_project_root):
        """Test error when active session is missing."""
        with pytest.raises(SystemExit) as exc_info:
            load_active_session(temp_project_root)

        assert exc_info.value.code == 1

    def test_load_session_with_missing_sections(self, temp_project_root):
        """Test loading session with missing sections."""
        minimal_session = """# Active Session Context

## Current Work
```yaml
mode: "build"
phase: "enablement"
```
"""
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        session_path.write_text(minimal_session)

        sections, content = load_active_session(temp_project_root)

        assert "Current Work" in sections
        assert "Session Metadata" not in sections
        assert 'mode: "build"' in sections["Current Work"]


@pytest.mark.unit
class TestGetNextPhase:
    """Test getting next phase."""

    def test_get_existing_next_phase(self, sample_pipeline_config):
        """Test getting next phase for existing phase."""
        result = get_next_phase(sample_pipeline_config, "enablement")

        assert result == "discovery"

    def test_get_next_phase_for_last_phase(self, sample_pipeline_config):
        """Test getting next phase for last phase."""
        result = get_next_phase(sample_pipeline_config, "scope")

        assert result is None

    def test_get_next_phase_nonexistent(self, sample_pipeline_config):
        """Test getting next phase for nonexistent phase."""
        result = get_next_phase(sample_pipeline_config, "nonexistent")

        assert result is None


@pytest.mark.unit
class TestGetPhaseInfo:
    """Test getting phase information."""

    def test_get_existing_phase_info(self, sample_pipeline_config):
        """Test getting info for existing phase."""
        result = get_phase_info(sample_pipeline_config, "enablement")

        assert result["name"] == "enablement"
        assert result["mode"] == "build"
        assert result["owner"] == "conductor"

    def test_get_nonexistent_phase_info(self, sample_pipeline_config):
        """Test getting info for nonexistent phase."""
        result = get_phase_info(sample_pipeline_config, "nonexistent")

        assert result is None


@pytest.mark.unit
class TestReplaceYamlSection:
    """Test replacing YAML sections."""

    def test_replace_existing_section(self):
        """Test replacing existing YAML section."""
        content = """# Test Document

## Current Work
```yaml
mode: "build"
phase: "enablement"
```

## Other Section
Some other content
"""

        new_yaml = """mode: "discover"
phase: "discovery"
agent: "onboarder" """

        result = replace_yaml_section(content, "Current Work", new_yaml)

        assert 'mode: "discover"' in result
        assert 'phase: "discovery"' in result
        assert 'agent: "onboarder"' in result
        assert 'mode: "build"' not in result
        assert "## Other Section" in result

    def test_replace_nonexistent_section(self):
        """Test replacing nonexistent YAML section."""
        content = """# Test Document

## Current Work
```yaml
mode: "build"
```
"""

        new_yaml = """mode: "discover" """

        result = replace_yaml_section(content, "Nonexistent Section", new_yaml)

        # Should return original content unchanged
        assert result == content

    def test_replace_section_with_special_characters(self):
        """Test replacing section with special characters in YAML."""
        content = """# Test Document

## Current Work
```yaml
mode: "build"
title: "Simple title"
```
"""

        new_yaml = """mode: "discover"
title: "Title with special chars: @#$%^&*()"
description: |
  Multi-line description
  with special characters"""

        result = replace_yaml_section(content, "Current Work", new_yaml)

        assert "Title with special chars: @#$%^&*()" in result
        assert "Multi-line description" in result


@pytest.mark.unit
class TestUpdateSessionPhase:
    """Test updating session phase."""

    def test_update_session_phase_success(
        self, temp_project_root, sample_active_session
    ):
        """Test successful session phase update."""
        sections = {
            "Current Work": """mode: "build"
phase: "enablement"
agent: "conductor"
task:
  issue_number: 1
  title: "Test task"
""",
            "Session Metadata": """session_id: "2025-01-18-test"
started_at: "2025-01-18 10:00:00"
last_updated: "2025-01-18 10:30:00"
""",
            "Session Notes": """decisions:
  - "Initial decision"
next_steps:
  - "Initial step"
""",
        }

        next_phase_info = {
            "name": "discovery",
            "mode": "discover",
            "owner": "onboarder",
        }

        result = update_session_phase(
            temp_project_root,
            sample_active_session,
            sections,
            "discovery",
            next_phase_info,
        )

        assert "phase: discovery" in result
        assert "mode: discover" in result
        assert "Advanced to discovery phase via conductor automation" in result
        assert "Begin discovery phase activities" in result

    def test_update_session_phase_with_missing_sections(self, temp_project_root):
        """Test updating session phase with missing sections."""
        content = """# Active Session Context

## Current Work
```yaml
mode: "build"
phase: "enablement"
```
"""

        sections = {
            "Current Work": """mode: "build"
phase: "enablement"
"""
        }

        next_phase_info = {
            "name": "discovery",
            "mode": "discover",
            "owner": "onboarder",
        }

        result = update_session_phase(
            temp_project_root, content, sections, "discovery", next_phase_info
        )

        assert "phase: discovery" in result
        assert "mode: discover" in result


@pytest.mark.unit
class TestSaveActiveSession:
    """Test saving active session."""

    def test_save_session_success(self, temp_project_root):
        """Test successful session save."""
        content = "# Updated Session Content"

        save_active_session(temp_project_root, content)

        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        assert session_path.exists()
        assert session_path.read_text() == content

    def test_save_session_create_directory(self, temp_project_root):
        """Test saving session creates directory if needed."""
        # Remove the session-context directory
        session_dir = temp_project_root / "docs" / "session-context"
        if session_dir.exists():
            session_dir.rmdir()

        content = "# Updated Session Content"

        save_active_session(temp_project_root, content)

        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        assert session_path.exists()
        assert session_path.read_text() == content


@pytest.mark.integration
class TestMainFunction:
    """Integration tests for main function."""

    def test_main_successful_advancement(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test successful phase advancement."""
        # Setup test files
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv",
            ["conductor_update.py", "--project-root", str(temp_project_root)],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that session was updated
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        updated_content = session_path.read_text()
        assert "phase: discovery" in updated_content
        assert "mode: discover" in updated_content

    def test_main_dry_run_mode(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test dry run mode."""
        # Setup test files
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        # Get original content
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        original_content = session_path.read_text()

        with patch(
            "sys.argv",
            [
                "conductor_update.py",
                "--project-root",
                str(temp_project_root),
                "--dry-run",
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that session was NOT updated
        updated_content = session_path.read_text()
        assert updated_content == original_content

    def test_main_force_phase(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test forcing advance to specific phase."""
        # Setup test files
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv",
            [
                "conductor_update.py",
                "--project-root",
                str(temp_project_root),
                "--force-phase",
                "scope",
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that session was updated to scope phase
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        updated_content = session_path.read_text()
        assert "phase: scope" in updated_content

    def test_main_at_end_of_pipeline(self, temp_project_root, sample_pipeline_config):
        """Test when already at end of pipeline."""
        # Create session at final phase
        session_content = sample_active_session.replace(
            'phase: "enablement"', 'phase: "scope"'
        )

        from tests.conftest import create_test_files

        create_test_files(temp_project_root, sample_pipeline_config, session_content)

        with patch(
            "sys.argv",
            ["conductor_update.py", "--project-root", str(temp_project_root)],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Should complete without error but no changes made
        session_path = (
            temp_project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )
        updated_content = session_path.read_text()
        assert "phase: scope" in updated_content  # Should remain unchanged

    def test_main_missing_current_work(self, temp_project_root, sample_pipeline_config):
        """Test when Current Work section is missing."""
        session_content = """# Active Session Context

## Session Metadata
```yaml
session_id: "test"
```
"""

        from tests.conftest import create_test_files

        create_test_files(temp_project_root, sample_pipeline_config, session_content)

        with patch(
            "sys.argv",
            ["conductor_update.py", "--project-root", str(temp_project_root)],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_missing_current_phase(
        self, temp_project_root, sample_pipeline_config
    ):
        """Test when current phase is missing."""
        session_content = """# Active Session Context

## Current Work
```yaml
mode: "build"
agent: "conductor"
```
"""

        from tests.conftest import create_test_files

        create_test_files(temp_project_root, sample_pipeline_config, session_content)

        with patch(
            "sys.argv",
            ["conductor_update.py", "--project-root", str(temp_project_root)],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_invalid_force_phase(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test forcing advance to invalid phase."""
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv",
            [
                "conductor_update.py",
                "--project-root",
                str(temp_project_root),
                "--force-phase",
                "nonexistent",
            ],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1


@pytest.mark.unit
class TestErrorHandling:
    """Test error handling scenarios."""

    def test_yaml_parsing_error_handling(
        self, temp_project_root, sample_pipeline_config
    ):
        """Test error handling for invalid YAML in session."""
        session_content = """# Active Session Context

## Current Work
```yaml
mode: "build"
phase: "enablement"
invalid_yaml: [unclosed bracket
```
"""

        from tests.conftest import create_test_files

        create_test_files(temp_project_root, sample_pipeline_config, session_content)

        with patch(
            "sys.argv",
            ["conductor_update.py", "--project-root", str(temp_project_root)],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_session_update_error_handling(self, temp_project_root):
        """Test error handling during session update."""
        # This would test scenarios where session update fails
        # In practice, this might involve mocking file operations to fail
        pass

    def test_timestamp_formatting(self, temp_project_root, sample_active_session):
        """Test that timestamps are formatted correctly."""
        sections = {
            "Current Work": """mode: "build"
phase: "enablement"
""",
            "Session Metadata": """session_id: "test"
started_at: "2025-01-18 10:00:00"
last_updated: "2025-01-18 10:30:00"
""",
        }

        next_phase_info = {
            "name": "discovery",
            "mode": "discover",
            "owner": "onboarder",
        }

        result = update_session_phase(
            temp_project_root,
            sample_active_session,
            sections,
            "discovery",
            next_phase_info,
        )

        # Check that timestamp is updated and properly formatted
        assert "last_updated:" in result
        # The timestamp should be in YYYY-MM-DD HH:MM:SS format
        import re

        timestamp_pattern = r'last_updated: "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"'
        assert re.search(timestamp_pattern, result)


if __name__ == "__main__":
    pytest.main([__file__])
