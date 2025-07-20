# AgenticOps Value Train Alignment Plan

This document outlines the comprehensive plan to bring the AgenticOps repository into full alignment with the Value Train™ methodology. Each change is detailed with rationale, implementation approach, dependencies, and proper task organization following PRD/CRD/Task hierarchy.

## Executive Summary

The repository has ~60% of the Value Train infrastructure implemented. Key gaps include automation tooling (Makefile, git hooks), workflow orchestration (conductor.yml, Auto-Pilot), and some structural elements. This plan addresses all gaps systematically.

## Current State Assessment

### ✅ Implemented (What We Have)
- Core directory structure and mode checklists
- Python helper scripts with comprehensive tests
- Basic CI/CD pipeline
- Session management framework
- Asset registry and pipeline configuration

### ❌ Missing (What We Need)
- Build automation (Makefile)
- Git hooks for quality gates
- Conductor workflow automation
- Auto-Pilot implementation
- Risk registry operationalization
- Complete GitHub templates
- Architecture documentation

## Issue Hierarchy Structure

Following the task management rules, this plan is organized into a new PRD with multiple CRDs, each containing specific implementation tasks. This PRD will be created as a child of the existing PRD #1 (AgenticOps Value Train Platform).

### New PRD: Complete Value Train Infrastructure
**Parent**: PRD #1 (AgenticOps Value Train Platform)  

**Goal**: Implement remaining infrastructure components to achieve full Value Train compliance 

**Priority**: next (will become "now" after current work completes)  

**Phase**: phase:enablement  

**Labels**: PRD, phase:enablement, next

**Success Criteria**:
- All builds automated via Makefile
- Git hooks prevent quality regressions
- Conductor automates phase transitions
- Auto-Pilot can run issues end-to-end
- Risk registry actively tracks system health
- Complete documentation and templates

## CRD Structure

### CRD-A: Operator Build Automation

**Parent PRD**: Complete Value Train Infrastructure  

**User Story**: As an operator, I can use `make` commands to manage my development environment so that setup and testing are consistent across the team.  

**Labels**: CRD, phase:enablement, agent:ops, next  

**Acceptance Criteria**:
- [ ] Makefile exists with standard targets
- [ ] Virtual environment setup automated
- [ ] Linting and testing integrated
- [ ] CI pipeline can run locally
- [ ] Documentation updated

### CRD-B: Quality Gate Automation

**Parent PRD**: Complete Value Train Infrastructure  

**User Story**: As a lead operator, I need git hooks to enforce standards so that bad commits never reach the repository.  

**Labels**: CRD, phase:enablement, agent:ops, next  

**Acceptance Criteria**:
- [ ] Pre-commit hooks validate commit messages
- [ ] YAML headers checked automatically
- [ ] File size limits enforced
- [ ] Pre-push hooks run tests
- [ ] Setup instructions documented

### CRD-C: Pipeline Orchestration

**Parent PRD**: Complete Value Train Infrastructure  

**User Story**: As an operator, I need automated phase advancement so that completed work flows smoothly to the next stage.  

**Labels**: CRD, phase:enablement, agent:conductor, next  

**Acceptance Criteria**:
- [ ] Conductor workflow automates phase transitions
- [ ] Pipeline location corrected
- [ ] GitHub templates completed
- [ ] Error handling implemented
- [ ] Operator notifications configured

### CRD-D: Auto-Pilot Implementation

**Parent PRD**: Complete Value Train Infrastructure  

**User Story**: As an operator, I can trigger Auto-Pilot to work through a queue of issues so that routine tasks complete without manual intervention.  

**Labels**: CRD, phase:enablement, agent:conductor, future  

**Acceptance Criteria**:
- [ ] Issue selection algorithm implemented
- [ ] Ticket folder structure created
- [ ] /drive command functional
- [ ] Integration tests passing
- [ ] Documentation complete

### CRD-E: Documentation and Risk Management

**Parent PRD**: Complete Value Train Infrastructure  

**User Story**: As an operator, I need comprehensive documentation and risk tracking so that we can operate safely and efficiently.  

**Labels**: CRD, phase:enablement, agent:conductor, future  

**Acceptance Criteria**:
- [ ] Architecture documentation created
- [ ] ADR-0010 written
- [ ] Risk templates implemented
- [ ] Risk automation configured
- [ ] All documentation linked

