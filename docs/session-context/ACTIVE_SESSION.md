# Active Session Context

## Session Metadata
```yaml
session_id: "YYYY-MM-DD-HHMMSS"
started_at: "YYYY-MM-DD HH:MM:SS"
last_updated: "YYYY-MM-DD HH:MM:SS"
operator: "charleslbryant"
assistant: "Claude Code"
```

## Current Work
```yaml
mode: "build"  # intake|discover|scope|design|build|evaluate|deliver|operate|improve
phase: "enablement"  # From pipeline.yml phases
agent: "conductor"  # conductor|onboarder|lab|studio|ops|evaluator|improver
task:
  issue_number: 3
  title: "Implement repo skeleton infrastructure"
  url: "https://github.com/charleslbryant/agenticops-value-train/issues/3"
  priority: "now"
  status: "In progress"
branch: "feature/issue-3-repo-skeleton"
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
  - content: "Create /pipelines/pipeline.yml with phases, modes, owners, artifacts"
    status: "completed"
    priority: "high"
    id: "1"
  - content: "Create /docs/rules/asset-registry.yaml with skills, tools, MCPs, A2A"
    status: "completed"
    priority: "high"
    id: "2"
  - content: "Create /templates/mode-header.md template"
    status: "completed"
    priority: "high"
    id: "3"
  - content: "Create /docs/session-context/ACTIVE_SESSION.md YAML schema stub"
    status: "in_progress"
    priority: "high"
    id: "4"
  - content: "Commit and push all skeleton files"
    status: "pending"
    priority: "high"
    id: "5"
```

## Artifacts
```yaml
created_files:
  - "/home/cbryant/projects/agenticops/pipelines/pipeline.yml"
  - "/home/cbryant/projects/agenticops/docs/rules/asset-registry.yaml"
  - "/home/cbryant/projects/agenticops/templates/mode-header.md"
  - "/home/cbryant/projects/agenticops/docs/session-context/ACTIVE_SESSION.md"
modified_files: []
dependencies: []
```

## Session Notes
```yaml
decisions:
  - "Created comprehensive pipeline configuration with all 18 phases"
  - "Defined asset registry with 10 skills, 10 tools, 5 MCPs, 8 A2A interfaces"
  - "Structured mode header template for consistent session management"
blockers: []
next_steps:
  - "Complete session context YAML schema"
  - "Commit all skeleton files to repository"
  - "Update task status to completed"
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