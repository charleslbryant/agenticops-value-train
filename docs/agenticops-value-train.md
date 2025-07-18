# AgenticOps Value Train™ an AI-Driven Value Delivery System

This document defines the standard roles, responsibilities, and artifacts for each Agent involved in delivering AI projects in the AgenticOps Value Train™. These agents operate as modular expert units across the AI project value stream and ML pipeline.

## Pre-Engagement

### Pipeline

| Phase                 | Agent     | Description                                       | Goal                                                       | Outcome                                        | Artifacts               |
|-----------------------|-----------|---------------------------------------------------|------------------------------------------------------------|------------------------------------------------|-------------------------|
| Opportunity Triage    | Onboarder | Qualify and assess AI opportunity                 | Determine fit for AI and strategic value                   | Internal Go/No-Go + Rough Opportunity Doc      | Opportunity Brief       |
| Discovery & Framing   | Onboarder | Elicit context, define use case, align objectives | Understand user need, business case, technical feasibility | Use Case Brief + Problem Statement             | Use Case One-Pager      |
| Client Readiness      | Onboarder | Assess data, systems, team, and constraints       | De-risk delivery and surface blockers early                | AI Readiness Score + Risk Profile              | Readiness Questionnaire |
| Scope & Pitch         | Onboarder | Define MVP scope, pricing, and delivery plan      | Land the right-sized engagement with clear value           | MVP Plan + Pricing + SOW + Pitch Deck          | SOW, Pitch Deck         |
| Pre-Kickoff Logistics | Onboarder | Confirm legal, technical, and team alignment      | Eliminate blockers before Day 1                            | Signed SOW + DPA + Access Checklist + Contacts | Access Checklist, DPA   |

### Checklist

| Step                            | Agent     | Asset                                 |
|---------------------------------|-----------|---------------------------------------|
| Log opportunity in CRM / Notion | Conductor | CRM Tool                              |
| Fill in Opportunity Brief       | Onboarder | Notion / Docs / Template              |
| Schedule discovery workshop     | Onboarder | Calendar + MCP Scheduler              |
| Send AI Readiness Form          | Onboarder | Docs / Forms / Email                  |
| Request sample data             | Onboarder | Secure Share (S3 / Azure / GDrive)    |
| Run Data Profiler               | Lab       | Python / C\# Notebook                 |
| Draft SOW and Budget            | Onboarder | Docs + Budget Calculator              |
| Build pitch deck                | Onboarder | Slides / Pitch.com / Canva            |
| Send DPA and checklist          | Onboarder | Docs / HelloSign / Email              |
| Finalize contacts               | Onboarder | Shared Sheet / CRM / Contract Tracker |

### Artifacts

| Type      | Title                          | File Path                                         | Purpose                                                     |
|-----------|--------------------------------|---------------------------------------------------|-------------------------------------------------------------|
| Framing   | Opportunity Brief              | /preengagement/framing/opportunity-brief.md       | Summarize problem, urgency, and AI fit                      |
| Framing   | Use Case One-Pager             | /preengagement/framing/use-case-one-pager.md      | Confirm understanding and alignment                         |
| Discovery | AI Readiness Questionnaire     | /preengagement/discovery/ai-readiness.md          | Surface capability gaps and risks                           |
| Discovery | Data Profile Template          | /preengagement/discovery/data-profiler.ipynb      | Summarize data coverage, nulls, types, quality              |
| Legal     | DPA Template                   | /preengagement/legal/dpa-template.docx            | Enable data sharing safely                                  |
| Planning  | SOW Template                   | /preengagement/planning/sow-template.md           | Define scope, timeline, pricing, and success metrics        |
| Planning  | Access Checklist               | /preengagement/planning/credentials-checklist.md  | Ensure no technical blockers at start                       |
| Planning  | Project Contact Sheet          | /preengagement/planning/contact-sheet.md          | List client and vendor team leads and SMEs                  |
| Planning  | Glossary of Terms              | /preengagement/planning/glossary.md               | Ensure common vocabulary across business and tech           |
| Pitch     | Pitch Deck                     | /preengagement/pitch/pitch-deck-template.pptx     | Win buy-in with value story and delivery plan               |
| Planning  | Reference Architecture Diagram | /preengagement/planning/architecture-diagram.pptx | Visualize how the AI system integrates into the environment |
| Comm      | Client Alignment Email         | /preengagement/communication/client-email.txt     | Confirm plan, docs, and roles before kickoff                |
| Comm      | Internal Kickoff Email         | /preengagement/communication/internal-email.txt   | Clarify scope and agent assignments internally              |

