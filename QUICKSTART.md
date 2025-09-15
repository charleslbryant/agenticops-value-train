# Value Train - One Page Guide

## The 9 Modes (In Order)

| Mode | Question | Output |
|------|----------|--------|
| Plan | What does the business need? | Requirements & issues |
| Research | What do we need to learn? | Technical findings |
| Scope | What's the simplest solution? | MVP definition |
| Design | What are the specifications? | Technical specs |
| Build | Code it | Working software |
| Evaluate | Does it work? | Test results |
| Deliver | Ship it | Deployed code |
| Operate | Keep it running | Monitoring data |
| Improve | Make it better | Improvements |

## Quick Patterns

**New Feature:** plan → research → scope → design → build → evaluate → deliver

**Bug Fix:** plan → research → build → evaluate → deliver  

**Client Work:** plan → research → scope → design → build → evaluate → deliver

**Hotfix:** plan → build → deliver

## Tracking Template

```markdown
# Task: [Your Task Name]

## Status: [Current Mode]

### ✅ Plan
- [ ] Business requirements defined
- [ ] Stakeholders identified

### ⏳ Research  
- [ ] Technical approach investigated
- [ ] Risks identified

### Scope
- [ ] MVP defined
- [ ] Simplest solution found

### Design
- [ ] Specifications created
- [ ] Acceptance criteria defined

### Build
- [ ] Tests written first
- [ ] Code implemented

### Evaluate
- [ ] Tests passing
- [ ] Code reviewed

### Deliver
- [ ] PR created
- [ ] Deployed

### Notes:
- 
```

## Three Rules

1. **Don't skip modes** - They exist for a reason
2. **Document decisions** - Future you will thank you
3. **Small iterations** - Go through all modes quickly, then repeat

## With Claude.ai

Just say: "Let's use Value Train for [task]"

---

*That's it. No complex setup. Just start with Plan and follow the modes.*