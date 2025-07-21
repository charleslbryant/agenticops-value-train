# /discover Command - User Guide

The `/discover` command switches Claude into Discover Mode, where it acts as the **Onboarder Agent** to conduct deep discovery of constraints, feasibility analysis, and comprehensive investigation of the problem space. This typically follows `/intake` in the Value Train workflow.

## When to Use /discover

Use `/discover` when you need to:
- **Validate initial requirements** - Test assumptions made during intake
- **Conduct feasibility analysis** - Determine if the proposed solution is viable
- **Investigate constraints** - Understand technical, business, and resource limitations
- **Analyze data availability** - Assess data sources, quality, and accessibility
- **Identify risks** - Conduct comprehensive risk analysis with mitigation strategies
- **Refine understanding** - Deepen knowledge of the problem space before scoping

## What /discover Does

The `/discover` command:
1. **Reviews intake artifacts** - Analyzes requirements documents from previous mode
2. **Validates assumptions** - Tests key assumptions through investigation and stakeholder input
3. **Assesses feasibility** - Evaluates technical, business, and resource constraints
4. **Investigates data** - Deep dive into data sources, quality, and availability
5. **Maps dependencies** - Identifies external dependencies and integration points
6. **Analyzes risks** - Comprehensive risk assessment with mitigation strategies
7. **Creates discovery report** - Documents all findings and recommendations

## How Context Detection Works

The `/discover` command adapts its investigation approach based on your work type:

### Business Context
**Focus**: Market validation, competitive analysis, regulatory requirements
- **Investigation Areas**: Market demand, competitive landscape, financial constraints
- **Key Questions**: Is there real market demand? What are regulatory requirements?
- **Validation Methods**: Market research, competitor analysis, stakeholder interviews
- **Output**: **Business Discovery Report** with market validation and feasibility
- **Risk Focus**: Market risks, competitive threats, regulatory compliance

### ML Engineering Context  
**Focus**: Data discovery, model feasibility, technical constraints
- **Investigation Areas**: Data quality, computational requirements, model complexity
- **Key Questions**: Is the data sufficient? Are performance targets realistic?
- **Validation Methods**: Data profiling, technical architecture review, prototype testing
- **Output**: **ML Discovery Report** with data assessment and technical feasibility
- **Risk Focus**: Data quality issues, computational limitations, model performance risks

### Software Engineering Context
**Focus**: Technical constraints, system integration, architecture analysis
- **Investigation Areas**: Existing systems, performance requirements, integration complexity
- **Key Questions**: How will this integrate? What are the performance implications?
- **Validation Methods**: System analysis, architecture review, technical spike testing
- **Output**: **Technical Discovery Report** with integration assessment
- **Risk Focus**: Integration complexity, performance bottlenecks, technical debt

## Using the /discover Command

### Basic Usage
```
/discover
```

Claude will switch to Discover Mode and begin comprehensive investigation of the problem space.

### Typical Entry Point
Usually follows `/intake`:
```
/intake    (gather requirements)
/clear
/discover  (validate and investigate)
```

### Command Response
When you run `/discover`, Claude will:

1. **Display Mode Header**: Shows Discover Mode - Onboarder Agent
2. **Show Current Status**: Reviews active work and session context
3. **Create Investigation Plan**: TodoWrite checklist with all discovery activities
4. **Begin Deep Investigation**: Starts systematic validation and analysis

### Sample Interaction

```
/discover

🤖 [Discover Mode - Onboarder Agent]

## Current Status
**Active PRD/CRD:** Issue #123 - Customer Churn Prediction
**Current Branch:** main
**Session Context:** Intake completed with ML Requirements Document

I'm now in Discover Mode and will conduct deep investigation of the ML problem 
space defined in our intake phase. Let me start by reviewing the requirements 
and validating our key assumptions.

**Investigation Areas for ML Context:**
- Data source validation and quality assessment
- Model performance feasibility analysis  
- Computational requirements evaluation
- Risk assessment and mitigation planning

[Continues with systematic discovery...]
```

## The Discovery Process

### 1. Artifact Review
Claude first analyzes intake outputs:
- Reviews requirements document from `/intake`
- Identifies key assumptions that need validation
- Maps out investigation areas based on context
- Plans systematic discovery approach