## Delivery

### Pipeline

| Phase                | Agent(s)             | Description                                                  | Goal                                    | Outcome                        | Artifacts                     |
|----------------------|----------------------|--------------------------------------------------------------|-----------------------------------------|--------------------------------|-------------------------------|
| Data Sources         | Onboarder + Lab      | Identify data assets and export strategies                   | Create clean extractable dataset        | Source schema and access       | Source map, data access plan  |
| Extraction           | Lab                  | Pull, clean, standardize raw input into structured form      | Consistent structure across sources     | Extracted and normalized files | Extraction script, log        |
| Preparation          | Lab + Studio         | Handle missing values, partition sets, validate input schema | Create model-ready training dataset     | Clean, split data artifacts    | Prepared dataset, schema spec |
| Exploration          | Lab                  | Profile features, classes, distribution, anomalies           | Identify promising variables and gaps   | Data profile report            | Profile notebook              |
| Feature Engineering  | Lab + Studio         | Generate derived features from SIGs, quantities, etc.        | Model-input features                    | Feature map and derivation     | Feature config, map           |
| Model Architecture   | Studio               | Choose modeling approach, design interfaces                  | AI system plan                          | Model flow design              | Model flow diagram            |
| Training             | Lab                  | Train models, log experiments, tune hyperparameters          | Model with target metric                | Training notebook and logs     | Training notebook, MLflow     |
| Validation           | Evaluator            | Evaluate model performance against business-aligned metrics  | Ensure quality and success acceptance   | Evaluation metrics and summary | Evaluation report             |
| Deployment           | Studio + Ops         | Deploy model as batch/API, tag infra, configure rollback     | Functional, secure, and scalable system | Live model endpoint            | Deployment config             |
| Monitoring           | Evaluator + Ops      | Track performance, usage, cost, drift                        | Detect issues early                     | Live metrics and drift logs    | Monitoring dashboard          |
| Evaluation           | Evaluator            | Compare to baselines, SME feedback, business value           | Show ROI and user alignment             | Stakeholder validation         | Champion challenger log       |
| Performance Analysis | Evaluator + Improver | Analyze failure patterns, edge cases, mispredictions         | Prioritize improvements                 | Root cause notes               | Error log, review doc         |
| Improvement          | Improver             | Refine features, annotations, interfaces                     | Higher accuracy and less friction       | Recommendations and roadmap    | Improvement roadmap           |
| Retraining Loop      | Improver + Lab       | Trigger retraining, run new versions, log improvements       | Sustainable model performance           | Updated model and baseline     | Retraining notebook           |

### Checklist

| Step                        | Agent(s)             | Asset                                 |
|-----------------------------|----------------------|---------------------------------------|
| Define source systems       | Onboarder + Lab      | Business framing, Source Map          |
| Pull and clean data         | Lab                  | Extraction tool, data profiler        |
| Split and validate dataset  | Lab + Studio         | C\# / Python notebook, schema checker |
| Run profiling notebook      | Lab                  | Data profiler notebook                |
| Engineer features           | Lab + Studio         | Feature map, SIG logic                |
| Define model architecture   | Studio               | Architecture design, DAG flow tool    |
| Train model and log run     | Lab                  | MLflow, training notebook             |
| Evaluate results            | Evaluator            | Evaluation metrics, benchmark report  |
| Package and deploy model    | Studio + Ops         | CI/CD, TorchScript, AWS deployment    |
| Set up monitoring alerts    | Ops + Evaluator      | CloudWatch, Eval-Perf-Watcher         |
| Review stakeholder feedback | Evaluator            | Business framing, results summary     |
| Analyze edge cases          | Evaluator + Improver | Root cause analysis                   |
| Recommend improvements      | Improver             | Post-mortem, improvement roadmap      |
| Retrain updated model       | Improver + Lab       | Retraining plan, baseline comparison  |

