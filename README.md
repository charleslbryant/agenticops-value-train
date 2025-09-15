# Value Train™ - Simple Version

*A structured workflow for getting software built right.*

## What is Value Train?

Nine simple modes that guide you from idea to production:

1. **Plan** - What does the business need?
2. **Research** - What do we need to learn?
3. **Scope** - What's the simplest solution?
4. **Design** - Technical specifications
5. **Build** - Write the code
6. **Evaluate** - Does it work?
7. **Deliver** - Ship it
8. **Operate** - Keep it running
9. **Improve** - Make it better

That's it. No complex configs. No 18 phases. No 7 agents. Just a simple workflow.

## Quick Start

### For a New Feature:
```
Plan       → Define business requirements
Research   → Investigate technical approach  
Scope      → Define MVP
Design     → Create specifications
Build      → Write code
Evaluate   → Test it
Deliver    → Deploy
```

### For a Bug Fix:
```
Plan       → Understand the bug report
Research   → Find root cause
Build      → Fix it
Evaluate   → Verify fix
Deliver    → Deploy patch
```

### For Client Work:
```
Plan       → Gather client requirements
Research   → Study their systems
Scope      → Define simplest solution
Design     → Technical specifications
Build      → Implementation
Evaluate   → Testing
Deliver    → Ship to client
```

## How to Use

### Option 1: Mental Model Only
Just use the modes as a checklist. Ask yourself:
- Have I defined the business requirements? (Plan)
- Have I researched the technical approach? (Research)
- Have I found the simplest solution? (Scope)
- Have I created specifications? (Design)
- etc.

### Option 2: With Claude.ai
Tell Claude: "Let's use Value Train for [your task]"

Claude will help you think through each mode as you progress.

### Option 3: Simple Tracking
Create a `value-train.md` file in your project:

```markdown
# Current Mode: Build

## Plan ✅
- Defined business requirements
- Identified stakeholders
- Created GitHub issues

## Research ✅
- Investigated technical approaches
- Identified risks
- Researched libraries

## Scope ✅
- Must have: Basic theme toggle
- Nice to have: Custom colors
- Defer: Per-page themes

## Design ✅
- Created technical specifications
- Defined acceptance criteria

## Build 🚧
- [ ] Write tests first
- [ ] Implement functionality
- [ ] Commit frequently

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

### Plan - Business Requirements
**Purpose:** Define what the business needs

**Questions to answer:**
- What problem are we solving?
- Who are the stakeholders?
- What does success look like?
- What's the business value?

**Output:** Clear business requirements and GitHub issues

---

### Research - Technical Investigation
**Purpose:** Learn what we need to know to deliver

**Activities:**
- Research technical approaches
- Identify unknowns and risks
- Investigate libraries and tools
- Study existing systems

**Output:** Technical findings documented in issues

---

### Scope - Simplest Solution
**Purpose:** Find the simplest solution that meets requirements

**Questions to answer:**
- What's the MVP?
- What are must-haves vs nice-to-haves?
- What can we defer?
- What's the simplest approach?

**Output:** Clear scope and priorities

---

### Design - Technical Specifications
**Purpose:** Create detailed technical specifications

**Activities:**
- Document technical approach
- Define acceptance criteria
- Specify API contracts
- Create data models
- Plan architecture

**Output:** Technical specifications and acceptance criteria

---

### Build - Implementation
**Purpose:** Write the actual code

**Best practices:**
- Write tests first (TDD)
- Commit frequently
- Follow existing patterns
- Document as you go

**Output:** Working code

---

### Evaluate - Testing & Validation
**Purpose:** Ensure it works correctly

**Activities:**
- Run automated tests
- Manual testing
- **Code review (automated via Claude)**
- Performance testing

**Output:** Validated, tested code

*Note: PRs automatically trigger Claude code review via `.github/workflows/claude-code-review.yml`*

---

### Deliver - Deployment
**Purpose:** Get it to production

**Activities:**
- Create pull request
- Deploy to staging
- Production deployment
- Update documentation

**Output:** Deployed feature

---

### Operate - Monitoring
**Purpose:** Ensure it keeps working

**Activities:**
- Monitor metrics
- Check error logs
- Respond to alerts
- Track performance

**Output:** Operational insights

---

### Improve - Optimization
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
Plan:
- Users want dark mode for night usage
- Business value: Improved user experience
- Success criteria: Users can toggle themes

Research:
- Current app uses CSS-in-JS
- Need to research theme switching patterns
- Check browser compatibility

Scope:
- MVP: Basic light/dark toggle
- DEFER: Custom colors, per-page themes
- Simplest: CSS variables + React Context

Design:
- Spec: Theme context for state
- Spec: CSS custom properties for colors
- Acceptance: Works in all browsers
- Acceptance: Preference persists

Build:
- Write theme toggle tests
- Implement ThemeContext
- Add toggle component

Evaluate:
- All tests passing
- Accessibility verified
- Cross-browser tested

Deliver:
- Create PR with screenshots
- Deploy to staging
- Ship to production
```

### Example 2: Fixing Performance Issue

```
Plan:
- Users reporting slow dashboard
- Business impact: User frustration
- Success: Sub-2 second load time

Research:
- Profile current performance
- Found N+1 query problem
- Database missing indexes

Scope:
- MVP: Add indexes and batching
- DEFER: Complete rewrite
- Simplest: Optimize queries

Build:
- Add database indexes
- Implement query batching
- Add caching layer

Evaluate:
- Load test with large dataset
- Verified 10x improvement

Deliver:
- Deploy during maintenance window
- Monitor performance metrics
```

## Getting Started

1. **Create a GitHub issue** - Use the Value Train task template  
2. **Start with Plan** - Define business requirements
3. **Research** - Investigate technical approach
4. **Scope** - Find the simplest solution
5. **Build through Deliver** - Implement and ship
6. **Iterate** - Learn and improve

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