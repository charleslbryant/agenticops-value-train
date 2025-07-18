#!/usr/bin/env python3
"""
Simple test runner for AgenticOps scripts when pytest is not available.
"""

import sys
import tempfile
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))


def run_basic_tests():
    """Run basic functionality tests for all scripts."""
    test_results = []

    # Test 1: Check imports
    print("Testing imports...")
    try:
        from check_artifacts import resolve_artifact_paths
        from conductor_update import get_next_phase, get_phase_info
        from migrate_session import detect_legacy_format, parse_json_format

        test_results.append("✅ All imports successful")
    except Exception as e:
        test_results.append(f"❌ Import failed: {e}")
        return test_results

    # Test 2: Legacy format detection
    print("Testing legacy format detection...")
    try:
        json_content = '{"mode": "build", "phase": "enablement"}'
        yaml_content = "---\nmode: build\nphase: enablement\n---"

        assert detect_legacy_format(json_content) == "json"
        assert detect_legacy_format(yaml_content) == "yaml_frontmatter"
        test_results.append("✅ Legacy format detection works")
    except Exception as e:
        test_results.append(f"❌ Legacy format detection failed: {e}")

    # Test 3: JSON parsing
    print("Testing JSON parsing...")
    try:
        json_data = parse_json_format(
            '{"mode": "build", "phase": "enablement", "agent": "conductor"}'
        )
        assert json_data["mode"] == "build"
        assert json_data["phase"] == "enablement"
        assert json_data["agent"] == "conductor"
        test_results.append("✅ JSON parsing works")
    except Exception as e:
        test_results.append(f"❌ JSON parsing failed: {e}")

    # Test 4: Pipeline config structure
    print("Testing pipeline config structure...")
    try:
        pipeline_config = {
            "phases": [
                {"name": "enablement", "next_phase": "discovery"},
                {"name": "discovery", "next_phase": "scope"},
                {"name": "scope", "next_phase": None},
            ]
        }

        assert get_next_phase(pipeline_config, "enablement") == "discovery"
        assert get_next_phase(pipeline_config, "scope") is None

        phase_info = get_phase_info(pipeline_config, "enablement")
        assert phase_info["name"] == "enablement"
        test_results.append("✅ Pipeline config handling works")
    except Exception as e:
        test_results.append(f"❌ Pipeline config handling failed: {e}")

    # Test 5: File path resolution
    print("Testing file path resolution...")
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            pipeline_config = {
                "artifact_paths": {
                    "delivery": {"base_path": "/delivery"},
                    "preengagement": {"base_path": "/preengagement"},
                }
            }

            artifacts = ["test.py", "config.yml"]
            resolved = resolve_artifact_paths(temp_path, artifacts, pipeline_config)

            assert len(resolved) == 2
            assert all(isinstance(p, Path) for p in resolved)
            test_results.append("✅ File path resolution works")
    except Exception as e:
        test_results.append(f"❌ File path resolution failed: {e}")

    return test_results


def main():
    """Run all tests and display results."""
    print("=" * 60)
    print("AgenticOps Value Train - Script Test Runner")
    print("=" * 60)

    results = run_basic_tests()

    print("\nTest Results:")
    print("-" * 40)
    for result in results:
        print(result)

    # Count passed/failed
    passed = sum(1 for r in results if r.startswith("✅"))
    failed = sum(1 for r in results if r.startswith("❌"))

    print("-" * 40)
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️  {failed} test(s) failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
