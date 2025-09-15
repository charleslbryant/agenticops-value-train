# Extending Value Train

How to adapt Value Train for your team, project, or organization.

## Core vs Custom

### Keep the Core
The 9 modes are universal - they work for any software project:
- Intake → Discover → Scope → Design → Build → Evaluate → Deliver → Operate → Improve

### Customize the Details
What you do in each mode depends on your context:
- Startup vs Enterprise
- Web vs Mobile vs Embedded
- Agile vs Waterfall
- Solo vs Team

## Team Adaptations

### For Startups
- **Intake**: Quick Slack discussion
- **Discover**: 30-min research spike
- **Scope**: T-shirt sizing (S/M/L)
- **Design**: Whiteboard sketch
- **Build**: Ship to production
- **Evaluate**: Test in production
- **Deliver**: Continuous deployment

### For Enterprises
- **Intake**: Requirements document
- **Discover**: Proof of concept
- **Scope**: Detailed estimation
- **Design**: Architecture review board
- **Build**: Feature branches
- **Evaluate**: QA environment
- **Deliver**: Release management

### For Open Source
- **Intake**: GitHub issue discussion
- **Discover**: RFC process
- **Scope**: Milestone planning
- **Design**: Design doc PR
- **Build**: Pull request
- **Evaluate**: CI/CD pipeline
- **Deliver**: Version release

## Adding Your Own Modes

While 9 modes cover most needs, you can add context-specific modes:

```csharp
public enum ExtendedMode
{
    Intake,
    Discover,
    Scope,
    Design,
    Prototype,  // New: Quick proof of concept
    Build,
    Evaluate,
    Security,   // New: Security review
    Deliver,
    Operate,
    Improve
}
```

## Integration with Existing Processes

### With Scrum
- **Sprint Planning**: Use intake/discover/scope
- **Daily Standup**: Report current mode
- **Sprint Review**: Show evaluate/deliver results
- **Retrospective**: Focus on improve mode

### With Kanban
- Create swim lanes for each mode
- Track WIP limits per mode
- Measure cycle time through modes
- Identify bottleneck modes

### With GitHub
```yaml
# .github/ISSUE_TEMPLATE/value-train.md
name: Value Train Task
about: Track work through Value Train modes

## Current Mode: [Intake]

### Intake
- [ ] Problem defined
- [ ] Success criteria clear

### Discover
- [ ] Research complete
- [ ] Approach chosen

### Scope
- [ ] Estimate provided
- [ ] Risks identified

[etc...]
```

## Automation Ideas

### Git Branch Naming
```bash
intake/user-story-123
discover/spike-auth
design/api-schema
build/feature-xyz
```

### Commit Messages
```bash
git commit -m "intake: Define requirements for dark mode"
git commit -m "build: Implement theme context"
git commit -m "evaluate: Add theme switching tests"
```

### CI/CD Integration
```yaml
# .github/workflows/value-train.yml
name: Value Train Checks

on: [push]

jobs:
  mode-check:
    runs-on: ubuntu-latest
    steps:
      - name: Check branch name matches mode
      - name: Verify tests exist (evaluate mode)
      - name: Check documentation (deliver mode)
```

## Metrics and Reporting

### Track Time in Modes
```sql
SELECT 
  mode,
  AVG(duration_hours) as avg_time,
  COUNT(*) as tasks_count
FROM value_train_metrics
GROUP BY mode
ORDER BY avg_time DESC;
```

### Identify Patterns
- Which modes take longest?
- Where do tasks get stuck?
- What modes get skipped?
- Which modes have most rework?

### Success Metrics
- **Intake Quality**: % of tasks with clear requirements
- **Discover Efficiency**: Research time vs build time ratio
- **Scope Accuracy**: Estimated vs actual time
- **Build Velocity**: Story points per sprint
- **Evaluate Coverage**: Test coverage percentage
- **Deliver Frequency**: Deployments per week
- **Operate Stability**: Uptime percentage
- **Improve Impact**: Performance gains

## Tool Integration

### Jira Custom Fields
```json
{
  "customfield_10001": {
    "name": "Value Train Mode",
    "type": "select",
    "options": [
      "Intake", "Discover", "Scope", 
      "Design", "Build", "Evaluate",
      "Deliver", "Operate", "Improve"
    ]
  }
}
```

### Slack Bot
```javascript
// Slackbot commands
/value-train status      // Show current mode
/value-train next        // Move to next mode
/value-train checklist   // Show mode checklist
/value-train report      // Weekly mode metrics
```

### VS Code Extension
```json
{
  "value-train.currentMode": "build",
  "value-train.showModeInStatusBar": true,
  "value-train.reminderInterval": 30,
  "value-train.checklistOnModeChange": true
}
```

## Cultural Adoption

### Start Small
1. One team tries it for one sprint
2. Gather feedback
3. Adjust for your context
4. Roll out gradually

### Make it Visible
- Mode labels on task boards
- Mode status in standups
- Mode metrics in reports
- Celebrate mode completions

### Common Adjustments
- Combine modes (discover+scope)
- Skip modes (no operate for one-offs)
- Repeat modes (multiple build+evaluate cycles)
- Parallel modes (design while discovering)

## Anti-Patterns to Avoid

❌ **Mode Skipping**: Jumping straight to build
❌ **Mode Rushing**: Not completing mode goals
❌ **Mode Bureaucracy**: Excessive documentation
❌ **Mode Rigidity**: Refusing to go backward
❌ **Mode Silos**: Only certain people do certain modes

## Success Tips

✅ **Keep it lightweight** - Process should help, not hinder
✅ **Adapt to context** - One size doesn't fit all
✅ **Focus on value** - Modes are means, not ends
✅ **Iterate on process** - Continuously improve how you work
✅ **Make it yours** - Best process is one team actually uses

## Questions to Consider

1. Which modes does your team excel at?
2. Which modes does your team avoid?
3. What would team-specific mode checklists look like?
4. How could you measure mode effectiveness?
5. What tools could automate mode transitions?

## Your Implementation

Start with these three steps:
1. **Try it as-is** - Use basic 9 modes for one week
2. **Gather feedback** - What worked? What didn't?
3. **Adapt and iterate** - Make it work for your team

Remember: Value Train is a framework, not a prescription. Take what works, leave what doesn't, and make it your own.