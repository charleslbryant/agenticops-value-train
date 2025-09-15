# Active Session Context

## Session Metadata
```yaml
session_id: null
started_at: null
last_updated: "2025-01-15 10:00:00"
operator: "charleslbryant"
assistant: "Claude Code"
```

## Current Work
```yaml
mode: null  # intake|discover|scope|design|build|evaluate|deliver|operate|improve
phase: null  # From pipeline.yml phases
agent: null  # conductor|onboarder|lab|studio|ops|evaluator|improver
task:
  issue_number: null
  title: null
  url: null
  priority: null
  status: "Not started"
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
  name: null
  url: null
```

## Work Progress
```yaml
todos: []
```

## Artifacts
```yaml
created_files: []
modified_files: []
dependencies: []
```

## Session Notes
```yaml
decisions: []
blockers: []
next_steps: []
handoff_requirements: []
```

## Git Context
```yaml
repository: "agenticops-value-train"
current_branch: "main"
working_directory: "/home/charleslbryant/projects/agenticops-value-train"
uncommitted_changes: false
last_commit: null
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