### Artifacts

| Type     | Title                   | File Path                             | Purpose                                  |
|----------|-------------------------|---------------------------------------|------------------------------------------|
| Data     | Source Map              | /delivery/data/source-map.md          | Document systems and fields              |
| Data     | Extraction Script       | /delivery/data/extract.py             | Reproducible ETL process                 |
| Data     | Prepared Dataset        | /delivery/data/prepared.csv           | Cleaned data used for training           |
| Analysis | Profile Report          | /delivery/exploration/profile.ipynb   | Data profile results and visualizations  |
| Features | Feature Map             | /delivery/features/feature-map.md     | Inputs used in model pipeline            |
| Model    | Model Flow Diagram      | /delivery/model/architecture.pptx     | Illustrate pipeline architecture         |
| Model    | Training Notebook       | /delivery/model/train.ipynb           | Tracks model development                 |
| Model    | Evaluation Report       | /delivery/validation/eval-results.pdf | Summarizes model performance and metrics |
| Deploy   | Deployment Config       | /delivery/deploy/deploy.yaml          | Infra as code definition                 |
| Monitor  | Monitoring Dashboard    | /delivery/monitor/dashboard-link.txt  | Live performance visualizations          |
| Review   | Champion Challenger Log | /delivery/evaluation/champion-log.md  | Track comparison of model versions       |
| Ops      | Error Log               | /delivery/performance/error-log.json  | Document failures for analysis           |
| Roadmap  | Improvement Roadmap     | /delivery/improvement/roadmap.md      | Guide to next improvements               |
| Retrain  | Retraining Notebook     | /delivery/retrain/retrain.ipynb       | Tracks next round of model tuning        |

## Agents

### Conductor

-   Leads the value train from planning to delivery
-   Coordinates handoffs, ensures business alignment
-   Resolves cross-agent blockers

### Onboarder

-   Owns pre-engagement success
-   Aligns client expectations, deliverables, and readiness

### Lab

-   Handles data profiling, extraction, cleaning, and initial modeling
-   Iterates with Improver for retraining and feature updates

### Studio

-   Designs models, architecture, and inference systems
-   Collaborates with Lab + Ops to productionize logic

### Ops

-   Provisions cloud resources, manages IAM, cost tagging, monitoring
-   Ensures deployment is secure, auditable, and reversible

### Evaluator

-   Defines and validates model quality
-   Tracks success metrics over time and triggers retraining reviews

### Improver

-   Optimizes features, feedback loops, retraining cadence
-   Converts feedback and errors into better performance

## Assets

Skills, tools, MCPs, and A2A available to agents.

| Type  | Name                  | Description                                    | Available To         |
|-------|-----------------------|------------------------------------------------|----------------------|
| Tool  | Data Profiler         | Jupyter or C\# notebook for EDA                | Lab                  |
| Tool  | MLflow Tracker        | Logs and visualizes experiment results         | Lab, Evaluator       |
| Tool  | Deployment Pipeline   | CI/CD system for model packaging               | Studio, Ops          |
| Skill | Architecture Design   | Ability to map inputs → model → outputs        | Studio, Conductor    |
| Skill | Business Framing      | Translate client needs into scoped delivery    | Onboarder, Conductor |
| MCP   | GPT-Prompting v1      | Structured prompt set for interviews/workshops | All agents           |
| A2A   | Conductor-Task-Router | Assigns, sequences, and re-tries agent tasks   | Conductor            |
| A2A   | Eval-Perf-Watcher     | Periodic model accuracy and drift monitor      | Evaluator, Improver  |