### CRD-F: Testing and Completion Workflows

**Parent PRD**: Complete Value Train Infrastructure  

**User Story**: As an operator, I need comprehensive testing protocols and completion workflows so that we can validate system functionality and properly transition between project phases.  

**Labels**: CRD, phase:enablement, agent:evaluator, future  

**Acceptance Criteria**:
- [ ] Smoke testing protocol implemented
- [ ] Command format standardized to JSON
- [ ] Legacy cleanup procedures defined
- [ ] End-to-end validation passes
- [ ] Completion workflows documented

## Detailed Implementation Tasks

Each task below will be created as a separate GitHub issue with proper parent CRD reference.

### Tasks for CRD-A: Developer Build Automation

#### Task A.1: Create Makefile

**Parent CRD**: CRD-A (Developer Build Automation)  

**Labels**: Task, phase:enablement, agent:ops, next

**Why**: Standardizes development environment setup and common operations. Currently, developers must remember multiple commands and setup steps.

**How**:
```makefile
# Key targets needed:
venv:          # Create virtual environment
install:       # Install dependencies
lint:          # Run flake8, black, isort
test:          # Run pytest suite
ci:            # Run full CI pipeline locally
clean:         # Remove artifacts
```

**Dependencies**:
- requirements.txt (exists)
- Python 3.8+ (exists)

**Implementation Details**:
1. Create `/Makefile` in repository root
2. Define standard targets following GNU Make conventions
3. Integrate with existing Python scripts
4. Document usage in README

**Acceptance Criteria**:
- [ ] `make venv` creates virtual environment
- [ ] `make test` runs all tests
- [ ] `make lint` runs all linters
- [ ] `make ci` mirrors GitHub Actions

#### Task A.2: Update CI/CD with Linting

**Parent CRD**: CRD-A (Developer Build Automation)

**Labels**: Task, phase:enablement, agent:ops, next

**Why**: From planning-tasks.md - need consistent code formatting across all Python files.

**How**:
Update `.github/workflows/ci.yml` to include linting steps that match local development.

**Dependencies**:
- Makefile (Task A.1)
- Existing CI workflow

**Acceptance Criteria**:
- [ ] CI runs flake8, black, isort
- [ ] CI configuration matches Makefile
- [ ] All Python files pass linting

---

### Tasks for CRD-B: Quality Gate Automation

#### Task B.1: Implement Pre-commit Hooks

**Parent CRD**: CRD-B (Quality Gate Automation)

**Labels**: Task, phase:enablement, agent:ops, next

**Why**: Catches issues before they enter git history. The Value Train spec requires commit message validation and YAML header checks.

**How**:
1. Create `.pre-commit-config.yml`
2. Define hooks for:
   - Commit message format (`#complete phase:<id>`)
   - YAML header validation
   - File size limits (prevent large files)
   - Python linting

**Dependencies**:
- pre-commit package
- Existing validation scripts

**Implementation Details**:
```yaml
repos:
  - repo: local
    hooks:
      - id: commit-msg-format
        name: Validate commit message
        entry: scripts/validate_commit_msg.py
        language: python
        stages: [commit-msg]
      
      - id: yaml-headers
        name: Check YAML headers
        entry: scripts/check_yaml_headers.py
        language: python
        files: \.(md|yaml|yml)$
```

**Acceptance Criteria**:
- [ ] Invalid commit messages are rejected
- [ ] YAML headers validated on commit
- [ ] Large files blocked (>5MB)
- [ ] Instructions for setup in README

#### Task B.2: Implement Pre-push Hooks

**Parent CRD**: CRD-B (Quality Gate Automation)  

**Labels**: Task, phase:enablement, agent:ops, next

**Why**: Final quality gate before code reaches remote. Ensures tests pass and code is properly formatted.

**How**:
- Run `make test` before push
- Run `make lint` before push
- Validate branch naming convention

**Dependencies**:
- Makefile (Task 1.1)
- Test suite (exists)

---

### Tasks for CRD-C: Pipeline Orchestration

#### Task C.1: Create conductor.yml GitHub Action

**Parent CRD**: CRD-C (Pipeline Orchestration)  

