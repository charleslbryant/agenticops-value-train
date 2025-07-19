"""
Tests for check_artifacts.py script.
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

# Import scripts after path modification
from check_artifacts import check_artifacts_exist  # noqa: E402
from check_artifacts import get_phase_artifacts  # noqa: E402
from check_artifacts import (  # noqa: E402
    load_active_session,
    load_pipeline_config,
    main,
    resolve_artifact_paths,
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

    def test_load_invalid_yaml_config(self, temp_project_root):
        """Test error handling for invalid YAML in config."""
        config_path = temp_project_root / "config" / "pipeline.yml"
        config_path.write_text("invalid: yaml: [unclosed")

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

        result = load_active_session(temp_project_root)

        assert result["mode"] == "build"
        assert result["phase"] == "enablement"
        assert result["agent"] == "conductor"

    def test_load_missing_session(self, temp_project_root):
        """Test error when active session is missing."""
        with pytest.raises(SystemExit) as exc_info:
            load_active_session(temp_project_root)

        assert exc_info.value.code == 1


@pytest.mark.unit
class TestGetPhaseArtifacts:
    """Test getting phase artifacts."""

    def test_get_existing_phase_artifacts(self, sample_pipeline_config):
        """Test getting artifacts for existing phase."""
        result = get_phase_artifacts(sample_pipeline_config, "enablement")

        assert result == ["setup.md", "config.yml"]

    def test_get_nonexistent_phase_artifacts(self, sample_pipeline_config):
        """Test getting artifacts for nonexistent phase."""
        result = get_phase_artifacts(sample_pipeline_config, "nonexistent")

        assert result == []

    def test_get_phase_with_no_artifacts(self, sample_pipeline_config):
        """Test getting artifacts for phase with no artifacts defined."""
        # Add a phase with no artifacts
        sample_pipeline_config["phases"].append(
            {"name": "no_artifacts", "description": "Phase with no artifacts"}
        )

        result = get_phase_artifacts(sample_pipeline_config, "no_artifacts")

        assert result == []


@pytest.mark.unit
class TestResolveArtifactPaths:
    """Test resolving artifact paths."""

    def test_resolve_absolute_paths(self, temp_project_root, sample_pipeline_config):
        """Test resolving absolute paths."""
        artifacts = ["/docs/test.md", "/config/test.yml"]

        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )

        assert len(result) == 2
        assert result[0] == temp_project_root / "docs" / "test.md"
        assert result[1] == temp_project_root / "config" / "test.yml"

    def test_resolve_documentation_files(
        self, temp_project_root, sample_pipeline_config
    ):
        """Test resolving documentation files."""
        artifacts = ["requirements.md", "use-case.md", "opportunity-brief.md"]

        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )

        assert len(result) == 3
        # Use-case and opportunity should go to preengagement
        assert result[1] == temp_project_root / "preengagement" / "use-case.md"
        assert result[2] == temp_project_root / "preengagement" / "opportunity-brief.md"

    def test_resolve_code_files(self, temp_project_root, sample_pipeline_config):
        """Test resolving code and notebook files."""
        artifacts = ["extract.py", "analysis.ipynb"]

        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )

        assert len(result) == 2
        assert result[0] == temp_project_root / "delivery" / "extract.py"
        assert result[1] == temp_project_root / "delivery" / "analysis.ipynb"

    def test_resolve_data_files(self, temp_project_root, sample_pipeline_config):
        """Test resolving data files."""
        artifacts = ["dataset.csv", "processed.csv"]

        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )

        assert len(result) == 2
        assert result[0] == temp_project_root / "delivery" / "data" / "dataset.csv"
        assert result[1] == temp_project_root / "delivery" / "data" / "processed.csv"

    def test_resolve_config_files(self, temp_project_root, sample_pipeline_config):
        """Test resolving configuration files."""
        artifacts = ["settings.yaml", "config.yml"]

        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )

        assert len(result) == 2
        assert result[0] == temp_project_root / "config" / "settings.yaml"
        assert result[1] == temp_project_root / "config" / "config.yml"

    def test_resolve_default_files(self, temp_project_root, sample_pipeline_config):
        """Test resolving files with default path."""
        artifacts = ["README.txt", "notes.txt"]

        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )

        assert len(result) == 2
        assert result[0] == temp_project_root / "README.txt"
        assert result[1] == temp_project_root / "notes.txt"


@pytest.mark.unit
class TestCheckArtifactsExist:
    """Test checking if artifacts exist."""

    def test_all_artifacts_exist(self, temp_project_root):
        """Test when all artifacts exist."""
        # Create test files
        test_files = [
            temp_project_root / "file1.md",
            temp_project_root / "file2.py",
            temp_project_root / "file3.yml",
        ]

        for file_path in test_files:
            file_path.write_text("test content")

        result = check_artifacts_exist(test_files)

        assert result == []

    def test_some_artifacts_missing(self, temp_project_root):
        """Test when some artifacts are missing."""
        # Create only some test files
        existing_file = temp_project_root / "existing.md"
        existing_file.write_text("test content")

        test_files = [
            existing_file,
            temp_project_root / "missing1.py",
            temp_project_root / "missing2.yml",
        ]

        result = check_artifacts_exist(test_files)

        assert len(result) == 2
        assert temp_project_root / "missing1.py" in result
        assert temp_project_root / "missing2.yml" in result

    def test_all_artifacts_missing(self, temp_project_root):
        """Test when all artifacts are missing."""
        test_files = [
            temp_project_root / "missing1.md",
            temp_project_root / "missing2.py",
            temp_project_root / "missing3.yml",
        ]

        result = check_artifacts_exist(test_files)

        assert len(result) == 3
        assert all(path in result for path in test_files)


@pytest.mark.integration
class TestMainFunction:
    """Integration tests for main function."""

    def test_main_with_existing_artifacts(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test main function with all artifacts existing."""
        # Setup test files
        from tests.conftest import create_test_artifacts, create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )
        create_test_artifacts(temp_project_root, ["setup.md", "config.yml"])

        with patch(
            "sys.argv", ["check_artifacts.py", "--project-root", str(temp_project_root)]
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

    def test_main_with_missing_artifacts_non_strict(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test main function with missing artifacts in non-strict mode."""
        # Setup test files (without artifacts)
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv", ["check_artifacts.py", "--project-root", str(temp_project_root)]
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

    def test_main_with_missing_artifacts_strict(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test main function with missing artifacts in strict mode."""
        # Setup test files (without artifacts)
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv",
            [
                "check_artifacts.py",
                "--project-root",
                str(temp_project_root),
                "--strict",
            ],
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_with_create_missing_flag(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test main function with create-missing flag."""
        # Setup test files (without artifacts)
        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv",
            [
                "check_artifacts.py",
                "--project-root",
                str(temp_project_root),
                "--create-missing",
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

        # Check that placeholder files were created
        assert (temp_project_root / "delivery" / "setup.md").exists()
        assert (temp_project_root / "config" / "config.yml").exists()

        # Check content of created files
        setup_content = (temp_project_root / "delivery" / "setup.md").read_text()
        assert "# setup.md" in setup_content
        assert "Placeholder file created" in setup_content

    def test_main_with_custom_phase(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test main function with custom phase specified."""
        # Setup test files
        from tests.conftest import create_test_artifacts, create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )
        create_test_artifacts(temp_project_root, ["use-case.md", "requirements.md"])

        with patch(
            "sys.argv",
            [
                "check_artifacts.py",
                "--project-root",
                str(temp_project_root),
                "--phase",
                "discovery",
            ],
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

    def test_main_with_no_artifacts_required(
        self, temp_project_root, sample_pipeline_config, sample_active_session
    ):
        """Test main function when no artifacts are required for phase."""
        # Modify config to have phase with no artifacts
        sample_pipeline_config["phases"][0]["artifacts"] = []

        from tests.conftest import create_test_files

        create_test_files(
            temp_project_root, sample_pipeline_config, sample_active_session
        )

        with patch(
            "sys.argv", ["check_artifacts.py", "--project-root", str(temp_project_root)]
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_not_called()

    def test_main_missing_phase_in_session(
        self, temp_project_root, sample_pipeline_config
    ):
        """Test main function when phase is missing from session."""
        session_content = """# Active Session

## Current Work
```yaml
mode: "build"
agent: "conductor"
```"""

        from tests.conftest import create_test_files

        create_test_files(temp_project_root, sample_pipeline_config, session_content)

        with patch(
            "sys.argv", ["check_artifacts.py", "--project-root", str(temp_project_root)]
        ):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1


@pytest.mark.unit
class TestErrorHandling:
    """Test error handling scenarios."""

    def test_artifact_path_resolution_edge_cases(
        self, temp_project_root, sample_pipeline_config
    ):
        """Test edge cases in artifact path resolution."""
        # Test with empty artifacts list
        result = resolve_artifact_paths(temp_project_root, [], sample_pipeline_config)
        assert result == []

        # Test with artifacts that have special characters
        artifacts = [
            "file with spaces.md",
            "file-with-dashes.py",
            "file_with_underscores.yml",
        ]
        result = resolve_artifact_paths(
            temp_project_root, artifacts, sample_pipeline_config
        )
        assert len(result) == 3
        assert all(isinstance(path, Path) for path in result)

    def test_missing_artifact_paths_config(self, temp_project_root):
        """Test handling when artifact_paths config is missing."""
        config = {"phases": [{"name": "test", "artifacts": ["test.md"]}]}

        artifacts = ["test.md"]
        result = resolve_artifact_paths(temp_project_root, artifacts, config)

        # Should fall back to default behavior
        assert len(result) == 1
        assert result[0] == temp_project_root / "delivery" / "test.md"


if __name__ == "__main__":
    pytest.main([__file__])
