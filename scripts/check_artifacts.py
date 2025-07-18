#!/usr/bin/env python3
"""
check_artifacts.py - AgenticOps Value Train Artifact Validation

Verifies that all required artifacts from pipeline.yml exist in the file system.
Ensures deliverables are present before allowing CI to pass.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import List

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


def load_active_session(project_root: Path) -> dict:
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

        # Parse the YAML
        current_work_str = "\n".join(current_work_yaml)
        return yaml.safe_load(current_work_str)

    except Exception as e:
        logger.error(f"Error parsing ACTIVE_SESSION.md: {e}")
        sys.exit(1)


def get_phase_artifacts(pipeline_config: dict, phase_name: str) -> List[str]:
    """Get required artifacts for a specific phase."""
    phases = pipeline_config.get("phases", [])

    for phase in phases:
        if phase.get("name") == phase_name:
            return phase.get("artifacts", [])

    logger.warning(f"Phase '{phase_name}' not found in pipeline configuration")
    return []


def resolve_artifact_paths(
    project_root: Path, artifacts: List[str], pipeline_config: dict
) -> List[Path]:
    """Resolve artifact names to actual file paths."""
    resolved_paths = []
    artifact_paths = pipeline_config.get("artifact_paths", {})

    for artifact in artifacts:
        # Handle different artifact path patterns
        if artifact.startswith("/"):
            # Absolute path from project root
            artifact_path = project_root / artifact.lstrip("/")
        elif artifact.endswith(".md"):
            # Documentation files
            if (
                "opportunity" in artifact
                or "use-case" in artifact
                or "ai-readiness" in artifact
            ):
                base_path = artifact_paths.get("preengagement", {}).get(
                    "base_path", "/preengagement"
                )
                artifact_path = project_root / base_path.lstrip("/") / artifact
            else:
                base_path = artifact_paths.get("delivery", {}).get(
                    "base_path", "/delivery"
                )
                artifact_path = project_root / base_path.lstrip("/") / artifact
        elif artifact.endswith(".py") or artifact.endswith(".ipynb"):
            # Code and notebook files
            base_path = artifact_paths.get("delivery", {}).get("base_path", "/delivery")
            artifact_path = project_root / base_path.lstrip("/") / artifact
        elif artifact.endswith(".csv"):
            # Data files
            data_path = artifact_paths.get("delivery", {}).get("data", "/delivery/data")
            artifact_path = project_root / data_path.lstrip("/") / artifact
        elif artifact.endswith(".yaml") or artifact.endswith(".yml"):
            # Configuration files
            artifact_path = project_root / "config" / artifact
        else:
            # Default to project root
            artifact_path = project_root / artifact

        resolved_paths.append(artifact_path)

    return resolved_paths


def check_artifacts_exist(artifact_paths: List[Path]) -> List[Path]:
    """Check which artifacts are missing."""
    missing_artifacts = []

    for artifact_path in artifact_paths:
        if not artifact_path.exists():
            missing_artifacts.append(artifact_path)

    return missing_artifacts


def main():
    """Main function to check for missing artifacts."""
    parser = argparse.ArgumentParser(
        description="Check for missing artifacts in current phase"
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Root directory of the project (default: current directory)",
    )
    parser.add_argument(
        "--phase",
        type=str,
        help="Specific phase to check (default: current phase from ACTIVE_SESSION.md)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code 1 if any artifacts are missing",
    )
    parser.add_argument(
        "--create-missing",
        action="store_true",
        help="Create placeholder files for missing artifacts",
    )

    args = parser.parse_args()

    logger.info("Starting artifact validation...")

    # Load pipeline configuration
    pipeline_config = load_pipeline_config(args.project_root)

    # Get current phase
    if args.phase:
        current_phase = args.phase
    else:
        current_work = load_active_session(args.project_root)
        current_phase = current_work.get("phase")
        if not current_phase:
            logger.error("No current phase found in ACTIVE_SESSION.md")
            sys.exit(1)

    logger.info(f"Current phase: {current_phase}")

    # Get required artifacts for current phase
    required_artifacts = get_phase_artifacts(pipeline_config, current_phase)

    if not required_artifacts:
        logger.info(f"No artifacts required for phase '{current_phase}'")
        return

    logger.info(f"Required artifacts: {required_artifacts}")

    # Resolve artifact paths
    artifact_paths = resolve_artifact_paths(
        args.project_root, required_artifacts, pipeline_config
    )

    # Check for missing artifacts
    missing_artifacts = check_artifacts_exist(artifact_paths)

    if missing_artifacts:
        logger.error(f"Found {len(missing_artifacts)} missing artifacts:")
        for artifact_path in missing_artifacts:
            logger.error(f"  Missing: {artifact_path}")

        if args.create_missing:
            logger.info("Creating placeholder files for missing artifacts...")
            for artifact_path in missing_artifacts:
                artifact_path.parent.mkdir(parents=True, exist_ok=True)
                with open(artifact_path, "w") as f:
                    f.write(f"# {artifact_path.name}\n\n")
                    f.write("<!-- Placeholder file created by check_artifacts.py -->\n")
                    f.write(
                        f"<!-- TODO: Add actual content for {artifact_path.name} -->\n"
                    )
                logger.info(f"  Created: {artifact_path}")

        if args.strict and not args.create_missing:
            logger.error("Failing CI due to missing artifacts (--strict mode)")
            sys.exit(1)
        elif not args.create_missing:
            logger.warning(
                "Missing artifacts found but not failing CI (use --strict to fail)"
            )
    else:
        logger.info("✅ All required artifacts are present!")

    logger.info("Artifact validation complete.")


if __name__ == "__main__":
    main()
