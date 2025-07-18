# CMDS Mode System

CMDS uses a mode-based workflow system to ensure structured, context-aware development across assistants and contributors. Each mode has its own responsibilities, tools, and transition logic.

---

## 🚀 Available Modes

### `/kick` — Project Kickoff Mode (Template Customization)
Customizes CMDS templates for new projects with operator collaboration.
- **Checklist**: `kick`
- **Transitions**: `/begin`, `/plan`
- **Responsibilities**:
  - Inventory and review template files
  - Collaborate with operator to customize product vision and strategy
  - Update architecture documentation for project specifics
  - Remove template warnings and validate customizations
  - Prepare project for development workflow

---

### `/begin` — Session Startup Mode
Prepares environment and selects a task to work on.
- **Checklist**: `begin`
- **Transitions**: `/plan`, `/design`
- **Responsibilities**:
  - Load all rule and session context files
  - Select a single "now" task
  - Create feature branch
  - Write session state to `ACTIVE_SESSION.md`

---

### `/plan` — Task Planning Mode
Breaks down PRDs/CRDs into tasks and prioritizes them.
- **Checklist**: `plan`
- **Transitions**: `/design`, `/deliver`
- **Responsibilities**:
  - Read all rule and context files
  - Break down work into CRDs and tasks
  - Set priorities and labels
  - Update session context before exit

---

### `/design` — Design Mode (Architecture & Technical Design)
Creates technical designs and architecture decisions before implementation.
- **Checklist**: `design`
- **Transitions**: `/dev`, `/plan`
- **Responsibilities**:
  - Create feature design documents using templates
  - Document architectural decisions in ADRs
  - Define API contracts and data models
  - Review security and performance implications
  - Get design approval before development

---

### `/dev` — Development Mode (TDD)
Implements a single task using strict test-driven development.
- **Checklist**: `dev`
- **Transitions**: `/design`, `/deliver`
- **Responsibilities**:
  - Follow red-green-refactor cycle
  - Commit code with proper attribution
  - Update context and documentation
  - Prepare for PR and handoff

---

### `/deliver` — Delivery Mode
Prepares work for review, creates PRs, and finalizes documentation.
- **Checklist**: `deliver`
- **Transitions**: `/begin`, `/dev`, `/qa`
- **Responsibilities**:
  - Final testing and documentation
  - PR creation and Git workflow
  - Session wrap-up and state update

---

### `/qa` — QA Mode
Verifies feature functionality, tests, and documentation.
- **Checklist**: `qa`
- **Transitions**: `/begin`, `/dev`
- **Responsibilities**:
  - Confirm all acceptance criteria and documentation are met
  - Validate PR merged and system state is clean
  - Raise issues for any gaps or defects

---

## 🔁 Mode Transition Overview
| From Mode | Can Transition To         |
|-----------|---------------------------|
| `/kick`   | `/begin`, `/plan`         |
| `/begin`  | `/plan`, `/design`        |
| `/plan`   | `/design`, `/deliver`     |
| `/design` | `/dev`, `/plan`           |
| `/dev`    | `/design`, `/deliver`     |
| `/deliver`| `/begin`, `/dev`, `/qa`   |
| `/qa`     | `/begin`, `/dev`          |

---

## 🔄 Workflow Integration

### New Project Setup
1. **`/kick`** → Customize templates for your project
2. **`/begin`** → Start first development session

### Standard Development Flow
1. **`/begin`** → Load context and select task
2. **`/plan`** → Break down work (if needed)
3. **`/design`** → Create technical design
4. **`/dev`** → Implement with TDD
5. **`/deliver`** → Create PR and ship
6. **`/qa`** → Validate and prepare next session

### When to Use Each Mode

**`/kick`**: 
- New projects requiring template customization
- Setting up CMDS for your specific domain/technology

**`/begin`**: 
- Start of every development session
- When returning after breaks or handoffs

**`/plan`**: 
- Large features needing breakdown
- Unclear requirements needing analysis

**`/design`**: 
- Non-trivial features requiring architecture decisions
- New APIs or significant data model changes
- Integration between multiple systems

**`/dev`**: 
- Implementation of designed features
- Bug fixes with clear scope

**`/deliver`**: 
- Feature completion and PR creation
- Documentation updates

**`/qa`**: 
- End-to-end validation
- Acceptance testing

---

## 🧠 Mode Context Files
Each mode starts by re-reading the following:
- Rule files (specific to mode)
- Product and architecture context
- Session files:
  - `CURRENT_STATE.md`
  - `NEXT_TASKS.md`
  - `ACTIVE_SESSION.md`

This ensures clean context boundaries between modes and reduces memory overload.

---

## ✅ Compliance Automation
- All modes use TodoWrite checklists
- Mode transitions require `/clear` to reset context
- Session state must be written before switching
- Rule reading is mandatory at each entry

---
*Generated from `modes/index.yaml`*