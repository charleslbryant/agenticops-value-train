# CLAUDE.md

Instructions for Claude when working with Value Train projects.

## Value Train Modes

The Value Train uses 10 conceptual modes to organize work. These are **mental models**, not commands - just ways to think about what type of work you're doing:

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

## How to Use Modes

Modes are simply **labels for the current type of work**. When working on a task:

1. **Identify the current mode** based on what you're doing
2. **Update the GitHub issue** to show current mode
3. **Focus on activities** appropriate for that mode
4. **Progress naturally** through modes as work evolves

## Example Workflow

```markdown
GitHub Issue #42: Add dark mode

## Current Mode: Design
(Previously completed: Plan, Research)

Working on UX mockups and technical specifications for theme implementation...
```

## Development Principles

1. **Prioritize ruthlessly** - Ship must-haves first
2. **Document in issues** - Maintain context across sessions
3. **Test first** - Write tests before implementation
4. **Small commits** - Commit frequently with clear messages
5. **Collaborate** - Update issues for handoffs

## Working with Issues

GitHub issues are the **single source of truth**:
- Document decisions and progress
- Update current mode as work progresses
- Leave clear next steps for others
- Maintain context across sessions

## No Special Commands

Value Train doesn't require special commands or state management. Just:
- Think about what type of work you're doing
- Label it with the appropriate mode
- Focus on that mode's goals
- Move to the next mode when ready

Keep it simple. Keep it practical.