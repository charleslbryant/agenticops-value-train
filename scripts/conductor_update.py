#!/usr/bin/env python3
"""
conductor_update.py - AgenticOps Value Train Phase Automation

Moves ACTIVE_SESSION.md to the next phase after successful CI completion.
Automates the "Conductor" agent role for seamless workflow transitions.
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_pipeline_config(project_root: Path) -> dict:
    """Load pipeline configuration from config/pipeline.yml."""
    pipeline_path = project_root / "config" / "pipeline.yml"

    if not pipeline_path.exists():
        logger.error(f"Pipeline configuration not found at {pipeline_path}")
        sys.exit(1)

    try:
        with open(pipeline_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading pipeline configuration: {e}")
        sys.exit(1)


def load_active_session(project_root: Path) -> Tuple[dict, str]:
    """Load current session context from ACTIVE_SESSION.md."""
    active_session_path = (
        project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
    )

    if not active_session_path.exists():
        logger.error(f"ACTIVE_SESSION.md not found at {active_session_path}")
        sys.exit(1)

    try:
        with open(active_session_path, "r") as f:
            content = f.read()

        # Parse YAML sections
        sections = {}
        current_section = None
        yaml_content = []
        in_yaml = False

        for line in content.split("\n"):
            if line.startswith("## ") and "yaml" not in line.lower():
                if current_section and yaml_content:
                    sections[current_section] = "\n".join(yaml_content)
                    yaml_content = []
                current_section = line[3:].strip()
                in_yaml = False
            elif line.strip() == "```yaml" and current_section:
                in_yaml = True
            elif line.strip() == "```" and in_yaml:
                in_yaml = False
            elif in_yaml and current_section:
                yaml_content.append(line)

        # Add the last section
        if current_section and yaml_content:
            sections[current_section] = "\n".join(yaml_content)

        return sections, content

    except Exception as e:
        logger.error(f"Error parsing ACTIVE_SESSION.md: {e}")
        sys.exit(1)


def get_next_phase(pipeline_config: dict, current_phase: str) -> Optional[str]:
    """Get the next phase in the pipeline."""
    phases = pipeline_config.get("phases", [])

    for phase in phases:
        if phase.get("name") == current_phase:
            return phase.get("next_phase")

    return None


def get_phase_info(pipeline_config: dict, phase_name: str) -> Optional[dict]:
    """Get phase information from pipeline configuration."""
    phases = pipeline_config.get("phases", [])

    for phase in phases:
        if phase.get("name") == phase_name:
            return phase

    return None


def update_session_phase(
    project_root: Path,
    content: str,
    sections: dict,
    next_phase: str,
    next_phase_info: dict,
) -> str:
    """Update the session content with new phase information."""
    try:
        # Parse current work section
        current_work_yaml = sections.get("Current Work", "")
        if current_work_yaml:
            current_work = yaml.safe_load(current_work_yaml)
        else:
            current_work = {}

        # Update phase information
        current_work["phase"] = next_phase
        current_work["mode"] = next_phase_info.get("mode", current_work.get("mode"))

        # Update timestamps
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update session metadata
        session_metadata_yaml = sections.get("Session Metadata", "")
        if session_metadata_yaml:
            session_metadata = yaml.safe_load(session_metadata_yaml)
            session_metadata["last_updated"] = current_time

        # Update session notes
        session_notes_yaml = sections.get("Session Notes", "")
        if session_notes_yaml:
            session_notes = yaml.safe_load(session_notes_yaml)
            if "decisions" not in session_notes:
                session_notes["decisions"] = []
            session_notes["decisions"].append(
                f"Advanced to {next_phase} phase via conductor automation"
            )

            if "next_steps" not in session_notes:
                session_notes["next_steps"] = []
            session_notes["next_steps"] = [
                f"Begin {next_phase} phase activities",
                f"Review {next_phase} checklist requirements",
                "Update task assignments for new phase",
            ]

        # Reconstruct the file content
        new_content = content

        # Replace Current Work section
        current_work_str = yaml.dump(
            current_work, default_flow_style=False, sort_keys=False
        )
        new_content = replace_yaml_section(
            new_content, "Current Work", current_work_str
        )

        # Replace Session Metadata section
        if session_metadata_yaml:
            session_metadata_str = yaml.dump(
                session_metadata, default_flow_style=False, sort_keys=False
            )
            new_content = replace_yaml_section(
                new_content, "Session Metadata", session_metadata_str
            )

        # Replace Session Notes section
        if session_notes_yaml:
            session_notes_str = yaml.dump(
                session_notes, default_flow_style=False, sort_keys=False
            )
            new_content = replace_yaml_section(
                new_content, "Session Notes", session_notes_str
            )

        return new_content

    except Exception as e:
        logger.error(f"Error updating session phase: {e}")
        sys.exit(1)


def replace_yaml_section(content: str, section_name: str, new_yaml: str) -> str:
    """Replace a YAML section in the content."""
    lines = content.split("\n")
    new_lines = []
    in_section = False
    in_yaml = False

    for line in lines:
        if line.strip() == f"## {section_name}":
            in_section = True
            new_lines.append(line)
        elif in_section and line.strip() == "```yaml":
            in_yaml = True
            new_lines.append(line)
            # Add the new YAML content
            for yaml_line in new_yaml.strip().split("\n"):
                new_lines.append(yaml_line)
        elif in_section and in_yaml and line.strip() == "```":
            in_yaml = False
            in_section = False
            new_lines.append(line)
        elif not (in_section and in_yaml):
            new_lines.append(line)

    return "\n".join(new_lines)


def save_active_session(project_root: Path, content: str):
    """Save updated session content to ACTIVE_SESSION.md."""
    active_session_path = (
        project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
    )

    try:
        with open(active_session_path, "w") as f:
            f.write(content)
        logger.info(f"Updated ACTIVE_SESSION.md at {active_session_path}")
    except Exception as e:
        logger.error(f"Error saving ACTIVE_SESSION.md: {e}")
        sys.exit(1)


def main():
    """Main function to advance session to next phase."""
    parser = argparse.ArgumentParser(description="Advance session to next phase")
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Root directory of the project (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be updated without making changes",
    )
    parser.add_argument(
        "--force-phase",
        type=str,
        help="Force advance to specific phase (bypasses normal progression)",
    )

    args = parser.parse_args()

    logger.info("Starting conductor phase advancement...")

    # Load pipeline configuration
    pipeline_config = load_pipeline_config(args.project_root)

    # Load current session
    sections, content = load_active_session(args.project_root)

    # Get current phase
    current_work_yaml = sections.get("Current Work", "")
    if not current_work_yaml:
        logger.error("No Current Work section found in ACTIVE_SESSION.md")
        sys.exit(1)

    current_work = yaml.safe_load(current_work_yaml)
    current_phase = current_work.get("phase")

    if not current_phase:
        logger.error("No current phase found in ACTIVE_SESSION.md")
        sys.exit(1)

    logger.info(f"Current phase: {current_phase}")

    # Determine next phase
    if args.force_phase:
        next_phase = args.force_phase
        logger.info(f"Forcing advance to phase: {next_phase}")
    else:
        next_phase = get_next_phase(pipeline_config, current_phase)
        if not next_phase:
            logger.info(
                f"No next phase found for '{current_phase}' - pipeline complete!"
            )
            return

    # Get next phase information
    next_phase_info = get_phase_info(pipeline_config, next_phase)
    if not next_phase_info:
        logger.error(f"Phase '{next_phase}' not found in pipeline configuration")
        sys.exit(1)

    logger.info(f"Advancing to phase: {next_phase}")
    logger.info(f"Next phase mode: {next_phase_info.get('mode')}")
    logger.info(f"Next phase owner: {next_phase_info.get('owner')}")

    # Update session content
    new_content = update_session_phase(
        args.project_root, content, sections, next_phase, next_phase_info
    )

    if args.dry_run:
        logger.info(
            "DRY RUN - Would update ACTIVE_SESSION.md with new phase information"
        )
        logger.info("Updated content preview:")
        print("=" * 50)
        print(new_content[:1000] + "..." if len(new_content) > 1000 else new_content)
        print("=" * 50)
    else:
        # Save updated session
        save_active_session(args.project_root, new_content)
        logger.info("✅ Session successfully advanced to next phase!")

    logger.info("Conductor phase advancement complete.")


if __name__ == "__main__":
    main()
