# Value Train Pipeline Guide

The AgenticOps Value Train™ implements an intelligent pipeline that seamlessly handles three distinct work contexts: business strategy, ML engineering, and software engineering. The pipeline adapts dynamically based on context type while maintaining consistent quality gates and workflows across all domains.

## Pipeline Philosophy

**One Pipeline, Multiple Workflows**: Instead of separate pipelines for different work types, the Value Train uses intelligent routing and context-aware commands that adapt their behavior based on the task at hand. This creates consistency while enabling specialization.

**Agent-Centric Execution**: Seven specialized agents collaborate through the pipeline, each bringing domain expertise while following standardized handoff patterns and quality gates.

**Context-Driven Intelligence**: The pipeline automatically detects task type, project phase, and current context to provide the most relevant workflow and tools for each situation.

## Core Pipeline Architecture

### Universal Workflow Stages

Every task flows through these foundational stages, with specialized branching based on context:

1. **🚀 Initiation** - Project setup and session preparation
2. **📋 Planning** - Task breakdown and workflow routing  
3. **🎯 Execution** - Context-aware implementation with specialized branches
4. **📦 Integration** - Packaging, testing, and quality validation
5. **🔄 Operations** - Deployment, monitoring, and continuous improvement

### Intelligent Routing System

The pipeline automatically routes work based on **task labels** and **project context**:

```
📋 Task Planning
    ↓
🔍 Context Detection (Business | ML Engineering | Software Engineering)
    ↓
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   Business  │     ML      │  Software   │Operations   │
│   Strategy  │ Engineering │ Engineering │   Branch    │
└─────────────┴─────────────┴─────────────┴─────────────┘
    ↓             ↓             ↓             ↓
📦 Convergence: Universal Integration & Quality Gates
```

## Command Structure

### Core Universal Commands

These commands work across all task types with intelligent adaptations:

#### `/kick` - Project Initialization
- **Purpose**: Bootstrap new projects with type-appropriate templates
- **Intelligence**: Detects project type (ML, SaaS, infrastructure) and configures accordingly
- **Outputs**: Project structure, initial configuration, agent assignments

#### `/begin` - Session Startup  
- **Purpose**: Initialize work sessions with full context loading
- **Intelligence**: Reads project state, loads appropriate context files, prepares agent handoffs
- **Outputs**: Session context, current state summary, recommended next steps

#### `/plan` - Intelligent Task Planning
- **Purpose**: Break down work and route to appropriate execution paths
- **Intelligence**: Analyzes PRDs/CRDs, detects task types, creates specialized workflows
- **Outputs**: Task breakdown, workflow routing decisions, priority assignments

#### `/design` - Multi-Modal Architecture
- **Purpose**: Create technical designs adapted to domain (software, ML, infrastructure)
- **Intelligence**: Provides domain-specific design patterns and templates
- **Outputs**: Architecture documents, system designs, integration plans

#### `/deliver` - Universal Packaging
- **Purpose**: Package and deploy any type of deliverable
- **Intelligence**: Adapts packaging strategy based on artifact type (code, models, documents)
- **Outputs**: Deployable artifacts, documentation, handoff materials

#### `/qa` - Comprehensive Quality Validation
- **Purpose**: Validate deliverables against domain-specific quality standards
- **Intelligence**: Applies appropriate testing strategies (unit tests, model validation, business criteria)
- **Outputs**: Quality reports, validation results, improvement recommendations

### Core Engineering Commands

These commands form the foundation of all engineering workflows:

#### Requirements & Context Gathering
- `/intake` - Initial requirements gathering and context understanding
- `/discover` - Deep discovery of constraints, data, and feasibility  
- `/scope` - Define technical approach, timeline, and deliverables

*Note: These commands adapt their focus based on context:*
- **ML Engineering Context**: ML problem definition, data requirements, model performance criteria
- **Software Engineering Context**: Technical requirements, system constraints, implementation scope
- **Business Context**: Market opportunities, business goals, strategic positioning

#### Specialized Engineering Commands

##### ML Engineering Branch
- `/extract` - Data extraction, cleaning, and preparation
- `/features` - Feature engineering and dataset preparation
- `/train` - Model training, experimentation, and optimization
- `/evaluate` - Model validation against business metrics

##### Software Engineering Branch
- `/dev` - Test-driven development implementation
- `/test` - Specialized testing and validation workflows

##### Operations Branch
- `/operate` - Production monitoring and incident response
- `/improve` - Performance optimization and continuous improvement

## Agent Collaboration Patterns

