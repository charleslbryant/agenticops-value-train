#!/usr/bin/env python3
"""
check_todo.py - AgenticOps Value Train CI Validation

Fails CI if any unchecked items exist in active checklist files.
Ensures all checklist items are completed before allowing PR merge.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import List, Tuple

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def find_active_session_file(project_root: Path) -> Path:
    """Find the ACTIVE_SESSION.md file."""
    active_session_path = (
        project_root / "docs" / "session-context" / "ACTIVE_SESSION.md"
    )

    if not active_session_path.exists():
        logger.error(f"ACTIVE_SESSION.md not found at {active_session_path}")
        sys.exit(1)

    return active_session_path


def parse_active_session(active_session_path: Path) -> dict:
    """Parse ACTIVE_SESSION.md to extract current mode and phase."""
    try:
        with open(active_session_path, "r") as f:
            content = f.read()

        # Extract YAML blocks
        lines = content.split("\n")
        current_work_yaml = []
        in_current_work = False

        for line in lines:
            if line.strip() == "## Current Work":
                in_current_work = True
                continue
            elif in_current_work and line.strip() == "```yaml":
                continue
            elif in_current_work and line.strip() == "```":
                break
            elif in_current_work:
                current_work_yaml.append(line)

        # Check if we found any content
        if not current_work_yaml:
            return {}

        # Parse the YAML
        current_work_str = "\n".join(current_work_yaml)
        current_work = yaml.safe_load(current_work_str)

        return current_work if current_work else {}

    except Exception as e:
        logger.error(f"Error parsing ACTIVE_SESSION.md: {e}")
        sys.exit(1)


def find_active_checklist(project_root: Path, mode: str) -> Path:
    """Find the active checklist file for the current mode."""
    checklist_path = (
        project_root / "docs" / "rules" / "checklists" / f"{mode}-checklist.md"
    )

    if not checklist_path.exists():
        logger.error(f"Checklist file not found: {checklist_path}")
        sys.exit(1)

    return checklist_path


def check_unchecked_items(checklist_path: Path) -> List[Tuple[int, str]]:
    """Check for unchecked items in checklist file."""
    unchecked_items = []

    try:
        with open(checklist_path, "r") as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, 1):
            # Look for unchecked checkbox patterns
            if "- [ ]" in line or "* [ ]" in line:
                unchecked_items.append((line_num, line.strip()))

        return unchecked_items

    except Exception as e:
        logger.error(f"Error reading checklist file {checklist_path}: {e}")
        sys.exit(1)


def main():
    """Main function to check for unchecked todo items."""
    parser = argparse.ArgumentParser(
        description="Check for unchecked todo items in active checklist"
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Root directory of the project (default: current directory)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code 1 if any unchecked items found",
    )

    args = parser.parse_args()

    logger.info("Starting todo checklist validation...")

    # Find and parse active session
    active_session_path = find_active_session_file(args.project_root)
    current_work = parse_active_session(active_session_path)

    # Get current mode
    current_mode = current_work.get("mode")
    if not current_mode:
        logger.error("No current mode found in ACTIVE_SESSION.md")
        sys.exit(1)

    logger.info(f"Current mode: {current_mode}")

    # Find active checklist
    checklist_path = find_active_checklist(args.project_root, current_mode)
    logger.info(f"Checking checklist: {checklist_path}")

    # Check for unchecked items
    unchecked_items = check_unchecked_items(checklist_path)

    if unchecked_items:
        logger.error(
            f"Found {len(unchecked_items)} unchecked items in {checklist_path.name}:"
        )
        for line_num, item in unchecked_items:
            logger.error(f"  Line {line_num}: {item}")

        if args.strict:
            logger.error("Failing CI due to unchecked items (--strict mode)")
            sys.exit(1)
        else:
            logger.warning(
                "Unchecked items found but not failing CI (use --strict to fail)"
            )
    else:
        logger.info("✅ All checklist items are completed!")

    logger.info("Todo checklist validation complete.")


if __name__ == "__main__":
    main()
