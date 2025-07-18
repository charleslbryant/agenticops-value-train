"""
Test fixtures and utilities for AgenticOps Value Train tests.
"""

import tempfile
from pathlib import Path
from typing import Any, Dict

import pytest
import yaml


@pytest.fixture
def temp_project_root():
    """Create a temporary project directory structure."""
    with tempfile.TemporaryDirectory() as temp_dir:
        project_root = Path(temp_dir)

        # Create directory structure
        (project_root / "docs" / "session-context").mkdir(parents=True)
        (project_root / "docs" / "rules" / "checklists").mkdir(parents=True)
        (project_root / "config").mkdir(parents=True)
        (project_root / "scripts").mkdir(parents=True)

        yield project_root


@pytest.fixture
def sample_pipeline_config():
    """Sample pipeline configuration for testing."""
    return {
        "metadata": {"name": "Test Pipeline", "version": "1.0.0"},
        "phases": [
            {
                "name": "enablement",
                "description": "Setup and enablement phase",
                "mode": "build",
                "owner": "conductor",
                "artifacts": ["setup.md", "config.yml"],
                "next_phase": "discovery",
            },
            {
                "name": "discovery",
                "description": "Discovery phase",
                "mode": "discover",
                "owner": "onboarder",
                "artifacts": ["use-case.md", "requirements.md"],
                "next_phase": "scope",
            },
            {
                "name": "scope",
                "description": "Scope phase",
                "mode": "scope",
                "owner": "onboarder",
                "artifacts": ["scope.md"],
                "next_phase": None,
            },
        ],
        "modes": [
            {
                "name": "build",
                "description": "Build mode",
                "agents": ["conductor"],
                "allowed_tools": ["Read", "Write"],
            },
            {
                "name": "discover",
                "description": "Discover mode",
                "agents": ["onboarder"],
                "allowed_tools": ["Read", "Write", "WebFetch"],
            },
        ],
        "artifact_paths": {
            "preengagement": {"base_path": "/preengagement"},
            "delivery": {"base_path": "/delivery"},
        },
    }


@pytest.fixture
def sample_active_session():
    """Sample ACTIVE_SESSION.md content for testing."""
    return """# Active Session Context

## Session Metadata
```yaml
session_id: "2025-01-18-test"
started_at: "2025-01-18 10:00:00"
last_updated: "2025-01-18 10:30:00"
operator: "testuser"
assistant: "Claude Code"
```

## Current Work
```yaml
mode: "build"
phase: "enablement"
agent: "conductor"
task:
  issue_number: 1
  title: "Test task"
  url: "https://github.com/test/repo/issues/1"
  priority: "now"
  status: "In progress"
branch: "main"
```

## Task Context
```yaml
parent_crd:
  issue_number: null
  title: null
  url: null
parent_prd:
  issue_number: null
  title: null
  url: null
project:
  id: 1
  name: "Test Project"
  url: "https://github.com/test/repo"
```

## Work Progress
```yaml
todos:
  - content: "Test todo item"
    status: "pending"
    priority: "high"
    id: "1"
```

## Artifacts
```yaml
created_files: []
modified_files: []
dependencies: []
```

## Session Notes
```yaml
decisions:
  - "Test decision"
blockers: []
next_steps:
  - "Test next step"
handoff_requirements: []
```

## Git Context
```yaml
repository: "test-repo"
current_branch: "main"
working_directory: "/tmp/test"
uncommitted_changes: false
last_commit: "abc123"
```

## Tool Access
```yaml
allowed_tools:
  - "Read"
  - "Write"
restricted_tools: []
```
"""


@pytest.fixture
def sample_checklist_with_unchecked():
    """Sample checklist with unchecked items."""
    return """# Build Mode Checklist

## Entry Criteria
- [x] Requirements completed
- [ ] Data access confirmed
- [ ] Team ready

## Core Activities
- [x] Setup environment
- [ ] Write code
- [ ] Run tests
- [ ] Create documentation

## Exit Criteria
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation complete
"""


@pytest.fixture
def sample_checklist_all_checked():
    """Sample checklist with all items checked."""
    return """# Build Mode Checklist

## Entry Criteria
- [x] Requirements completed
- [x] Data access confirmed
- [x] Team ready

## Core Activities
- [x] Setup environment
- [x] Write code
- [x] Run tests
- [x] Create documentation

## Exit Criteria
- [x] All tests passing
- [x] Code reviewed
- [x] Documentation complete
"""


@pytest.fixture
def sample_legacy_json():
    """Sample legacy JSON format session."""
    return """{
    "mode": "build",
    "phase": "enablement",
    "agent": "conductor",
    "task": {
        "issue_number": 1,
        "title": "Legacy task",
        "status": "In progress"
    },
    "decisions": ["Legacy decision 1", "Legacy decision 2"],
    "next_steps": ["Legacy step 1", "Legacy step 2"]
}"""


@pytest.fixture
def sample_legacy_yaml_frontmatter():
    """Sample legacy YAML frontmatter format."""
    return """---
mode: build
phase: enablement
agent: conductor
task:
  issue_number: 1
  title: Legacy task
  status: In progress
decisions:
  - Legacy decision 1
  - Legacy decision 2
next_steps:
  - Legacy step 1
  - Legacy step 2
---

# Legacy Session Content

This is the legacy session content.
"""


def create_test_files(
    project_root: Path, pipeline_config: Dict[str, Any], active_session: str
):
    """Helper to create test files in project structure."""
    # Create pipeline config
    with open(project_root / "config" / "pipeline.yml", "w") as f:
        yaml.dump(pipeline_config, f)

    # Create active session
    with open(
        project_root / "docs" / "session-context" / "ACTIVE_SESSION.md", "w"
    ) as f:
        f.write(active_session)


def create_test_checklist(project_root: Path, mode: str, content: str):
    """Helper to create test checklist files."""
    checklist_path = (
        project_root / "docs" / "rules" / "checklists" / f"{mode}-checklist.md"
    )
    with open(checklist_path, "w") as f:
        f.write(content)


def create_test_artifacts(project_root: Path, artifacts: list):
    """Helper to create test artifact files."""
    for artifact in artifacts:
        artifact_path = project_root / artifact
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        with open(artifact_path, "w") as f:
            f.write(f"# {artifact}\n\nTest content for {artifact}")
