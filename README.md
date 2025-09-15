# AgenticOps Value Train™

> **⚠️ EXPERIMENTAL PROJECT**
>
> This is an active research and development project exploring AI-agent collaboration workflows. The methodology and tooling are rapidly evolving. Expect frequent changes, incomplete features, and experimental approaches.
>
> **Current Status**: Simplified to 10 conceptual modes with Feature Slice Requirements Documents (FSRDs)

![Value Train Logo](/assets/images/value-train-logo.png)

*DevOps for AI Agents: A structured workflow methodology for getting software built right with human-AI collaboration.*

## What is AgenticOps Value Train™?

Value Train brings the rigor, discipline, automation, and reliability of DevOps to AI-agent collaboration. Instead of ad-hoc conversations with AI, Value Train provides a structured methodology that transforms human-AI software development into a predictable, traceable, and scalable process.

**Core Innovation**: Ten conceptual modes organized around **Feature Slice Requirements Documents (FSRDs)** that eliminate handoffs between product requirements and technical implementation.

1. **Plan** - Defining business requirements
2. **Research** - Investigating technical approach
3. **Design** - Creating UX, UI, technical specifications, and go-to-market strategies
4. **Build** - Writing code
5. **Validate** - Testing (unit tests, integration tests, e2e tests)
6. **Review** - Code review, PR review, client demos, and merging
7. **Deliver** - Deploying to production
8. **Operate** - Monitoring and maintenance
9. **Evaluate** - Assessing that delivery meets requirements from plan
10. **Improve** - Optimization and enhancement

**Key Philosophy**: These are **mental models**, not rigid commands. Think in **vertical slices** that deliver end-to-end user value, not horizontal technical layers. This methodology transforms ML engineering from experimental chaos into structured, automated processes.

## The Problem Value Train Solves

**Before Value Train**: AI-agent collaboration was ad-hoc, context was lost between sessions, requirements were unclear, and handoffs between product and engineering created friction.

**After Value Train**: Structured workflow with persistent context, clear requirements through FSRDs, and eliminated handoffs through vertical slice thinking.

> *"DevOps revolutionized software delivery. Value Train brings that same transformation to AI-agent collaboration."*

## Quick Start

### Interactive Planning with `/plan`
**RECOMMENDED**: Use the `/plan` command for automatic FSRD generation:
```
/plan → "I want to add user authentication"
      → Conversational requirements gathering
      → Generates Feature Slice Requirements Document
      → Creates GitHub issue with implementation plan
      → Provides testable work items (1-2 day granularity)
```

### For a New Feature Slice:
```
Plan     → Use /plan command to generate FSRD
Research → Investigate technical approach
Design   → Create UX/UI and technical specifications
Build    → Write code following FSRD work items
Validate → Run tests (unit, integration, e2e)
Review   → Code review and PR merge
Deliver  → Deploy to production
```

### For a Bug Fix:
```
Plan     → Document bug and expected behavior
Research → Find root cause
Build    → Fix it
Validate → Verify fix with tests
Review   → Code review
Deliver  → Deploy patch
```

### For Client Work:
```
Plan     → Use /plan for client requirements FSRD
Research → Study their systems and constraints
Design   → Technical specifications and mockups
Build    → Implementation
Validate → Testing with client scenarios
Review   → Client demo and feedback
Deliver  → Ship to client environment
```

## How to Use

### Option 1: Interactive Planning with `/plan`
**RECOMMENDED**: Use the `/plan` command for structured requirements gathering:
- Creates Feature Slice Requirements Documents automatically
- Generates GitHub issues with implementation plans
- Provides 3-tier templates (Micro/Standard/Full) based on complexity
- Forces vertical slice thinking for end-to-end user value

### Option 2: Mental Model Only
Use the modes as a checklist for any work:
- Have I defined the business requirements? (Plan)
- Have I researched the technical approach? (Research)
- Have I created specifications? (Design)
- Have I written code? (Build)
- Have I tested thoroughly? (Validate)
- Have I gotten code review? (Review)
- Have I deployed? (Deliver)

### Option 3: GitHub Issues as Truth Source
**PRIMARY WORKFLOW**: Maintain context in GitHub issues:

```markdown
GitHub Issue #42: Add dark mode (Feature Slice)

## Current Mode: Build
(Previously completed: Plan, Research, Design)

## FSRD Generated via /plan command
- **Slice Type**: Standard (3-day implementation)
- **User Value**: Users can toggle between light/dark themes
- **Vertical Slice**: Complete theme system from UI to persistence

## Implementation Plan (from FSRD)
### Build 🚧
- [ ] Create ThemeContext and provider
- [ ] Implement CSS custom properties
- [ ] Add toggle component to header
- [ ] Add localStorage persistence
- [ ] Update all existing components

### Validate
- [ ] Unit tests for ThemeContext
- [ ] Integration tests for persistence
- [ ] Accessibility testing

### Review
- [ ] Code review with screenshots
- [ ] Cross-browser testing

### Deliver
- [ ] Deploy to staging
- [ ] Production deployment

**Next Steps**: Move to Validate mode after Build completion
```

## Core Principles

1. **Vertical slices** - Each feature slice delivers end-to-end user value
2. **One mode at a time** - Focus on the current stage
3. **FSRD-driven development** - Use Feature Slice Requirements Documents for clarity
4. **GitHub issues as truth** - Maintain context across sessions
5. **Testable work items** - Break work into 1-2 day granular tasks
6. **Continuous handoff elimination** - Product and engineering unified in FSRDs

## Mode Details

### Plan - Defining Business Requirements
**Purpose:** Create Feature Slice Requirements Documents using `/plan` command

**Key Activity:** Use `/plan` command for conversational requirements gathering
- Automatically generates FSRD (Micro/Standard/Full templates)
- Creates GitHub issues with implementation plans
- Forces vertical slice thinking
- Provides testable work items (1-2 day granularity)

**Output:** FSRD with clear business requirements and implementation plan

---

### Research - Investigating Technical Approach
**Purpose:** Learn what we need to know to deliver the slice

**Activities:**
- Research technical approaches and alternatives
- Identify unknowns, risks, and dependencies
- Investigate libraries, tools, and patterns
- Study existing systems and constraints

**Output:** Technical findings and recommendations documented

---

### Design - Creating UX, UI, Technical Specifications
**Purpose:** Detailed specifications for user experience and technical implementation

**Activities:**
- Create UX flows and UI mockups
- Document technical architecture and API contracts
- Define data models and database changes
- Specify acceptance criteria and Definition of Done
- Plan go-to-market strategies (if applicable)

**Output:** Complete specifications ready for implementation

---

### Build - Writing Code
**Purpose:** Implement the feature slice following FSRD work items

**Best practices:**
- Follow FSRD implementation plan
- Write tests first (TDD)
- Commit frequently with clear messages
- Complete work items in 1-2 day increments

**Output:** Working code that implements the vertical slice

---

### Validate - Testing (Unit, Integration, E2E)
**Purpose:** Ensure the slice works correctly across all levels

**Activities:**
- Unit tests for individual components
- Integration tests for component interactions
- End-to-end tests for complete user journeys
- Performance and accessibility testing

**Output:** Thoroughly tested, validated code

---

### Review - Code Review, PR Review, Client Demos
**Purpose:** Validation through peer review and stakeholder feedback

**Activities:**
- Code review for quality and standards
- Pull request review and approval
- Client demonstrations and feedback
- Final acceptance criteria verification

**Output:** Reviewed and approved implementation

---

### Deliver - Deploying to Production
**Purpose:** Ship the feature slice to users

**Activities:**
- Deploy to staging environment
- Production deployment
- Feature flag management
- Documentation updates

**Output:** Live feature slice delivering user value

---

### Operate - Monitoring and Maintenance
**Purpose:** Ensure the slice continues working in production

**Activities:**
- Monitor metrics and performance
- Check error logs and alerts
- Respond to operational issues
- Track usage patterns

**Output:** Operational insights and health metrics

---

### Evaluate - Assessing Delivery Against Plan
**Purpose:** Validate that the slice meets original requirements

**Activities:**
- Compare delivered functionality to FSRD requirements
- Measure success criteria and user adoption
- Gather user feedback and usage data
- Document lessons learned

**Output:** Assessment of slice success and areas for improvement

---

### Improve - Optimization and Enhancement
**Purpose:** Make the slice better based on real usage

**Activities:**
- Analyze performance bottlenecks
- Identify user experience improvements
- Plan technical debt reduction
- Iterate based on feedback

**Output:** Improvement backlog for next iterations

## FAQ

**Q: Do I have to use all 10 modes?**
A: No. Use what makes sense. Simple bug fix? Maybe just Plan → Research → Build → Validate → Deliver. Complex feature? Use all modes.

**Q: What's the difference between Micro, Standard, and Full FSRDs?**
A: **Micro** (<1 day): Title, Description, Requirements, DoD. **Standard** (1-5 days): Core sections. **Full** (>5 days): All sections including risk assessment and metrics.

**Q: Can I go backwards between modes?**
A: Yes! If Build reveals you need more Research, go back. Modes are guidelines, not rigid gates.