**Labels**: Task, phase:enablement, agent:conductor, next

**Why**: Manual phase advancement is error-prone. Conductor should automatically progress the pipeline when work completes.

**How**:
```yaml
name: Conductor Update
on:
  push:
    branches: [main]
    paths:
      - 'tickets/**/checklist.md'
      - 'docs/session-context/ACTIVE_SESSION.md'

jobs:
  advance-phase:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
      - name: Run conductor update
        run: |
          python scripts/conductor_update.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Dependencies**:
- conductor_update.py (exists)
- GitHub bot token
- ACTIVE_SESSION.md structure

**Implementation Details**:
1. Create `.github/workflows/conductor.yml`
2. Configure bot permissions
3. Test phase advancement logic
4. Add error handling and notifications

**Acceptance Criteria**:
- [ ] Merges to main trigger conductor
- [ ] Phase advances when checklist complete
- [ ] Next phase branch/folder created
- [ ] Failures notify operators

#### Task C.2: Fix Pipeline Location

**Parent CRD**: CRD-C (Pipeline Orchestration)  

**Labels**: Task, phase:enablement, agent:conductor, next

**Why**: Spec expects `/pipelines/pipeline.yml` but file is at `/config/pipeline.yml`. This causes confusion and breaks assumptions.

**How**:
1. Create `/pipelines/` directory
2. Move `pipeline.yml` with git mv
3. Update all references in code
4. Add redirect/compatibility layer

**Dependencies**:
- Identify all code references
- Update documentation

**Implementation Details**:
```bash
mkdir -p pipelines
git mv config/pipeline.yml pipelines/pipeline.yml
# Update imports in Python scripts
# Update references in documentation
```

#### Task C.3: Create Pull Request Template

**Parent CRD**: CRD-C (Pipeline Orchestration)  

**Labels**: Task, phase:enablement, agent:conductor, next  

**Why**: Ensures PRs include required information and follow standards.

**How**:
Create `.github/PULL_REQUEST_TEMPLATE.md` with required fields.

**Dependencies**: None

**Acceptance Criteria**:
- [ ] Template auto-loads on PR creation
- [ ] Includes all required fields
- [ ] Clear instructions

#### Task C.4: Create Feature Issue Template

**Parent CRD**: CRD-C (Pipeline Orchestration)  

**Labels**: Task, phase:enablement, agent:conductor, next  

**Why**: Features need structured information for Value Train processing.

**How**:
Create `.github/ISSUE_TEMPLATE/feature.md` with phase, mode, and agent fields.

**Dependencies**: 
- Understanding of Value Train phases
- Issue label structure

**Acceptance Criteria**:
- [ ] Template includes all Value Train fields
- [ ] Auto-labels configured
- [ ] Template appears in issue chooser

---

### Tasks for CRD-D: Auto-Pilot Implementation

#### Task D.1: Implement Issue Selection Script

**Parent CRD**: CRD-D (Auto-Pilot Implementation)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Auto-Pilot needs deterministic issue selection. Currently missing `select_next_issue.py`.

**How**:
```python
# Core logic:
1. Query GitHub API for issues
2. Filter: labels=['Task', 'auto'], assignee=None
3. Sort by priority (now > next > future) then created_at
4. Return oldest high-priority issue or empty
```

**Dependencies**:
- GitHub API access
- PyGithub library

**Implementation Details**:
1. Create `scripts/select_next_issue.py`
2. Add comprehensive tests
3. Handle API rate limits
4. Support dry-run mode

**Acceptance Criteria**:
- [ ] Selects correct issue by priority
- [ ] Handles empty queue gracefully
- [ ] Includes logging
- [ ] Has full test coverage

#### Task D.2: Create Ticket Folder Structure

**Parent CRD**: CRD-D (Auto-Pilot Implementation)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Each phase needs isolated workspace to prevent conflicts. Ticket folders provide this isolation.

**How**:
- Create `tickets/<phase>_<id>/` on branch creation
- Include checklist.md, ACTIVE_SESSION.md, artifacts/
- Template initial content

**Dependencies**:
- Branch naming validation
- Template files
- ticket.yml schema definition (Task D.6)

**Implementation Details**:
```bash
tickets/
  train_142/
    checklist.md       # Mode-specific checklist
    ACTIVE_SESSION.md  # Session state
    ticket.yml        # Metadata
    artifacts/        # Output directory