### Agent Specializations

**🎭 Conductor** - Pipeline orchestration, phase transitions, cross-agent coordination
- **Primary Commands**: `/begin`, `/plan`, `/deliver`
- **Handoff Responsibility**: Routes work between specialized agents

**🎬 Onboarder** - Client engagement and business development
- **Primary Commands**: `/intake`, `/discover`, `/scope`
- **Handoff Responsibility**: Transitions qualified opportunities to technical teams

**🔬 Lab** - Data engineering and model experimentation  
- **Primary Commands**: `/extract`, `/features`, `/train`
- **Handoff Responsibility**: Provides prepared data and trained models to Studio

**🏗️ Studio** - Architecture design and system implementation
- **Primary Commands**: `/design`, `/dev`, `/deliver`
- **Handoff Responsibility**: Creates production-ready systems from Lab experiments

**⚙️ Ops** - Infrastructure and deployment management
- **Primary Commands**: `/deliver`, `/operate`
- **Handoff Responsibility**: Ensures reliable, scalable production deployment

**📊 Evaluator** - Quality assurance and performance validation
- **Primary Commands**: `/evaluate`, `/qa`
- **Handoff Responsibility**: Validates quality before production deployment

**📈 Improver** - Continuous optimization and enhancement
- **Primary Commands**: `/improve`, `/train`
- **Handoff Responsibility**: Identifies and implements performance improvements

### Handoff Protocols

**Context Preservation**: Each agent handoff includes complete context transfer via `ticket.yml` and session state
**Quality Gates**: Standardized acceptance criteria must be met before handoffs
**Rollback Capability**: Any handoff can be reversed if quality issues are discovered

## Workflow Examples

### ML Engineering Workflow

```
/kick → /begin → /plan → /intake → /discover → /scope → /design → /extract → /features → /train → /evaluate → /deliver → /operate → /improve
```

**Context-Specific Artifacts**:
- **Template Used**: ML Requirements Document (`/docs/templates/ml-requirements-document.md`)
- **Focus Areas**: Data requirements, model performance criteria, ML problem definition
- **Success Metrics**: Model accuracy, inference performance, business impact validation

**Execution Flow**:
1. **Onboarder** gathers ML requirements and context via `/intake` → produces ML Requirements Document
2. **Onboarder** conducts data discovery and feasibility via `/discover`  
3. **Onboarder + Conductor** define ML technical scope and approach via `/scope`
4. **Studio** designs ML architecture and model approach via `/design`
5. **Lab** extracts and prepares data via `/extract` → `/features`
6. **Lab** trains and optimizes models via `/train`
7. **Evaluator** validates model performance via `/evaluate`
8. **Studio + Ops** deploy ML systems to production via `/deliver`
9. **Ops + Evaluator** monitor model performance and data drift via `/operate`
10. **Improver** retrains models and optimizes based on feedback via `/improve`

### Software Engineering Workflow

```
/kick → /begin → /plan → /intake → /discover → /scope → /design → /dev → /qa → /deliver → /operate
```

**Context-Specific Artifacts**:
- **Template Used**: Requirements Document (`/docs/templates/requirements-document.md`)  
- **Focus Areas**: Functional requirements, system integration, API specifications
- **Success Metrics**: Code quality, test coverage, performance benchmarks, user acceptance

**Execution Flow**:
1. **Conductor** initializes development session via `/begin`
2. **Conductor** breaks down work into tasks via `/plan`
3. **Onboarder** gathers technical requirements via `/intake` → produces Requirements Document
4. **Onboarder** discovers constraints and integration points via `/discover`
5. **Onboarder + Conductor** define implementation scope via `/scope`
6. **Studio** creates technical design and architecture via `/design`
7. **Studio** implements features via `/dev` (TDD approach)
8. **Evaluator** validates implementation via `/qa`
9. **Studio + Ops** deploy to production via `/deliver`
10. **Ops** monitors production health and performance via `/operate`

### Business Development Workflow

```
/kick → /begin → /plan → /intake → /discover → /scope → /deliver
```

**Context-Specific Artifacts**:
- **Template Used**: Opportunity Brief (`/docs/templates/opportunity-brief.md`)
- **Focus Areas**: Market opportunity, strategic alignment, competitive analysis
- **Success Metrics**: ROI projections, market penetration, strategic value delivery

