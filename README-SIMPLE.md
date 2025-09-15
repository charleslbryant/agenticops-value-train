# Value Train™ - Simple Version

*A structured workflow for getting software built right.*

## What is Value Train?

Nine simple modes that guide you from idea to production:

1. **`/intake`** - What needs to be built?
2. **`/discover`** - What do we need to learn first?
3. **`/scope`** - How much work is this?
4. **`/design`** - How should we build it?
5. **`/build`** - Write the code
6. **`/evaluate`** - Does it work?
7. **`/deliver`** - Ship it
8. **`/operate`** - Keep it running
9. **`/improve`** - Make it better

That's it. No complex configs. No 18 phases. No 7 agents. Just a simple workflow.

## Quick Start

### For a New Feature:
```bash
/intake     # Gather requirements
/discover   # Research approach
/scope      # Estimate effort
/design     # Plan architecture
/build      # Write code
/evaluate   # Test it
/deliver    # Deploy
```

### For a Bug Fix:
```bash
/intake     # Understand the bug
/discover   # Find root cause
/build      # Fix it
/evaluate   # Verify fix
/deliver    # Deploy patch
```

### For Refactoring:
```bash
/discover   # Identify problem areas
/scope      # Define refactor boundaries
/design     # Plan new structure
/build      # Refactor
/evaluate   # Ensure nothing broke
```

## How to Use

### Option 1: Mental Model Only
Just use the modes as a checklist. Ask yourself:
- Have I understood what needs to be built? (`/intake`)
- Do I know enough to build it? (`/discover`)
- Have I planned the approach? (`/design`)
- etc.

### Option 2: With Claude.ai
Tell Claude: "Let's use Value Train. Start with `/intake` for [your task]"

Claude will guide you through each mode with appropriate questions.

### Option 3: Simple Tracking
Create a `value-train.md` file in your project:

```markdown
# Current Mode: /build

## /intake ✅
- Understood requirements
- Identified stakeholders

## /discover ✅
- Researched existing solutions
- Identified technical constraints

## /scope ✅
- Estimated 2 days
- Defined deliverables

## /design ✅
- Created architecture diagram
- Chose tech stack

## /build 🚧
- [ ] Implement API
- [ ] Add frontend
- [ ] Write tests

## /evaluate
- [ ] Run tests
- [ ] Code review

## /deliver
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

### /scope - Effort Estimation
**Purpose:** Define boundaries and estimate work

**Questions to answer:**
- What's in scope vs out of scope?
- How long will this take?
- What resources are needed?
- What are the risks?

**Output:** Scoped work plan with estimates

---

### /design - Architecture Planning
**Purpose:** Design the solution before coding

**Activities:**
- Create architecture diagrams
- Define data models
- Plan API contracts
- Choose patterns and tools

**Output:** Technical design document

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
- Code review
- Performance testing

**Output:** Validated, tested code

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
/intake
- Users want dark mode for night usage
- Should respect system preferences
- Need toggle in settings

/discover
- Current app uses CSS-in-JS
- Need to research theme switching patterns
- Check browser compatibility

/scope
- 3 days estimated
- Will affect all components
- Need to update design system

/design
- Use React Context for theme state
- CSS variables for colors
- LocalStorage for persistence

/build
- Create ThemeContext
- Add toggle component
- Update all components

/evaluate
- Test in multiple browsers
- Check accessibility contrast
- Verify persistence works

/deliver
- Deploy to staging for QA
- Get design approval
- Deploy to production
```

### Example 2: Fixing Performance Issue

```
/intake
- App is slow when loading large datasets
- Users reporting timeouts
- Affects dashboard page

/discover
- Profile current performance
- Found N+1 query problem
- Database missing indexes

/build
- Add database indexes
- Implement query batching
- Add caching layer

/evaluate
- Load test with large dataset
- Verify 10x performance improvement

/deliver
- Deploy during maintenance window
- Monitor performance metrics
```

## Getting Started

1. **Pick a task** - Something you need to build
2. **Start with /intake** - Write down what you know
3. **Move through modes** - Don't skip steps
4. **Track progress** - Use todos or markdown
5. **Iterate** - Go through modes multiple times if needed

## The Value Train Philosophy

- **Structure prevents chaos** - A little process goes a long way
- **Think before coding** - The modes before `/build` save time
- **Small steps** - Better to go through all modes quickly than get stuck
- **Continuous improvement** - Every iteration teaches you something

---

*Value Train: Making software development as reliable as clockwork* ⚙️

*No complex setup. No steep learning curve. Just a simple, effective workflow.*