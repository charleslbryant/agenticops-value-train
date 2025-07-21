# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AgenticOps Value Train™ is an AI-driven value delivery system that implements a structured methodology for managing AI agent development workflows across the entire ML pipeline. The project provides a comprehensive framework for digital, data, IoT, and AI product development with phase-based workflows, agent orchestration, and continuous improvement cycles.

## Key Architecture Components

### Agent Roles

The Value Train defines specialized agents for different responsibilities:

- **Conductor** - Leads the value train from planning to delivery, coordinates handoffs, ensures business alignment
- **Onboarder** - Owns pre-engagement success, aligns client expectations, deliverables, and readiness
- **Lab** - Handles data profiling, extraction, cleaning, and initial modeling
- **Studio** - Designs models, architecture, and inference systems
- **Ops** - Provisions cloud resources, manages IAM, cost tagging, monitoring
- **Evaluator** - Defines and validates model quality, tracks success metrics
- **Improver** - Optimizes features, feedback loops, retraining cadence

### Pipeline Structure

The ML pipeline follows these stages:
```
Data Sources → Extraction → Preparation → Exploration → Feature Engineering
     ↓                                                            ↓
Monitoring ← Deployment ← Validation ← Training ← Model Architecture
     ↓                                      ↑                     ↑
Improvement → Evaluation → Performance Analysis → Retraining Loop
```

### Mode System

Modes are bounded operating contexts with specific tools, checklists, and transitions:

| Mode Command | Purpose |
|--------------|---------|
| `/intake`    | Qualify lead, capture opportunity brief, decide Go/No-Go |
| `/discover`  | Workshops, data samples, risk and readiness scoring |
| `/scope`     | Produce MVP plan, SOW, pricing, pitch |
| `/design`    | Architect data flow, feature plan, model approach |
| `/build`     | Extract data, engineer features, train models |
| `/evaluate`  | Formal validation against metrics and business KPIs |
| `/deliver`   | Final tests, package artifacts, create PR or release |
| `/operate`   | Watch live performance, drift, cost, error budgets |
| `/improve`   | Root-cause analysis, retraining, roadmap updates |

### Core Files (To Be Created)
- `/pipelines/pipeline.yml` - Phase definitions, modes, owners, artifacts
- `/docs/rules/asset-registry.yaml` - Skills, tools, MCPs, A2A configurations
- `/docs/session-context/ACTIVE_SESSION.md` - Current session state with YAML front-matter
- `/docs/rules/<mode>-checklist.md` - Mode-specific checklists with exit criteria
- `/templates/mode-header.md` - Template for mode front-matter
- `.claude/commands/*.json` - Configuration for each slash command

### Asset Types

- **Skills** - Capabilities or domain expertise (e.g., "Architecture Design", "Business Framing")
- **Tools** - Software utilities (e.g., Data Profiler, MLflow Tracker, Deployment Pipeline)
- **MCPs** - Model Context Protocols for structured AI interactions
- **A2A** - Agent-to-Agent interfaces for coordination and information flow

## Development Commands

### Python Scripts (To Be Created)
```bash
python scripts/check_todo.py        # Verify all checklist items are complete
python scripts/check_artifacts.py   # Validate artifact paths from pipeline.yml
python scripts/conductor_update.py  # Advance session to next phase
python scripts/migrate_session.py   # Migrate legacy context to new format
```

### Testing & Validation
```bash
make lint          # Run linting (to be configured)
make test          # Run test suite (to be configured)
```

### Git Hooks (To Be Configured)
- **pre-commit**: Lint commit messages for `#complete phase:<id>`, validate YAML headers
- **pre-push**: Run unit tests and linting

## Important Implementation Notes

1. **George Attribution**: All AI agents in the system are referred to as "George" for consistency

2. **Mode Workflow**:
   - Each mode has allowed tools specified in front-matter
   - Status blocks show git status, branch, and open PRs
   - Checklists must be completed before mode transitions
   - Exit criteria and allowed transitions are explicitly defined

3. **Checklist Enforcement**: CI/CD pipeline blocks merges if any checklist items remain unchecked

4. **Session Management**: The `ACTIVE_SESSION.md` file tracks current phase, mode, and progress with YAML front-matter

5. **Git Workflow**: 
   - Branch naming: `<phase>/<feature-description>`
   - Commit messages must include `#complete phase:<id>` tags
   - PRs require explicit issue closure with `Closes #<id>`

6. **Artifact Management**: 
   - All deliverables follow structured paths defined in pipeline.yml
   - Artifacts are organized by phase (e.g., `/preengagement/`, `/delivery/`)
   - Each artifact has defined purpose and format

7. **FinOps Considerations**:
   - Mandatory cost tags on all cloud resources
   - Budget alerts and monitoring
   - Unit economics tracking (cost per prediction)

## Current Project References

### Key Documentation
- `/docs/agenticops-value-train.md` - Complete agent roles, pipeline stages, and artifacts
- `/docs/ml-pipeline.md` - Detailed ML pipeline methodology with DiscoverTec case study
- `/docs/boot-up.md` - Master checklist for implementing the Value Train infrastructure
- `/docs/developer-guides/prompt-engineering.md` - AgenticOps prompt engineering methodology

### Planning Framework (AOPF)
The AgenticOps Planning Framework emphasizes:
1. Vision & Strategy Alignment (VSA)
2. Agentic Workflow Design (AWD)
3. Iterative Product Development & Sprints (IPDS)
4. Data-Driven Decision Making (3D)
5. Agentic Feedback & Continuous Improvement (AFCI)
6. Scalability & Integration (S&I)

## Current Status

The project is in initial setup phase. Reference `/docs/boot-up.md` for the complete implementation checklist. This contains George's Master Checklist for bootstrapping the AgenticOps Value Train infrastructure.

When implementing features:
1. Follow the phase progression defined in the pipeline
2. Complete all checklist items before phase transitions
3. Ensure artifacts are properly documented and stored
4. Maintain session context in `ACTIVE_SESSION.md`
5. Use the appropriate agent role for each task
6. Register all assets in the asset registry