**Execution Flow**:
1. **Conductor** initializes business strategy session via `/begin`
2. **Conductor** plans strategic initiatives via `/plan`
3. **Onboarder** analyzes market opportunity and business goals via `/intake` → produces Opportunity Brief
4. **Onboarder** discovers market dynamics and competitive landscape via `/discover`
5. **Onboarder** defines business strategy and go-to-market approach via `/scope`
6. **Conductor** finalizes strategic deliverables via `/deliver`

## Quality Gates and Validation

### Universal Quality Standards

**Git Workflow**: All work uses feature branches with PR-based integration
**Documentation**: Every deliverable includes creating or updating appropriate documentation
**Testing**: Domain-appropriate testing strategies applied automatically
**Review Process**: Peer review requirements based on impact and complexity

### Domain-Specific Validation

**ML Models**: Evals, performance metrics, bias analysis, production readiness
**Software Features**: Unit tests, integration tests, security review
**Business Deliverables**: Stakeholder approval, legal review, compliance check
**Infrastructure**: Security scan, cost analysis, reliability testing

## Context Management

### Session State Tracking

**Distributed Context**: Each ticket maintains isolated context in `tickets/<phase>_<issue_id>/`
**Global Coordination**: Conductor maintains overall project state and agent assignments
**Version Control**: All context changes tracked via Git for complete audit trail

### Ticket Structure

```
tickets/<phase>_<issue_id>/
├── ACTIVE_SESSION.md    # Current session state and progress
├── checklist.md         # Mode-specific checklist with completion status
├── ticket.yml          # Metadata, evaluation criteria, relationships
└── artifacts/          # Generated outputs and deliverables
```

### Context Files

**ticket.yml Schema**:
- **Metadata**: ticket ID, title, description, timeline
- **Assignment**: operator, team, project, client information  
- **Workflow**: phase, stage, mode, status, dependencies
- **Validation**: entry/exit criteria, required artifacts
- **Evaluation**: completion status, quality metrics, notes

## Auto-Pilot Operation

### Autonomous Execution

**Issue Selection**: Automatically selects next priority task from GitHub issues
**Context Loading**: Loads appropriate session context and prepares workspace
**Workflow Execution**: Follows mode-specific checklists with agent collaboration
**Quality Validation**: Enforces completion criteria before advancing
**Handoff Management**: Coordinates smooth transitions between agents

### Human Oversight

**Strategic Decisions**: Major architectural or business decisions require human approval
**Quality Gates**: Critical quality checkpoints include human validation
**Exception Handling**: Complex failures escalate to human operators
**Customization**: Operators can modify workflows for specific project needs

## Integration Points

### External Systems

**GitHub**: Issue tracking, PR management, project coordination
**Cloud Platforms**: Azure/AWS integration for ML and infrastructure deployment
**Communication**: Slack/Teams integration for stakeholder updates
**Documentation**: Automated documentation generation and maintenance

### Tool Ecosystem

**MCP Integration**: Model Context Protocol provides standardized tool access
**Development Tools**: IDE integration, testing frameworks, deployment pipelines
**ML Tools**: MLflow, experiment tracking, model versioning
**Business Tools**: CRM integration, proposal generation, client communication

## Continuous Improvement

### Feedback Loops

**Performance Metrics**: Track completion time, quality scores, client satisfaction
**Agent Effectiveness**: Monitor individual agent performance and collaboration
**Workflow Optimization**: Identify bottlenecks and process improvements
**Tool Enhancement**: Upgrade tools and capabilities based on usage patterns

### Evolution Strategy

**Incremental Enhancement**: Continuous small improvements to existing workflows
**New Capability Addition**: Seamless integration of new tools and methodologies
**Agent Specialization**: Deeper domain expertise development over time
**Cross-Pollination**: Best practices sharing between different workflow branches

## Getting Started

### For New Projects

1. **Run `/kick`** to initialize project with appropriate templates
2. **Execute `/begin`** to load context and understand current state
3. **Use `/plan`** to break down initial work and establish workflow
4. **Follow recommended mode transitions** based on project type
5. **Leverage Auto-Pilot** for routine task execution with quality oversight

### For Existing Projects

1. **Run `/begin`** to load current project context
2. **Review session state** via `ACTIVE_SESSION.md` and ticket structure
3. **Check outstanding work** via GitHub issues and project boards
4. **Continue from current phase** using appropriate mode command
5. **Coordinate with other agents** via established handoff protocols

The Value Train Pipeline provides a sophisticated yet intuitive framework for managing complex, multi-disciplinary projects while maintaining high quality standards and enabling autonomous operation where appropriate. By intelligently adapting to task type and context, it eliminates the complexity of managing multiple separate workflows while preserving the specialized expertise required for different domains.