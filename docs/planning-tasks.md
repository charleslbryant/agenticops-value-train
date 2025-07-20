# Planning Tasks and Ideas

This document captures tasks, ideas, and changes to review during `/plan` mode sessions. These items should be converted to GitHub issues and removed from this document as they are created in the `/plan` mode.

## Pending Tasks to Create Issues For

- Run flake8, black, and isort on relevant python files before committing. Update the `docs/rules/git-workflow.md` file to reflect the new process.
- Always run python file in venv. Update CLAUDE.md to reflect the new process.
- Run the same CI/CD pipeline as we do in GitHub Actions (`.github/workflows/ci.yml`). Update the `docs/rules/git-workflow.md` file to reflect the new process.
  source venv/bin/activate
  pip install flake8 black isort mypy types-PyYAML
  flake8 scripts/ tests/ --max-line-length=88 --extend-ignore=E203,W503
  black --check scripts/ tests/
  isort --check-only scripts/ tests/
  mypy scripts/
- Add "meta" as a GitHub label for issues that are not counted towards flow metrics. Update the `docs/rules/task-management.md` file to reflect the new process.

## Recently Created Issues

- [#11 Implement dependency tracking for parallel task execution](https://github.com/charleslbryant/agenticops-value-train/issues/11)
- [#12 Update all file paths to use Claude @includes format](https://github.com/charleslbryant/agenticops-value-train/issues/12)  
- [#13 Integrate and align command structures](https://github.com/charleslbryant/agenticops-value-train/issues/13)

---

## Notes and Observations

- Consider creating a "Task Dependencies" section in each checklist file
- The @includes format will significantly reduce token usage when referencing files
- Command integration will help maintain single source of truth for workflows

## Future Considerations

- Automated dependency validation in CI/CD
- Command validation against mode definitions
- Context optimization metrics tracking