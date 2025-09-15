# Value Train - One Page Guide

## The 9 Modes (In Order)

| Mode | Question | Output |
|------|----------|--------|
| Intake | What needs to be built? | Initial understanding |
| Discover | What don't we know? | Research findings |
| Scope | What's most important? | Priorities & boundaries |
| Design | What are the requirements? | Specs & acceptance criteria |
| Build | Code it | Working software |
| Evaluate | Does it work? | Test results |
| Deliver | Ship it | Deployed code |
| Operate | Keep it running | Monitoring data |
| Improve | Make it better | Improvements |

## Quick Patterns

**New Feature:** intake → discover → scope → design → build → evaluate → deliver

**Bug Fix:** intake → discover → build → evaluate → deliver  

**Research:** discover → scope → design

**Hotfix:** intake → build → deliver

## Tracking Template

```markdown
# Task: [Your Task Name]

## Status: [Current Mode]

### ✅ Intake
- [ ] Requirements clear
- [ ] Success criteria defined

### ⏳ Discover  
- [ ] Technical approach researched
- [ ] Unknowns identified

### Scope
- [ ] Priorities clear (must/nice/defer)
- [ ] Boundaries defined

### Design
- [ ] Architecture planned
- [ ] Patterns chosen

### Build
- [ ] Code written
- [ ] Tests written

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

*That's it. No complex setup. Just start with Intake and follow the modes.*