### Skill

A capability or domain of expertise that an agent can apply to perform reasoning, decision-making, or execution within its scope.

-   Often taught via examples, documentation, or demonstrations.
-   May be specific (e.g., “label schema design”) or abstract (e.g., “business framing”).
-   Can be possessed by both human agents and AI agents.
-   Normally scoped to functionality implemented inside of the agentic system.
-   Usually implemented with system prompts for LLM based AI agents.

### Tool

A tangible asset or software utility that an agent uses to complete a task.

-   Examples: notebooks, CI/CD pipelines, code libraries, dashboards.
-   Tools have affordances and outputs that shape how agents operate.
-   May require configuration, permissions, or integrations.
-   Normally scoped to functionality implemented outside of an agentic system.
-   Usually implemented as discrete functions callable by an LLM based AI agent.

### MCP (Model Context Protocol)

A structured prompt set or communication format that governs how models are instructed, queried, or guided across phases.

-   Ensures consistency across agent interactions with LLMs.
-   Think of it as an API contract between agents and models.

### A2A (Agent-to-Agent)

A system-level interaction, interface, or automation that enables coordination or information flow between agents.

-   Includes handoffs, alerts, task routing, retry policies, or chat interfaces.
-   Can be human-mediated or machine-driven (e.g., orchestrated by the Conductor).

## Workshop

| Phase               | Goal                                         |
|---------------------|----------------------------------------------|
| Opportunity Triage  | Determine if this is a real AI opportunity   |
| Discovery & Framing | Define the use case and success metrics      |
| Client Readiness    | Identify blockers and readiness gaps         |
| Data Sources        | Locate and understand data systems           |
| Feature Engineering | Clarify business logic for features          |
| Evaluation          | Confirm how value and quality will be judged |

### Question Prompts

#### Use Case & Impact

-   What problem are we solving?
-   What happens when this problem isn’t solved?
-   Who feels the pain, and how often?
-   How are you solving it today?
-   What would a successful solution unlock?

#### Business Alignment

-   What’s the measurable business value of solving this?
-   What metric would make this project a success?
-   Who ultimately approves or evaluates the result?
-   Are there organizational initiatives this aligns with?

#### Data & Feasibility

-   What systems store the relevant data?
-   How is the data structured? How complete?
-   Is the data labeled, annotated, or pre-processed?
-   How far back does the data go?
-   Who controls or owns this data internally?

#### Delivery Constraints

-   Is there a specific deadline or external driver?
-   What systems will this need to integrate with?
-   Is there a budget constraint for this initiative?
-   Are there technical or regulatory constraints?

#### Stakeholders & Decision-Makers

-   Who will use the output or predictions?
-   Who is responsible for approving the results?
-   Who can label data or validate outcomes?
-   Who is the internal technical POC?

#### Risk & Failure Handling

-   What are the risks if the model is wrong?
-   How do you currently handle mistakes in this process?
-   Are there legal or operational boundaries we should be aware of?

### Usage Instructions

Agents can:

-   Pull relevant sections for 1:1 or group interviews
-   Use prompt sets in workshops or GPT-guided discovery
-   Turn completed answers into Opportunity Briefs, Risk Registers, and Use Case Docs

For each session:

-   Document the agent name, date, participants
-   Save responses as markdown or form JSON for system ingestion
-   Push summaries into CRM, Notion, or project tracker

## Modes

### What a “Mode”

A Mode is a bounded operating context with its own:

-   Front-matter
    -   Description header
    -   Allowed tool list
-   Status
-   Checklist
-   Rules
-   Exit criteria
-   Transitions

A Mode is *not* the same as a pipeline phase; it is a controlled working state an agent enters to complete a focused slice of work.

### Proposed Mode Set