```

#### Task D.3: Implement /drive Command

**Parent CRD**: CRD-D (Auto-Pilot Implementation)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Operators need simple way to start Auto-Pilot. The /drive command provides this interface.

**How**:
1. Create `.claude/commands/drive.json`
2. Implement command logic
3. Add to Claude command index

**Dependencies**:
- select_next_issue.py (Task 4.1)
- Ticket folder structure (Task 4.2)

#### Task D.4: Implement Session Context Migration to Ticket-Based Model

**Parent CRD**: CRD-D (Auto-Pilot Implementation)  

**Labels**: Task, phase:enablement, agent:conductor, future  

**Why**: Current centralized session context creates merge conflicts and prevents parallel agent operation. Need distributed, ticket-based context management.

**How**:
1. Extend `migrate_session.py` with ticket migration functions
2. Create ticket folder structure: `tickets/<phase>_<issue_id>/`
3. Migrate current `ACTIVE_SESSION.md` to ticket-specific contexts
4. Implement context aggregation for global state queries
5. Update all scripts to work with distributed contexts

**Dependencies**:
- Auto-Pilot ticket folder structure (Task D.2)
- GitHub issue integration
- Session management schema

**Implementation Details**:
```bash
tickets/
  enablement_142/
    ACTIVE_SESSION.md    # Ticket-specific session state
    checklist.md         # Mode checklist for this ticket
    ticket.yml          # Metadata and relationships
    artifacts/          # Ticket outputs
