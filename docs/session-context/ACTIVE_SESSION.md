# Active Session Context

## Session Metadata
```yaml
session_id: "2025-01-18-140000"
started_at: "2025-01-18 14:00:00"
last_updated: "2025-01-18 14:45:00"
operator: "charleslbryant"
assistant: "Claude Code"
```

## Current Work
```yaml
mode: "build"  # intake|discover|scope|design|build|evaluate|deliver|operate|improve
phase: "enablement"  # From pipeline.yml phases
agent: "conductor"  # conductor|onboarder|lab|studio|ops|evaluator|improver
task:
  issue_number: 4
  title: "Create mode checklist files"
  url: "https://github.com/charleslbryant/agenticops-value-train/issues/4"
  priority: "now"
  status: "In progress"
branch: "feature/issue-4-mode-checklists"
```

## Task Context
```yaml
parent_crd:
  issue_number: null
  title: null
  url: null
parent_prd:
  issue_number: 1
  title: "AgenticOps Value Train Implementation"
  url: "https://github.com/charleslbryant/agenticops-value-train/issues/1"
project:
  id: 3
  name: "AgenticOps Value Train"
  url: "https://github.com/users/charleslbryant/projects/3"
```

## Work Progress
```yaml
todos:
  - content: "Create /config/pipeline.yml with phases, modes, owners, artifacts"
    status: "completed"
    priority: "high"
    id: "1"
  - content: "Create /docs/rules/asset-registry.yaml with skills, tools, MCPs, A2A"
    status: "completed"
    priority: "high"
    id: "2"
  - content: "Create /docs/templates/mode-header.md template"
    status: "completed"
    priority: "high"
    id: "3"
  - content: "Create /docs/session-context/ACTIVE_SESSION.md YAML schema stub"
    status: "completed"
    priority: "high"
    id: "4"
  - content: "Commit and push all skeleton files"
    status: "completed"
    priority: "high"
    id: "5"
  - content: "Reorganize files to proper locations (config/, docs/templates/)"
    status: "completed"
    priority: "medium"
    id: "6"
```

## Artifacts
```yaml
created_files:
  - "/home/cbryant/projects/agenticops/config/pipeline.yml"
  - "/home/cbryant/projects/agenticops/docs/rules/asset-registry.yaml"
  - "/home/cbryant/projects/agenticops/docs/templates/mode-header.md"
  - "/home/cbryant/projects/agenticops/docs/session-context/ACTIVE_SESSION.md"
modified_files:
  - "/home/cbryant/projects/agenticops/docs/session-context/ACTIVE_SESSION.md"
dependencies: []
```

## Session Notes
```yaml
decisions:
  - "Created comprehensive pipeline configuration with all 18 phases"
  - "Defined asset registry with 10 skills, 10 tools, 5 MCPs, 8 A2A interfaces"
  - "Structured mode header template for consistent session management"
  - "Organized files into config/ and docs/templates/ directories"
  - "Completed Task #3 - repo skeleton infrastructure"
blockers: []
next_steps:
  - "Update GitHub issue #3 status to Done"
  - "Remove priority label from completed task"
  - "Identify next task from backlog"
handoff_requirements: []
```

## Git Context
```yaml
repository: "agenticops-value-train"
current_branch: "main"
working_directory: "/home/cbryant/projects/agenticops"
uncommitted_changes: true
last_commit: "eb38277"
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