| Mode Command | Agents               | Purpose                                                                         |
|--------------|----------------------|---------------------------------------------------------------------------------|
| `/intake`    | Onboarder            | Qualify lead, capture opportunity brief, decide Go/No-Go                        |
| `/discover`  | Onboarder            | Workshops, data samples, risk and readiness scoring                             |
| `/scope`     | Onboarder, Conductor | Produce MVP plan, SOW, pricing, pitch                                           |
| `/design`    | Studio, Lab          | Architect data flow, feature plan, model approach                               |
| `/build`     | Lab, Studio          | Extract data, engineer features, train models (TDD or TML “test-measure-learn”) |
| `/evaluate`  | Evaluator            | Formal validation against metrics and business KPIs                             |
| `/deliver`   | Studio, Ops          | Final tests, package artifacts, create PR or release                            |
| `/operate`   | Ops, Evaluator       | Watch live performance, drift, cost, error budgets                              |
| `/improve`   | Improver, Lab        | Root-cause analysis, retraining, roadmap updates                                |

Each mode inherits a common shell but has its own checklist and transition map.

### Mode Template

```Code Language
---
description: <one-sentence purpose>
allowed-tools: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), Bash(test:*)
---
# <Mode Name> Agent

Always start responses with:
🤖 [<Mode Name>]

Initial status block:
🤖 [<Mode Name>]
Status
Git status: !git status 
Current branch: !git branch --show-current 
Open PRs: !gh pr list --head $(git branch --show-current)

### Checklist (TodoWrite)

0. Read rule and context files *
1. ...
n. Ready for mode switch *

### Rules
* @docs/rules/rulel-filename.ext
* @docs/rules/rule2-filename.ext

### Exit Requirements
* Itemised list

### Allowed Transitions
* `/other-mode`,`/another-mode`
```

### Mapping Modes to Pipeline Phases

| Pipeline Phase       | Active Mode         |
|----------------------|---------------------|
| Data Sources         | /discover, /design  |
| Extraction           | /build              |
| Preparation          | /build              |
| Exploration          | /build              |
| Feature Engineering  | /build              |
| Model Architecture   | /design             |
| Training             | /build              |
| Validation           | /evaluate           |
| Deployment           | /deliver            |
| Monitoring           | /operate            |
| Evaluation           | /operate, /evaluate |
| Performance Analysis | /improve            |
| Improvement          | /improve            |
| Retraining Loop      | /improve, /build    |

### Checklist Seeds for the Remaining Modes

-   /scope: Finalise SOW, budget, pitch deck; push artifacts; get Conductor approval.
-   /design: Write model flow diagram, feature spec, ADRs; review security implications.
-   /build: Red-green-refactor for code or train-measure-iterate for models; commit MLflow runs.
-   /evaluate: Run test suite and KPI checks; record champion–challenger comparison.
-   /deliver: Merge to main, tag release, update CURRENT_STATE and NEXT_TASKS.
-   /operate: Verify monitors live; update cost dashboards; produce weekly performance note.
-   /improve: Open issues for failure themes; draft improvement roadmap; farm new training data.

### Assets: Skills, Tools, MCP, A2A Registry

Add a simple YAML or markdown table (one per category) under `/docs/rules/asset-registry.md`. Agents reference it instead of hard-coding paths in every mode header.

Example skeleton:

```yaml
skills:
  architecture_design: Studio, Conductor
  data_profiling: Lab

tools:
  data_profiler: Lab
  mlflow_tracker: Lab, Evaluator
  deployment_pipeline: Studio, Ops

mcps:
  mcp_discovery_v1: All
  mcp_review_v2: Evaluator

a2a:
  conductor_task_router: Conductor
  eval_perf_watcher: Evaluator, Improver
```

### Next Steps

1.  Decide which of the nine proposed modes you truly need day one.
2.  Create `docs/rules/<mode>-checklist.md` files containing each checklist.
3.  Add header templates to the codebase so agents can copy-paste quickly.
4.  Register skills, tools, MCPs, and A2A assets in a single file for easy maintenance.

Once the skeleton is in place, every session follows the same rhythm across the whole AI life-cycle.
