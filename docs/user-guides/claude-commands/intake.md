# /intake Command - User Guide

The `/intake` command switches Claude into Intake Mode, where it acts as the **Onboarder Agent** to gather requirements and understand the context for work. This is typically the first step in any Value Train workflow.

## When to Use /intake

Use `/intake` when you need to:
- **Start a new project or feature** - Gather initial requirements and context
- **Clarify project scope** - Understand what needs to be built and why
- **Identify work context** - Determine if this is business, ML engineering, or software engineering work
- **Create structured requirements** - Generate proper requirement documents
- **Transition from planning** - Move from high-level ideas to concrete specifications

## What /intake Does

The `/intake` command:
1. **Switches Claude to Onboarder Agent mode** - Specialized in requirements gathering
2. **Loads relevant context files** - Reads project rules and current session state
3. **Detects work context** - Determines if this is business, ML, or software engineering work
4. **Guides requirements gathering** - Asks structured questions to understand needs
5. **Creates structured documents** - Generates appropriate requirement artifacts
6. **Validates completeness** - Ensures all necessary information is captured

## How Context Detection Works

The `/intake` command automatically adapts based on your work type:

### Business Context
**Triggers**: Strategic initiatives, market opportunities, business planning
- **Focus**: Market opportunity, competitive analysis, ROI projections
- **Questions**: Business goals, value proposition, stakeholder needs
- **Output**: **Opportunity Brief** with strategic analysis
- **Template**: `/docs/templates/opportunity-brief.md`

### ML Engineering Context  
**Triggers**: Data science projects, machine learning models, AI solutions
- **Focus**: Data requirements, model performance, ML problem definition
- **Questions**: Data sources, model metrics, training requirements
- **Output**: **ML Requirements Document** with technical ML specifications  
- **Template**: `/docs/templates/ml-requirements-document.md`

### Software Engineering Context
**Triggers**: Application development, system integration, technical features
- **Focus**: Functional requirements, APIs, system architecture
- **Questions**: User stories, technical constraints, integration needs
- **Output**: **Requirements Document** with software specifications
- **Template**: `/docs/templates/requirements-document.md`

## Using the /intake Command

### Basic Usage
Simply type `/intake` in your conversation with Claude:

```
/intake
```

Claude will switch to Intake Mode and begin the requirements gathering process.

### Command Response
When you run `/intake`, Claude will:

1. **Display Mode Header**: Shows that it's now in Intake Mode as the Onboarder Agent
2. **Show Current Status**: Displays active PRDs/CRDs, current branch, and session context
3. **Create TodoWrite Checklist**: Lists all required activities for intake mode
4. **Begin Requirements Gathering**: Starts asking structured questions

### Sample Interaction

```
/intake

🤖 [Intake Mode - Onboarder Agent]

## Current Status
**Active PRD/CRD:** [Shows current GitHub issues]
**Current Branch:** main
**Session Context:** [Shows current session information]

I'm now in Intake Mode and will help gather requirements for your project. 
Let me start by understanding the context and scope of what we're building.

**Understanding the Need**
- What problem are we trying to solve?
- What is the current state vs. desired state?
- Who is affected by this problem?

[Continues with structured questions...]
```

## The Intake Process

### 1. Context Identification
Claude first determines what type of work this is:
- Analyzes your description for keywords and indicators
- Asks clarifying questions if context is unclear
- Selects appropriate template and question set

### 2. Requirements Gathering
Claude guides you through structured questions:

**Business Context Questions**:
- What is the market opportunity?
- Who are the key stakeholders?
- What is the expected ROI?
- What is the competitive landscape?

**ML Engineering Questions**:
- What ML problem are we solving?
- What data sources are available?
- What are the performance requirements?
- How will we measure model success?

**Software Engineering Questions**:
- What are the functional requirements?
- What systems need to integrate?
- What are the user stories?
- What are the technical constraints?

### 3. Document Creation
Based on the context, Claude creates the appropriate document:
- **Opportunity Brief** for business contexts
- **ML Requirements Document** for ML engineering
- **Requirements Document** for software engineering

### 4. Validation and Review
Claude ensures all information is captured:
- Reviews requirements for completeness
- Validates understanding with you
- Confirms all template sections are addressed
- Updates session context with findings

## Required Checklist Items

Before exiting `/intake` mode, all these items must be completed:

### Core Activities (Required)
- [ ] **Read Mode Context Files** - Load all relevant rule and session files
- [ ] **Identify Context Type** - Determine business, ML, or software engineering context
- [ ] **Gather Initial Requirements** - Document high-level needs and objectives
- [ ] **Identify Stakeholders** - List key people and their roles
- [ ] **Capture Success Criteria** - Define what success looks like
- [ ] **Document Constraints** - Identify technical, business, or resource constraints
- [ ] **Initial Risk Assessment** - Identify potential risks or blockers
- [ ] **Create Structured Document** - Generate appropriate requirements document
- [ ] **Validate Understanding** - Review requirements with operator
- [ ] **Update Session Context** - Update active session with findings
- [ ] **Ready for Mode Switch** - Confirm completion and readiness to proceed