```

**Migration Strategy**:
- Gradual migration: Support both centralized and distributed during transition
- Backward compatibility: Keep centralized format during development
- Automated migration: Script migrates when Auto-Pilot activates

**Acceptance Criteria**:
- [ ] Migration script handles current ACTIVE_SESSION.md
- [ ] Ticket contexts isolated and conflict-free
- [ ] Global state aggregation works
- [ ] All existing scripts updated
- [ ] Backward compatibility maintained

#### Task D.5: Create Integration Tests for Auto-Pilot
**Parent CRD**: CRD-D (Auto-Pilot Implementation)  

**Labels**: Task, phase:enablement, agent:conductor, future  

**Why**: Individual scripts tested but full Auto-Pilot flow needs validation.

**How**:
- Test full Auto-Pilot flow with ticket contexts
- Test phase transitions and handoffs
- Test git hook integration
- Mock GitHub API calls
- Validate session context migration

**Dependencies**:
- All Auto-Pilot components
- Session migration (Task D.4)
- Test fixtures

**Acceptance Criteria**:
- [ ] End-to-end tests pass
- [ ] Mock API prevents rate limits
- [ ] All edge cases covered
- [ ] Session migration tested

#### Task D.6: Define ticket.yml Schema and Templates
**Parent CRD**: CRD-D (Auto-Pilot Implementation)  
**Labels**: Task, phase:enablement, agent:conductor, next
**Why**: ticket.yml requires comprehensive schema for metadata, evaluation tracking, and state management as defined in agenticops-value-train.md.

**How**:
1. Create `/templates/ticket.yml` template with full schema
2. Include sections for: metadata, project context, phase tracking, checklist definitions, artifacts, criteria, evaluation status
3. Create initialization script that populates ticket.yml from GitHub issue data
4. Document schema fields and their purposes

**Dependencies**:
- GitHub issue structure understanding
- agenticops-value-train.md schema specification

**Acceptance Criteria**:
- [ ] Complete ticket.yml schema template created
- [ ] Schema matches agenticops-value-train.md specification
- [ ] Template includes all required fields (metadata, evaluation, criteria)
- [ ] Documentation explains each schema field

#### Task D.7: Create ticket.yml Management Scripts
**Parent CRD**: CRD-D (Auto-Pilot Implementation)  
**Labels**: Task, phase:enablement, agent:conductor, future
**Why**: ticket.yml state must be kept in sync with work progress and ACTIVE_SESSION.md updates.

**How**:
1. Create `scripts/init_ticket.py` - initializes ticket.yml from GitHub issue
2. Create `scripts/update_ticket.py` - updates ticket.yml evaluation section
3. Create `scripts/sync_ticket_session.py` - syncs ticket.yml with ACTIVE_SESSION.md
4. Integrate with existing validation scripts (check_todo.py, check_artifacts.py)

**Dependencies**:
- ticket.yml schema (Task D.6)
- Existing validation scripts
- GitHub API integration

**Acceptance Criteria**:
- [ ] ticket.yml automatically initialized from GitHub issues
- [ ] Evaluation section updates as work progresses
- [ ] State kept in sync with ACTIVE_SESSION.md
- [ ] Integration with existing validation scripts

#### Task D.8: Integrate ticket.yml with Auto-Pilot Workflow
**Parent CRD**: CRD-D (Auto-Pilot Implementation)  
**Labels**: Task, phase:enablement, agent:conductor, future
**Why**: Auto-Pilot must read and update ticket.yml state to coordinate work and track progress.

**How**:
1. Update Auto-Pilot to initialize ticket.yml when creating ticket folders
2. Integrate ticket.yml updates into task execution workflow
3. Use ticket.yml evaluation section for completion validation
4. Update conductor_update.py to read ticket.yml for phase transitions

**Dependencies**:
- ticket.yml management scripts (Task D.7)
- Auto-Pilot implementation (Tasks D.1-D.3)
- Conductor workflow (Task C.1)

**Acceptance Criteria**:
- [ ] Auto-Pilot creates and maintains ticket.yml
- [ ] ticket.yml evaluation drives completion validation
- [ ] Phase transitions read ticket.yml state
- [ ] Full integration with conductor workflow

---

### Tasks for CRD-E: Documentation and Risk Management

#### Task E.1: Create Architecture Overview

**Parent CRD**: CRD-E (Documentation and Risk Management)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Teams need visual understanding of system architecture and agent interactions.

**How**:
Create `/docs/architecture/agenticops-overview.md` with:
1. System architecture diagram
2. Agent interaction flows
3. Data flow diagrams
4. Integration points

**Dependencies**:
- Diagramming tool (Mermaid/PlantUML)
- Architecture decisions

**Acceptance Criteria**:
- [ ] Clear system diagram
- [ ] Agent responsibilities mapped
- [ ] Integration points documented
- [ ] Mermaid diagrams render properly

#### Task E.2: Write ADR-0010

**Parent CRD**: CRD-E (Documentation and Risk Management)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Architecture Decision Records capture why we adopted Value Train.

**How**:
Create `/docs/architecture/decisions/ADR-0010-adopt-value-train.md`:
- Context and problem
- Decision drivers
- Considered options
- Decision outcome
- Consequences

**Dependencies**: ADR template

#### Task E.3: Create Risk Issue Templates
**Parent CRD**: CRD-E (Documentation and Risk Management)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Risks need structured capture for tracking and mitigation.

**How**:
1. Create `.github/ISSUE_TEMPLATE/risk.yml`
2. Create `.github/ISSUE_TEMPLATE/mitigation.yml`
3. Add to issue template chooser

**Dependencies**:
- GitHub issue template syntax
- Risk categories from risk-registry.md

**Implementation Details**:
- YAML-based templates
- Required fields for risk/mitigation
- Auto-labeling with 'risk' or 'mitigation'
- Link fields for relationships

**Acceptance Criteria**:
- [ ] Risk template includes all fields
- [ ] Mitigation links to risks
- [ ] Auto-labels work correctly
- [ ] Templates appear in issue chooser

#### Task E.4: Implement Risk Tracking Automation

**Parent CRD**: CRD-E (Documentation and Risk Management)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Manual risk status updates are missed. Automation ensures accuracy.

**How**:
- GitHub Action to update risk status
- Link PR merges to mitigation completion
- Generate risk report on schedule

**Dependencies**:
- GitHub Actions knowledge
- Risk label structure

#### Task E.5: Create Value Train README for Non-Technical Users

**Parent CRD**: CRD-E (Documentation and Risk Management)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Boot-up checklist requires `/docs/product/value-train-readme.md` for non-technical narrative.

**How**:
Create user-friendly documentation explaining Value Train concepts without technical details for business stakeholders and new team members.

**Dependencies**: 
- Product vision and strategy documents
- Value Train specification

**Acceptance Criteria**:
- [ ] Non-technical explanation of Value Train benefits
- [ ] Clear overview of agent roles and responsibilities
- [ ] Business value proposition and ROI explanation
- [ ] Getting started guide for stakeholders

---

### Tasks for CRD-F: Testing and Completion Workflows

#### Task F.1: Create Smoke Testing Protocol

**Parent CRD**: CRD-F (Testing and Completion Workflows)  

**Labels**: Task, phase:enablement, agent:evaluator, future

**Why**: Boot-up checklist requires comprehensive end-to-end validation protocol.

**How**:
1. Create smoke test suite that validates full Value Train workflow
2. Test `/begin` command functionality and status block rendering
3. Validate checklist interaction and commit workflows
4. Test CI blocking for incomplete checklists
5. Verify conductor automation for phase advancement

**Dependencies**:
- All infrastructure components implemented
- Integration tests (Task D.5)

**Acceptance Criteria**:
- [ ] End-to-end workflow test passes
- [ ] All mode commands render status blocks correctly
- [ ] CI properly blocks incomplete work
- [ ] Conductor advances phases automatically
- [ ] Documentation for running smoke tests

#### Task F.2: Convert Command Files to JSON Format  

**Parent CRD**: CRD-F (Testing and Completion Workflows)  

**Labels**: Task, phase:enablement, agent:conductor, next

**Why**: Boot-up checklist expects `.claude/commands/*.json` but current implementation uses `.md` files.

**How**:
1. Convert all existing `.claude/commands/*.md` files to `.json` format
2. Ensure JSON includes fields: `description`, `mode`, `allowed-tools`
3. Update command index and documentation
4. Test all converted commands work correctly

**Dependencies**:
- Current command documentation
- Claude Code JSON command format specification

**Acceptance Criteria**:
- [ ] All commands converted to JSON format
- [ ] JSON includes required fields
- [ ] Commands function correctly after conversion
- [ ] Documentation updated

#### Task F.3: Implement Legacy Cleanup and Handoff Procedures

**Parent CRD**: CRD-F (Testing and Completion Workflows)  

**Labels**: Task, phase:enablement, agent:conductor, future

**Why**: Boot-up checklist requires procedures for legacy file cleanup and project handoff.

**How**:
1. Create script to move legacy context files to `docs/session-context/_legacy/`
2. Define issue transition protocols for project completion
3. Create completion workflow documentation
4. Implement automated cleanup triggers

**Dependencies**:
- Session context migration (Task D.4)
- Conductor workflow (Task C.1)

**Acceptance Criteria**:
- [ ] Legacy cleanup script implemented
- [ ] Issue transition protocols documented
- [ ] Completion workflow defined
- [ ] Cleanup integrated with conductor automation

---

### Task Group 8: Testing & Quality (CRD-002)

#### Task 8.1: Add Linting to CI
---

## Implementation Priorities

### Phase 1: Foundation (Week 1)

**Focus**: CRD-A (Developer Build Automation), CRD-B (Quality Gate Automation), high-priority CRD-F tasks, and ticket.yml foundation
- Task A.1: Create Makefile
- Task A.2: Update CI/CD with Linting
- Task B.1: Pre-commit hooks
- Task B.2: Pre-push hooks
- Task F.2: Convert Command Files to JSON Format
- Task D.6: Define ticket.yml Schema and Templates

**Rationale**: These provide immediate value and unblock other work. Command format conversion and ticket.yml schema are needed early for Auto-Pilot foundation.

### Phase 2: Automation (Week 2)

**Focus**: CRD-C (Pipeline Orchestration)
- Task C.1: Conductor workflow
- Task C.2: Fix pipeline location
- Task C.3: PR template
- Task C.4: Feature template

**Rationale**: Automates repetitive work and enforces standards.

### Phase 3: Auto-Pilot (Week 3)

**Focus**: CRD-D (Auto-Pilot Implementation)
- Task D.1: Issue selection
- Task D.2: Ticket folders
- Task D.3: /drive command
- Task D.4: Session context migration
- Task D.5: Integration tests
- Task D.7: ticket.yml management scripts
- Task D.8: ticket.yml Auto-Pilot integration

**Rationale**: Enables autonomous agent operation with comprehensive ticket state management.

### Phase 4: Documentation & Validation (Week 4)

**Focus**: CRD-E (Documentation and Risk Management) and CRD-F (Testing and Completion)
- Task E.1: Architecture docs
- Task E.2: ADR-0010
- Task E.3: Risk templates
- Task E.4: Risk automation
- Task E.5: Value Train README
- Task F.1: Smoke testing protocol
- Task F.3: Legacy cleanup procedures

**Rationale**: Captures knowledge, prevents failures, and ensures complete validation.

## Dependencies Graph

```
Makefile (A.1)
    ├── Pre-push hooks (B.2)
    └── Linting in CI (A.2)

Pre-commit hooks (B.1)
    └── [Independent]

Pipeline location (C.2)
    └── Conductor workflow (C.1)
        └── /drive command (D.3)

Issue selection (D.1)
    └── Ticket folders (D.2)
        └── /drive command (D.3)
            └── Integration tests (D.4)

Templates (C.3, C.4)
    └── [Independent]

Documentation (E.1, E.2)
    └── [Independent]

Risk templates (E.3)
    └── Risk automation (E.4)
```

## Risk Mitigation

### Risk: Breaking Existing Workflows

**Mitigation**: 
- Implement changes on feature branches
- Test thoroughly before merging
- Provide compatibility layers (e.g., pipeline.yml redirect)

### Risk: Team Adoption Challenges

**Mitigation**:
- Clear documentation for each change
- Gradual rollout with training
- Optional adoption initially

### Risk: Automation Failures

**Mitigation**:
- Comprehensive error handling
- Operator notifications
- Manual override capabilities
- Dry-run modes for testing

## Success Metrics

1. **Build Consistency**: 100% of builds use Makefile
2. **Quality Gates**: 0 commits bypass hooks after implementation
3. **Automation Rate**: >80% of phase transitions automated
4. **Risk Coverage**: 100% of identified risks have defined mitigations
5. **Test Coverage**: Maintain >90% coverage
6. **Documentation**: All features documented within 1 sprint

## Issue Creation Plan

### Step 1: Create New PRD
Create a new PRD issue titled "Complete Value Train Infrastructure" with:
- Parent reference to PRD #1
- Labels: `PRD`, `phase:enablement`, `next`
- Copy success criteria from this document

### Step 2: Create CRDs (5 issues)
Create each CRD as a separate issue with:
- Parent reference to the new PRD
- Proper agent assignment
- Priority labels (start with `next`, will change to `now` when work begins)
- Copy acceptance criteria from this document

### Step 3: Create Tasks (18 issues)
Create each task as a separate issue with:
- Parent reference to appropriate CRD
- Same labels as parent CRD
- Copy implementation details from this document
- Time estimates where applicable

### Step 4: Add to GitHub Project
For each created issue:
1. Add to project: `gh project item-add 3 --owner charleslbryant --url [issue-url]`
2. Set status to "Ready" for `next` priority items
3. Update project fields as needed

### Step 5: Update Existing Issues
- Add "meta" label to risk registry issues (#101-112, #201-219) per planning-tasks.md
- Update any conflicting priorities per one-piece-flow rules

## Summary

This plan addresses all gaps identified in the boot-up checklist and incorporates items from planning-tasks.md. The structured approach with proper PRD/CRD/Task hierarchy ensures:

1. **Clear ownership**: Each CRD has an assigned agent
2. **Manageable scope**: Tasks are completable in single sessions
3. **Proper dependencies**: Work flows in logical order
4. **Measurable progress**: Acceptance criteria for every level

Total new issues to create:
- 1 PRD
- 6 CRDs  
- 26 Tasks
- Total: 33 new issues

## Next Steps

1. Review this plan with the team for feedback and approval
2. Create the PRD issue first
3. Create CRDs referencing the PRD
4. Create tasks referencing their parent CRDs
5. Add all issues to the GitHub project with proper status
6. Begin implementation with Phase 1 tasks

## References

- [Value Train Specification](docs/agenticops-value-train.md)
- [Boot-up Checklist](docs/boot-up.md)
- [Risk Registry](docs/risk-registry.md)
- [Planning Tasks](docs/planning-tasks.md)
- [Task Management Rules](docs/rules/task-management.md)
- [GitHub Project](https://github.com/users/charleslbryant/projects/3)