### 2. Assumption Validation
Critical testing of initial assumptions:

**Business Context Validation**:
- Market demand verification through research
- Competitive landscape analysis
- Regulatory requirement investigation
- Financial constraint assessment

**ML Context Validation**:
- Data availability and quality assessment
- Model performance target feasibility
- Computational resource requirement analysis
- Technical approach validation

**Software Context Validation**:
- Integration complexity assessment
- Performance requirement feasibility
- Technical architecture validation
- Resource and timeline reality check

### 3. Constraint Discovery
Comprehensive analysis of limitations:
- **Technical Constraints**: Infrastructure, performance, integration
- **Business Constraints**: Budget, timeline, regulatory, organizational
- **Resource Constraints**: Team capacity, skills, tools, access
- **Data Constraints**: Quality, availability, privacy, compliance

### 4. Risk Analysis
Deep dive into potential challenges:
- **High-Impact Risks**: Issues that could derail the project
- **Likelihood Assessment**: Probability of risks occurring
- **Mitigation Strategies**: Approaches to reduce or eliminate risks
- **Contingency Plans**: Alternative approaches if risks materialize

### 5. Discovery Documentation
Comprehensive reporting of findings:
- **Executive Summary**: Key findings and recommendations
- **Detailed Analysis**: Evidence-based conclusions for each area
- **Risk Register**: Prioritized risks with mitigation plans
- **Updated Requirements**: Refined requirements based on discoveries

## Required Checklist Items

Before exiting `/discover` mode, all these items must be completed:

### Investigation Activities (Required)
- [ ] **Read Mode Context Files** - Load all relevant rule and session files
- [ ] **Review Intake Artifacts** - Analyze requirements from previous mode
- [ ] **Validate Assumptions** - Test key assumptions from requirements gathering
- [ ] **Assess Technical Feasibility** - Evaluate technical constraints and capabilities
- [ ] **Analyze Data Availability** - Investigate data sources and accessibility
- [ ] **Identify Dependencies** - Map external dependencies and integration points
- [ ] **Risk Deep Dive** - Comprehensive risk analysis with mitigation strategies
- [ ] **Constraint Documentation** - Document discovered constraints and limitations
- [ ] **Stakeholder Validation** - Confirm findings with relevant stakeholders
- [ ] **Update Requirements** - Refine requirements based on discovery findings
- [ ] **Discovery Report** - Create comprehensive discovery document
- [ ] **Update Session Context** - Document findings and recommendations
- [ ] **Ready for Mode Switch** - Confirm discovery completion and readiness

### Quality Standards
Your discovery report must meet these standards:

**Thoroughness**
- **All assumptions tested** - No key assumption left unvalidated
- **Evidence-based conclusions** - All findings supported by concrete evidence
- **Comprehensive risk analysis** - All significant risks identified and assessed

**Accuracy**
- **Stakeholder validation** - Critical findings confirmed with relevant stakeholders
- **Multiple source verification** - Important facts validated from multiple sources
- **Objective analysis** - Findings based on evidence, not assumptions

**Completeness**
- **All investigation areas covered** - No significant area left unexplored
- **Clear recommendations** - Actionable next steps based on findings
- **Updated requirements** - Requirements refined based on discovery results

## Investigation Framework

### Data Discovery (For All Contexts)

**Data Source Analysis**
- What data sources are available?
- What is the quality and completeness of the data?
- What are the access requirements and restrictions?
- What is the update frequency and latency?

**Data Quality Assessment**
- How accurate and reliable is the data?
- What cleaning and preparation is required?
- Are there data privacy or compliance issues?
- What are the data governance requirements?

### Technical Feasibility Assessment

**Infrastructure Analysis**
- What technical infrastructure is available?
- What are the performance and scalability requirements?
- What integration points exist with current systems?
- What security and compliance requirements apply?

**Implementation Complexity**
- How complex is the proposed technical solution?
- What skills and expertise are required?
- What tools and technologies are needed?
- What are the development and maintenance costs?

### Business Viability Investigation

**Market and Competition**
- What is the competitive landscape?
- What market trends affect viability?
- What regulatory requirements apply?
- What are the business case assumptions?

**Organizational Readiness**
- What organizational changes are required?
- What change management challenges exist?
- What training and support is needed?
- What are the adoption and success factors?

