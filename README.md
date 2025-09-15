# Value Train™ - Simple Version

*A structured workflow for getting software built right.*

## What is Value Train?

Nine simple modes that guide you from idea to production:

1. **Intake** - What needs to be built?
2. **Discover** - What do we need to learn first?
3. **Scope** - What's in/out of scope? Constraints?
4. **Design** - Requirements and specifications
5. **Build** - Write the code
6. **Evaluate** - Does it work?
7. **Deliver** - Ship it
8. **Operate** - Keep it running
9. **Improve** - Make it better

That's it. No complex configs. No 18 phases. No 7 agents. Just a simple workflow.

## Quick Start

### For a New Feature:
```
Intake     → Understand the need
Discover   → Research approach  
Scope      → Define priorities
Design     → Specify requirements
Build      → Write code
Evaluate   → Test it
Deliver    → Deploy
```

### For a Bug Fix:
```
Intake     → Understand the bug
Discover   → Find root cause
Build      → Fix it
Evaluate   → Verify fix
Deliver    → Deploy patch
```

### For Refactoring:
```
Discover   → Identify problem areas
Scope      → Define refactor boundaries
Design     → Plan new structure
Build      → Refactor
Evaluate   → Ensure nothing broke
```

## How to Use

### Option 1: Mental Model Only
Just use the modes as a checklist. Ask yourself:
- Have I understood what needs to be built? (Intake)
- Do I know enough to build it? (Discover)
- Have I planned the approach? (Design)
- etc.

### Option 2: With Claude.ai
Tell Claude: "Let's use Value Train for [your task]"

Claude will help you think through each mode as you progress.

### Option 3: Simple Tracking
Create a `value-train.md` file in your project:

```markdown
# Current Mode: Build

## Intake ✅
- Understood requirements
- Identified stakeholders

## Discover ✅
- Researched existing solutions
- Identified technical constraints

## Scope ✅
- Must have: Basic theme toggle
- Nice to have: Custom colors
- Ship first, iterate later

## Design ✅
- Created architecture diagram
- Chose tech stack

## Build 🚧
- [ ] Implement API
- [ ] Add frontend
- [ ] Write tests

## Evaluate
- [ ] Run tests
- [ ] Code review

## Deliver
- [ ] Create PR
- [ ] Deploy to staging
- [ ] Deploy to production
```

## Core Principles

1. **One mode at a time** - Focus on the current stage
2. **Complete before moving on** - Don't skip steps
3. **Document decisions** - Write down why, not just what
4. **Small iterations** - Go through all modes quickly, then iterate

## Mode Details

### /intake - Requirements Gathering
**Purpose:** Understand what needs to be built and why

**Questions to answer:**
- What problem are we solving?
- Who will use this?
- What does success look like?
- What are the constraints?

**Output:** Clear requirements document or user story

---

### /discover - Research & Learning
**Purpose:** Figure out what you don't know

**Activities:**
- Research existing solutions
- Identify technical challenges
- Spike on unknown technologies
- Talk to domain experts

**Output:** Technical findings and approach options

---

### /scope - Boundaries & Priorities
**Purpose:** Define what we will and won't do, and what matters most

**Questions to answer:**
- What's in scope vs out of scope?
- What are the must-haves vs nice-to-haves?
- What constraints do we have (technical, regulatory, etc)?
- What can we ship first and iterate on?

**Output:** Clear priorities and boundaries

---

### /design - Requirements & Specifications
**Purpose:** Define detailed requirements and technical specifications

**Activities:**
- Document functional requirements
- Define non-functional requirements
- Specify API contracts
- Create data models
- Define acceptance criteria

**Output:** Requirements document and technical specifications

---

### /build - Implementation
**Purpose:** Write the actual code

**Best practices:**
- Write tests first (TDD)
- Commit frequently
- Follow existing patterns
- Document as you go

**Output:** Working code

---

### /evaluate - Testing & Validation
**Purpose:** Ensure it works correctly

**Activities:**
- Run automated tests
- Manual testing
- **Code review (automated via Claude)**
- Performance testing

**Output:** Validated, tested code

*Note: PRs automatically trigger Claude code review via `.github/workflows/claude-code-review.yml`*

---

### /deliver - Deployment
**Purpose:** Get it to production

**Activities:**
- Create pull request
- Deploy to staging
- Production deployment
- Update documentation

**Output:** Deployed feature

---

### /operate - Monitoring
**Purpose:** Ensure it keeps working

**Activities:**
- Monitor metrics
- Check error logs
- Respond to alerts
- Track performance

**Output:** Operational insights

---

### /improve - Optimization
**Purpose:** Make it better based on real usage

**Activities:**
- Analyze usage patterns
- Identify bottlenecks
- Plan improvements
- Iterate

**Output:** Improvement backlog

## FAQ

**Q: Do I have to use all 9 modes?**
A: No. Use what makes sense. Small bug fix? Maybe just `/intake` → `/build` → `/deliver`.

**Q: Can I go backwards?**
A: Yes! If `/build` reveals you need more `/discover`, go back.

**Q: How is this different from Agile/Scrum?**
A: Value Train is compatible with any methodology. Think of it as a structured way to approach individual tasks within your sprints.

**Q: What about all the complex stuff in the original Value Train?**
A: We removed it. This is the simplified version focused on practical software development.

## Examples

### Example 1: Adding Dark Mode to an App

```
Intake:
- Users want dark mode for night usage
- Should respect system preferences
- Need toggle in settings

Discover:
- Current app uses CSS-in-JS
- Need to research theme switching patterns
- Check browser compatibility

Scope:
- MUST: Theme switching, settings toggle
- NICE: System preference detection, animations
- DEFER: Custom color picker, per-page themes
- CONSTRAINT: Must work in IE11

Design:
- Requirement: Toggle between light/dark themes
- Requirement: Remember user preference
- Spec: Use CSS custom properties for theming
- Spec: React Context for state management
- Acceptance: Works in all target browsers

Build:
- Create ThemeContext
- Add toggle component
- Update all components

Evaluate:
- Test in multiple browsers
- Check accessibility contrast
- Verify persistence works

Deliver:
- Deploy to staging for QA
- Get design approval
- Deploy to production
```

### Example 2: Fixing Performance Issue

```
Intake:
- App is slow when loading large datasets
- Users reporting timeouts
- Affects dashboard page

Discover:
- Profile current performance
- Found N+1 query problem
- Database missing indexes

Build:
- Add database indexes
- Implement query batching
- Add caching layer

Evaluate:
- Load test with large dataset
- Verify 10x performance improvement

Deliver:
- Deploy during maintenance window
- Monitor performance metrics
```

## Getting Started

1. **Create a GitHub issue** - Use the Value Train task template
2. **Start with Intake** - Document requirements in the issue
3. **Move through modes** - Update issue as you progress
4. **Collaborate** - Others can continue from your issue context
5. **Iterate** - Go through modes multiple times if needed

### 💡 Pro Tip: Persistent Context
GitHub issues maintain context across sessions. Update them regularly so anyone (human or AI) can pick up where you left off. See [collaboration guide](docs/collaboration.md) for details.

## The Value Train Philosophy

- **Structure prevents chaos** - A little process goes a long way
- **Think before coding** - The modes before `/build` save time
- **Small steps** - Better to go through all modes quickly than get stuck
- **Continuous improvement** - Every iteration teaches you something

---

*Value Train: Making software development as reliable as clockwork* ⚙️

*No complex setup. No steep learning curve. Just a simple, effective workflow.*