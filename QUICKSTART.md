# Value Train - One Page Guide

## The 9 Modes (In Order)

| Mode | Question | Output |
|------|----------|--------|
| `/intake` | What needs to be built? | Requirements |
| `/discover` | What don't we know? | Research findings |
| `/scope` | How much work? | Time estimate |
| `/design` | How to build it? | Architecture plan |
| `/build` | Code it | Working software |
| `/evaluate` | Does it work? | Test results |
| `/deliver` | Ship it | Deployed code |
| `/operate` | Keep it running | Monitoring data |
| `/improve` | Make it better | Improvements |

## Quick Patterns

**New Feature:** intake → discover → scope → design → build → evaluate → deliver

**Bug Fix:** intake → discover → build → evaluate → deliver  

**Research:** discover → scope → design

**Hotfix:** intake → build → deliver

## Tracking Template

```markdown
# Task: [Your Task Name]

## Status: [Current Mode]

### ✅ /intake
- [ ] Requirements clear
- [ ] Success criteria defined

### ⏳ /discover  
- [ ] Technical approach researched
- [ ] Unknowns identified

### /scope
- [ ] Effort estimated
- [ ] Scope defined

### /design
- [ ] Architecture planned
- [ ] Patterns chosen

### /build
- [ ] Code written
- [ ] Tests written

### /evaluate
- [ ] Tests passing
- [ ] Code reviewed

### /deliver
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

Just say: "Let's use Value Train for [task]. Start with /intake"

---

*That's it. No complex setup. Just start with /intake and follow the modes.*