### Optional Activities
- [ ] **Identify Dependencies** - Document external dependencies
- [ ] **Estimate Effort** - Provide initial effort estimates
- [ ] **Plan Timeline** - Suggest implementation timeline

## Quality Standards

Your requirements document must meet these standards:

### Template Compliance
- **All sections completed** - No placeholder text remaining
- **Proper formatting** - Follows template structure exactly
- **Complete metadata** - Agent name, date, version included

### Content Quality
- **Specific and measurable** - Requirements are testable
- **Clear and unambiguous** - No vague or ambiguous language
- **Complete and comprehensive** - All necessary information captured
- **Stakeholder-validated** - Requirements confirmed with stakeholders

### Context Appropriateness
- **Right template used** - Appropriate for work context
- **Relevant sections emphasized** - Focus on context-specific needs
- **Appropriate level of detail** - Suitable for intended audience

## Transitioning from /intake

### Allowed Next Steps
After completing `/intake`, you can transition to:

- **`/discover`** - Deep dive into constraints and feasibility (recommended)
- **`/scope`** - Define technical approach if discovery is complete
- **`/plan`** - Return to planning if different work is needed

### Exit Requirements
Before transitioning, ensure:
- [ ] All checklist items are completed
- [ ] Requirements document is created and validated
- [ ] Session context is updated
- [ ] Stakeholder alignment is confirmed

### Transition Command
```
/clear
/discover
```

Always use `/clear` before switching modes to ensure clean context boundaries.

## Common Patterns

### Starting New Features
```
1. /intake (gather requirements)
2. /discover (analyze feasibility)  
3. /scope (define approach)
4. /design (create architecture)
5. /dev (implement solution)
```

### Business Opportunity Analysis
```
1. /intake (understand opportunity)
2. /discover (market analysis)
3. /scope (business case)
4. /deliver (strategic plan)
```

### ML Project Initiation
```
1. /intake (define ML problem)
2. /discover (data discovery)
3. /scope (model approach)
4. /design (ML architecture)
5. /extract (data preparation)
```

## Tips for Success

### Preparation
- **Have stakeholder access** - Ensure you can get answers to questions
- **Gather existing materials** - Collect any existing requirements or specifications
- **Understand business context** - Know the broader goals and constraints
- **Identify decision makers** - Know who needs to approve requirements

### During Intake
- **Be specific** - Provide concrete examples and detailed information
- **Ask questions** - If something isn't clear, ask for clarification
- **Think systematically** - Consider all aspects of the problem
- **Validate understanding** - Confirm that Claude captured requirements correctly

### Best Practices
- **One problem at a time** - Focus on single issue or opportunity
- **Start with why** - Understand business value and motivation
- **Consider all stakeholders** - Include technical and business perspectives
- **Document assumptions** - Be explicit about what you're assuming
- **Plan for validation** - Think about how you'll validate requirements

## Troubleshooting

### Common Issues

**Context Detection Problems**
- *Issue*: Claude selects wrong context type
- *Solution*: Explicitly state the context ("This is an ML project...")

**Incomplete Requirements**  
- *Issue*: Requirements document missing key information
- *Solution*: Review template sections and ask specific follow-up questions

**Unclear Success Criteria**
- *Issue*: Success metrics are vague or unmeasurable  
- *Solution*: Define specific, quantifiable success criteria

**Stakeholder Alignment Issues**
- *Issue*: Different stakeholders have conflicting requirements
- *Solution*: Document conflicts and identify decision-making process

### Getting Help

**Check Templates**
- Review appropriate template to see what information is needed
- Use template sections as a guide for complete requirements

**Validate with Stakeholders**
- Share draft requirements document for feedback
- Confirm understanding with key stakeholders before proceeding

**Use Validation Commands**
```bash
# Check if requirements are complete
agenticops artifacts check --phase intake --strict

# Validate checklist completion  
agenticops todos check --mode intake --strict
```

## Examples

### Business Context Example
**Input**: "We want to expand our platform to new markets"
**Output**: Opportunity Brief with market analysis, competitive landscape, ROI projections, and go-to-market strategy

### ML Context Example
**Input**: "We need to predict customer churn"
**Output**: ML Requirements Document with data sources, model performance targets, training requirements, and deployment specifications

### Software Context Example  
**Input**: "We need an API for mobile app integration"
**Output**: Requirements Document with API specifications, authentication requirements, data models, and integration patterns

The `/intake` command ensures that every Value Train workflow starts with a solid foundation of well-understood requirements, setting the stage for successful delivery of high-quality solutions.