# Value Train Mode Commands

Simple mode switching for the 9 Value Train modes.

## Commands

### `/intake`
Switch to Intake Mode - Gather requirements and understand what needs to be built.

### `/discover`
Switch to Discover Mode - Research unknowns and investigate technical approaches.

### `/scope`
Switch to Scope Mode - Define priorities, boundaries, and constraints.

### `/design`
Switch to Design Mode - Document requirements and create technical specifications.

### `/build`
Switch to Build Mode - Write code following TDD practices.

### `/evaluate`
Switch to Evaluate Mode - Test thoroughly and verify requirements.

### `/deliver`
Switch to Deliver Mode - Deploy code and update documentation.

### `/operate`
Switch to Operate Mode - Monitor production and track metrics.

### `/improve`
Switch to Improve Mode - Analyze usage and plan optimizations.

## Mode Behavior

When entering any mode:
1. Acknowledge the mode switch
2. Create appropriate todos for that mode
3. Focus on mode-specific activities
4. Track progress

## Integration with Code Review

The `/evaluate` mode naturally includes code review. When in this mode:
- Run tests
- Review code quality
- Check for security issues
- Verify requirements are met

This integrates with the Claude Code Review workflows in `.github/workflows/`