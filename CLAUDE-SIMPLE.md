# CLAUDE.md (Simplified)

Instructions for Claude when working with Value Train projects.

## Value Train Modes

When the user types a mode command, switch to that mode's focus:

- `/intake` - Gather requirements. Ask what, why, who, and success criteria.
- `/discover` - Research unknowns. Investigate technical approaches.
- `/scope` - Estimate effort. Define what's in/out of scope.
- `/design` - Plan architecture. Create technical design.
- `/build` - Write code. Follow TDD. Commit frequently.
- `/evaluate` - Test thoroughly. Verify requirements are met.
- `/deliver` - Deploy code. Create PRs, update docs.
- `/operate` - Monitor health. Check logs and metrics.
- `/improve` - Optimize based on usage. Plan enhancements.

## Mode Behavior

When entering a mode:
1. Acknowledge the mode switch
2. Create a todo list for that mode's activities
3. Guide the user through mode-appropriate tasks
4. Track progress with TodoWrite

## Example Interaction

```
User: /intake
Claude: Switching to intake mode. Let's gather requirements.
- What problem are we solving?
- Who will use this feature?
- What does success look like?
- Are there any constraints?

[Creates todos for requirements gathering]
```

## Development Principles

1. **One mode at a time** - Focus on current stage
2. **Complete before advancing** - Ensure mode goals are met
3. **Document everything** - Capture decisions and rationale
4. **Test first** - Write tests before implementation
5. **Small commits** - Commit frequently with clear messages

## Simplified Workflow

No complex YAML files, no 18 phases, no 7 agents. Just:
- 9 modes as a mental model
- Todos for tracking
- Git for version control
- Markdown for documentation

## Commands

The user may ask to:
- Switch modes: `/intake`, `/discover`, etc.
- Check status: "What mode are we in?"
- Show progress: "Show todos"
- Complete mode: "Ready for next mode"

Keep it simple. Keep it focused. Keep it practical.