**Q: How is this different from Agile/Scrum?**
A: Value Train is compatible with any methodology. It's a structured way to approach individual feature slices within your sprints, with emphasis on vertical delivery.

**Q: Why Feature Slice Requirements Documents instead of traditional PRDs?**
A: FSRDs eliminate handoffs between product and engineering by combining user requirements with implementation planning in a single document.

## Examples

### Example 1: Adding Dark Mode (Feature Slice)

**Using `/plan` command:**
```
/plan → "Add dark mode toggle for better user experience"
```

**Generated FSRD (Standard template):**
```
Plan (FSRD Generated):
- User Story: Users can toggle between light/dark themes
- Business Value: Improved accessibility and user preference
- Vertical Slice: Complete theme system from UI toggle to persistence
- Success Criteria: Theme persists across sessions, works in all browsers

Research:
- Current app uses CSS-in-JS with styled-components
- React Context pattern for global state
- localStorage for persistence
- WCAG contrast requirements

Design:
- UX: Toggle button in header with accessibility labels
- Technical: ThemeProvider + CSS custom properties
- API: Theme context with light/dark/system modes
- Acceptance: Sub-100ms theme switching

Build (Work Items from FSRD):
- [ ] Create ThemeContext with reducer (1 day)
- [ ] Implement CSS custom properties system (1 day)
- [ ] Add toggle component with accessibility (1 day)
- [ ] Add localStorage persistence (0.5 day)

Validate:
- Unit tests for ThemeContext
- Integration tests for persistence
- Accessibility audit with screen reader

Review:
- Code review with visual regression testing
- Cross-browser testing (Chrome, Firefox, Safari)

Deliver:
- Feature flag rollout to 10% users
- Full deployment after metrics validation
```

### Example 2: API Performance Issue (Micro Slice)

**Using `/plan` command:**
```
/plan → "Dashboard API calls are taking 5+ seconds"
```

**Generated FSRD (Micro template):**
```
Plan:
- Problem: Dashboard loads slowly (5+ seconds)
- Root Cause: N+1 query problem in user data fetching
- User Value: Sub-2 second dashboard load times

Research:
- Profiled queries: 200+ individual user lookups
- Database missing composite indexes
- No query result caching

Build:
- [ ] Add composite index on user_profiles (0.5 day)
- [ ] Implement query batching for user data (1 day)
- [ ] Add Redis caching layer (0.5 day)

Definition of Done:
- [ ] Load tests show <2 second response
- [ ] Query count reduced by 95%
- [ ] Production monitoring confirms improvement
```

## Getting Started

1. **Use `/plan` command** - Interactive FSRD generation for any new feature
2. **Create GitHub issue** - Automatically generated with implementation plan
3. **Follow the slice** - Work through modes focusing on end-to-end user value
4. **Update issue progress** - Maintain context across sessions
5. **Iterate and improve** - Learn from each slice delivery

### 💡 Pro Tips
- **Start with `/plan`**: Let the command guide you through requirements gathering
- **Think vertically**: Each slice should deliver complete user value, not technical layers
- **Use GitHub issues**: They maintain context across sessions for humans and AI
- **Granular work items**: Keep tasks to 1-2 days for better tracking and delivery

### 🚀 Quick Commands
- `/plan` - Generate Feature Slice Requirements Document
- Update GitHub issues with current mode and progress
- Use Value Train modes as mental models for any work

## The Value Train Philosophy

Value Train transforms AI-agent collaboration from experimental chaos into engineering discipline:

- **Vertical slices deliver value** - End-to-end user journeys over technical layers
- **FSRDs eliminate handoffs** - Product and engineering unified in single documents
- **Structure prevents chaos** - Modes provide guardrails without rigid constraints
- **GitHub issues as truth** - Persistent context across all sessions
- **Testable work items** - 1-2 day granularity enables continuous delivery
- **AI-agent collaboration** - Structured workflow optimized for human-AI teams
- **Traceable and reproducible** - Every decision and context is captured

## Project Status & Roadmap

**Current Focus**: Simplified 10-mode methodology with FSRD-driven development

**Evolution**: This represents a distillation of earlier complex multi-agent systems into practical, immediately usable workflow concepts.

**Technology Stack**:
- **Workflow**: 10 conceptual modes (mental models)
- **Documentation**: Feature Slice Requirements Documents (FSRDs)
- **Integration**: GitHub Issues for persistent context
- **Commands**: `/plan` for interactive requirements gathering

---

*AgenticOps Value Train: Where DevOps discipline meets AI-agent collaboration* 🚂

*Bringing rigor, automation, and reliability to the future of software development*