## Common Discovery Patterns

### ML Project Discovery
```
1. Data source investigation and quality assessment
2. Model performance target feasibility analysis
3. Computational resource requirement validation
4. Training data availability and labeling assessment
5. Model deployment and monitoring capability review
6. Business impact measurement and validation approach
```

### Software Development Discovery
```
1. Existing system architecture and integration analysis
2. Performance and scalability requirement validation
3. User experience and interface requirement investigation
4. Security and compliance requirement assessment
5. Development team capability and resource analysis
6. Timeline and delivery milestone feasibility review
```

### Business Initiative Discovery
```
1. Market opportunity validation and competitive analysis
2. Financial investment and ROI requirement assessment
3. Stakeholder alignment and change management analysis
4. Regulatory and compliance requirement investigation
5. Organizational capability and resource assessment
6. Success measurement and KPI validation approach
```

## Transitioning from /discover

### Allowed Next Steps
After completing `/discover`, you can transition to:

- **`/scope`** - Define technical approach and implementation plan (recommended)
- **`/intake`** - Return to requirements if major gaps discovered
- **`/plan`** - Return to planning if project direction needs change

### Exit Requirements
Before transitioning, ensure:
- [ ] All discovery checklist items completed
- [ ] Discovery report created with comprehensive findings
- [ ] Key assumptions validated or updated
- [ ] Critical risks identified with mitigation strategies
- [ ] Stakeholder validation completed
- [ ] Session context updated with results

### Transition Command
```
/clear
/scope
```

## Tips for Effective Discovery

### Preparation
- **Review intake thoroughly** - Understand what was learned and assumed
- **Plan investigation systematically** - Don't miss important areas
- **Engage stakeholders early** - Get access to key people and information
- **Gather evidence** - Focus on facts over opinions

### During Discovery
- **Stay objective** - Don't let preferences bias investigation
- **Dig deep** - Surface-level analysis isn't enough
- **Document everything** - Keep detailed records of findings
- **Validate with stakeholders** - Confirm critical findings

### Best Practices
- **Test assumptions rigorously** - Challenge what was assumed in intake
- **Look for showstoppers** - Identify issues that could kill the project
- **Understand constraints fully** - Know what you're working within
- **Plan for contingencies** - Have backup approaches ready

## Troubleshooting

### Common Issues

**Insufficient Access to Information**
- *Issue*: Can't get access to needed data or stakeholders
- *Solution*: Document access requirements and escalate to project sponsor

**Contradictory Information**
- *Issue*: Different sources provide conflicting information
- *Solution*: Investigate discrepancies and identify authoritative sources

**Overwhelming Complexity**
- *Issue*: Problem space seems too complex to understand fully
- *Solution*: Break down into smaller investigation areas and prioritize

**Stakeholder Availability**
- *Issue*: Key stakeholders not available for validation
- *Solution*: Document assumptions and schedule follow-up validation

### Getting Help

**Use Validation Commands**
```bash
# Validate discovery completeness
agenticops artifacts check --phase discover --strict

# Check discovery report quality
agenticops quality check --artifact discovery-report.md --template discovery

# Validate stakeholder sign-off
agenticops stakeholders validate --phase discover
```

**Escalation Guidelines**
- Document what you cannot validate or investigate
- Clearly identify risks and assumptions
- Provide recommendations for addressing gaps
- Escalate blockers to appropriate decision makers

## Examples

### Business Context Example
**Input**: Market expansion opportunity
**Discovery Focus**: Market research, competitive analysis, regulatory requirements
**Output**: Business Discovery Report with market validation and go/no-go recommendation

### ML Context Example  
**Input**: Customer churn prediction model
**Discovery Focus**: Data quality assessment, model feasibility, infrastructure requirements
**Output**: ML Discovery Report with data recommendations and technical approach validation

### Software Context Example
**Input**: Mobile app API integration
**Discovery Focus**: System architecture, performance requirements, integration complexity
**Output**: Technical Discovery Report with integration strategy and implementation recommendations

The `/discover` command ensures that every Value Train workflow has a solid foundation of validated assumptions and comprehensive understanding before moving to implementation planning. This reduces project risk and increases the likelihood of successful delivery.