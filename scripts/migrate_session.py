#!/usr/bin/env python3
"""
migrate_session.py - AgenticOps Value Train Legacy Migration

One-time migration utility to merge legacy session context into new YAML format.
Converts old session formats to the current ACTIVE_SESSION.md schema.
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def detect_legacy_format(content: str) -> str:
    """Detect the format of legacy session context."""
    content = content.strip()

    if content.startswith("{") and content.endswith("}"):
        try:
            json.loads(content)
            return "json"
        except json.JSONDecodeError:
            pass

    if "---" in content and ("mode:" in content or "phase:" in content):
        return "yaml_frontmatter"

    if content.startswith("# ") and "## " in content:
        return "markdown"

    if "mode=" in content or "phase=" in content:
        return "key_value"

    return "unknown"


def parse_json_format(content: str) -> Dict[str, Any]:
    """Parse JSON format legacy session."""
    try:
        data = json.loads(content)
        return {
            "mode": data.get("mode", "build"),
            "phase": data.get("phase", "enablement"),
            "agent": data.get("agent", "conductor"),
            "task": data.get("task", {}),
            "decisions": data.get("decisions", []),
            "next_steps": data.get("next_steps", []),
        }
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON format: {e}")
        return {}


def parse_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """Parse YAML frontmatter format legacy session."""
    try:
        # Split on first --- boundary
        parts = content.split("---", 2)
        if len(parts) >= 2:
            yaml_content = parts[1].strip()
            data = yaml.safe_load(yaml_content)
            return {
                "mode": data.get("mode", "build"),
                "phase": data.get("phase", "enablement"),
                "agent": data.get("agent", "conductor"),
                "task": data.get("task", {}),
                "decisions": data.get("decisions", []),
                "next_steps": data.get("next_steps", []),
            }
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML frontmatter: {e}")
    return {}


def parse_markdown_format(content: str) -> Dict[str, Any]:
    """Parse markdown format legacy session."""
    data: Dict[str, Any] = {
        "mode": "build",
        "phase": "enablement",
        "agent": "conductor",
        "task": {},
        "decisions": [],
        "next_steps": [],
    }

    lines = content.split("\n")
    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith("# ") or line.startswith("## "):
            current_section = line.lstrip("# ").lower()
        elif current_section == "mode" and line:
            data["mode"] = line
        elif current_section == "phase" and line:
            data["phase"] = line
        elif current_section == "agent" and line:
            data["agent"] = line
        elif current_section == "task" and line:
            # Try to parse task info
            if ":" in line:
                key, value = line.split(":", 1)
                if "task" not in data:
                    data["task"] = {}
                data["task"][key.strip()] = value.strip()
        elif (
            current_section and "decision" in current_section and line.startswith("- ")
        ):
            data["decisions"].append(line[2:])
        elif current_section and "next" in current_section and line.startswith("- "):
            data["next_steps"].append(line[2:])

    return data


def parse_key_value_format(content: str) -> Dict[str, Any]:
    """Parse key=value format legacy session."""
    data: Dict[str, Any] = {
        "mode": "build",
        "phase": "enablement",
        "agent": "conductor",
        "task": {},
        "decisions": [],
        "next_steps": [],
    }

    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("\"'")

            if key in ["mode", "phase", "agent"]:
                data[key] = value
            elif key.startswith("task."):
                task_key = key[5:]  # Remove 'task.' prefix
                if "task" not in data:
                    data["task"] = {}
                data["task"][task_key] = value
            elif key == "decisions":
                data["decisions"] = [v.strip() for v in value.split(",")]
            elif key == "next_steps":
                data["next_steps"] = [v.strip() for v in value.split(",")]

    return data


def generate_new_session_content(legacy_data: Dict, project_root: Path) -> str:
    """Generate new ACTIVE_SESSION.md content from legacy data."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session_id = datetime.now().strftime("%Y-%m-%d-%H%M%S")

    # Build task information
    task_info = legacy_data.get("task", {})
    if isinstance(task_info, dict):
        task_yaml = f"""  issue_number: {task_info.get('issue_number', 'unknown')}
  title: "{task_info.get('title', 'Migrated from legacy session')}"
  url: "{task_info.get('url', 'https://github.com/example/repo/issues/1')}"
  priority: "{task_info.get('priority', 'now')}"
  status: "{task_info.get('status', 'In progress')}\""""
    else:
        task_yaml = """  issue_number: unknown
  title: "Migrated from legacy session"
  url: "https://github.com/example/repo/issues/1"
  priority: "now"
  status: "In progress\""""

    # Build decisions and next steps
    decisions = legacy_data.get("decisions", []) or []
    next_steps = legacy_data.get("next_steps", []) or []

    def escape_quotes(text):
        return text.replace('"', '\\"')

    decisions_yaml = "\n".join(
        [f'  - "{escape_quotes(decision)}"' for decision in decisions]
    )
    next_steps_yaml = "\n".join([f'  - "{escape_quotes(step)}"' for step in next_steps])

    if not decisions_yaml:
        decisions_yaml = '  - "Migrated from legacy session format"'

    if not next_steps_yaml:
        next_steps_yaml = '  - "Review and update session context"'

    # Build mode comment with line breaks for readability
    mode_comment = (
        "# intake|discover|scope|design|build|evaluate|deliver|operate|improve"
    )
    phase_comment = "# From pipeline.yml phases"
    agent_comment = "# conductor|onboarder|lab|studio|ops|evaluator|improver"

    content = f"""# Active Session Context

## Session Metadata
```yaml
session_id: "{session_id}"
started_at: "{current_time}"
last_updated: "{current_time}"
operator: "unknown"
assistant: "Claude Code"
```

## Current Work
```yaml
mode: "{legacy_data.get('mode') or 'build'}"  {mode_comment}
phase: "{legacy_data.get('phase') or 'enablement'}"  {phase_comment}
agent: "{legacy_data.get('agent') or 'conductor'}"  {agent_comment}
task:
{task_yaml}
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
  id: null
  name: "Migrated Project"
  url: null
```

## Work Progress
```yaml
todos:
  - content: "Review migrated session context"
    status: "pending"
    priority: "high"
    id: "1"
  - content: "Update session metadata with correct information"
    status: "pending"
    priority: "medium"
    id: "2"
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
{decisions_yaml}
blockers: []
next_steps:
{next_steps_yaml}
handoff_requirements: []
```

## Git Context
```yaml
repository: "unknown"
current_branch: "main"
working_directory: "{project_root}"
uncommitted_changes: false
last_commit: "unknown"
```

## Tool Access
```yaml
allowed_tools:
  - "Read"
  - "Write"
  - "TodoWrite"
  - "Bash(git:*)"
  - "Bash(gh:*)"
  - "Bash(python:*)"
  - "Bash(test:*)"
restricted_tools: []
```

---

## Schema Definition

This file follows the AgenticOps session context schema:

### Required Fields
- `session_id`: Unique identifier for the session
- `started_at`: ISO 8601 timestamp when session began
- `operator`: GitHub username of the human operator
- `mode`: Current operating mode from pipeline.yml
- `phase`: Current phase from pipeline.yml
- `agent`: Current agent role from pipeline.yml
- `task`: Current GitHub issue being worked on

### Optional Fields
- `parent_crd`: Reference to parent CRD issue if applicable
- `parent_prd`: Reference to parent PRD issue if applicable
- `todos`: Current TodoWrite list for tracking progress
- `artifacts`: Files created/modified during session
- `decisions`: Key decisions made during session
- `blockers`: Any blockers encountered
- `next_steps`: Planned next actions
- `handoff_requirements`: Items needed for agent handoff

### Update Requirements
- Update `last_updated` timestamp on any changes
- Update `todos` section when TodoWrite is used
- Update `artifacts` when files are created/modified
- Add to `decisions` for any significant choices made
- Add to `blockers` for any impediments encountered
"""

    return content


def main():
    """Main function to migrate legacy session format."""
    parser = argparse.ArgumentParser(
        description="Migrate legacy session context to new format"
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Root directory of the project (default: current directory)",
    )
    parser.add_argument(
        "--legacy-file",
        type=Path,
        required=True,
        help="Path to legacy session context file",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        help="Output file path (default: docs/session-context/ACTIVE_SESSION.md)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without creating files",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create backup of existing ACTIVE_SESSION.md",
    )

    args = parser.parse_args()

    logger.info("Starting legacy session migration...")

    # Check if legacy file exists
    if not args.legacy_file.exists():
        logger.error(f"Legacy file not found: {args.legacy_file}")
        sys.exit(1)

    # Read legacy content
    try:
        with open(args.legacy_file, "r") as f:
            legacy_content = f.read()
    except Exception as e:
        logger.error(f"Error reading legacy file: {e}")
        sys.exit(1)

    logger.info(f"Read legacy file: {args.legacy_file}")

    # Detect format
    format_type = detect_legacy_format(legacy_content)
    logger.info(f"Detected legacy format: {format_type}")

    # Parse legacy content
    if format_type == "json":
        legacy_data = parse_json_format(legacy_content)
    elif format_type == "yaml_frontmatter":
        legacy_data = parse_yaml_frontmatter(legacy_content)
    elif format_type == "markdown":
        legacy_data = parse_markdown_format(legacy_content)
    elif format_type == "key_value":
        legacy_data = parse_key_value_format(legacy_content)
    else:
        logger.error(f"Unknown legacy format: {format_type}")
        sys.exit(1)

    if not legacy_data:
        logger.error("Failed to parse legacy content")
        sys.exit(1)

    logger.info(f"Parsed legacy data: {legacy_data}")

    # Generate new content
    new_content = generate_new_session_content(legacy_data, args.project_root)

    # Determine output file
    if args.output_file:
        output_file = args.output_file
    else:
        output_file = (
            args.project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
        )

    # Create output directory if needed
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Backup existing file if requested
    if args.backup and output_file.exists():
        backup_file = output_file.with_suffix(".md.backup")
        backup_file.write_text(output_file.read_text())
        logger.info(f"Created backup: {backup_file}")

    if args.dry_run:
        logger.info("DRY RUN - Would create new ACTIVE_SESSION.md:")
        print("=" * 50)
        print(new_content)
        print("=" * 50)
    else:
        # Write new content
        try:
            with open(output_file, "w") as f:
                f.write(new_content)
            logger.info(f"Created new ACTIVE_SESSION.md: {output_file}")
        except Exception as e:
            logger.error(f"Error writing output file: {e}")
            sys.exit(1)

    logger.info("✅ Legacy session migration complete!")


if __name__ == "__main__":
    main()
