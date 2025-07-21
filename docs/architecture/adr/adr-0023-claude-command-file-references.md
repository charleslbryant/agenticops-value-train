# ADR-0023: Claude Command File References Using @ Paths

## Status
Accepted

## Context
Our Claude commands in `.claude/commands/*.md` currently reference files using traditional relative paths like `/docs/rules/session-workflow.md`. However, Claude Code has a specific convention for file references that provides better integration and functionality.

According to Claude Code documentation, file references should use the `@` prefix to include file contents directly in commands. This convention:

1. **Includes File Contents**: The `@` prefix tells Claude Code to include the actual file contents, not just reference the path
2. **Standardized Convention**: This is the documented standard for Claude Code file references
3. **Better Integration**: Provides seamless integration with Claude Code's file handling system
4. **Enhanced Functionality**: Enables Claude to access and analyze file contents directly

Examples from documentation:
- `Review the implementation in @src/utils/helpers.js`
- `Compare @src/old-version.js with @src/new-version.js`

## Decision
We will update all file references in our Claude commands to use the `@` prefix convention as specified in Claude Code documentation.

### File Reference Standards
- **Rule Files**: `@/docs/rules/session-workflow.md`
- **Session Context**: `@/docs/session-context/ACTIVE_SESSION.md`
- **Templates**: `@/docs/templates/opportunity-brief.md`
- **Product Documentation**: `@/docs/product/`
- **Architecture Documents**: `@/docs/architecture/`

### Implementation Approach
1. Update all existing Claude commands to use `@` paths
2. Ensure consistent path formatting across all commands
3. Update documentation to reflect the new standard
4. Create developer guide for future command development

## Consequences

### Positive
- **Standards Compliance**: Aligns with Claude Code documented conventions
- **Enhanced Functionality**: Claude can directly access and include file contents
- **Better Integration**: Seamless integration with Claude Code file handling
- **Consistency**: Standardized approach across all commands
- **Future-Proof**: Following documented best practices

### Negative
- **Migration Effort**: Requires updating all existing commands
- **Learning Curve**: Team needs to understand the `@` path convention

### Neutral
- **Path Format Change**: Existing paths work but don't provide optimal functionality

## Implementation Plan
1. Update all 9 Claude commands with `@` path references
2. Test commands to ensure file access works correctly
3. Update developer documentation with `@` path standards
4. Create commit with all changes for consistency

## Acceptance Criteria
- [ ] All Claude commands use `@` prefix for file references
- [ ] Commands can successfully access referenced files
- [ ] Documentation updated to reflect new standards
- [ ] Developer guide includes `@` path conventions

## References
- [Claude Code Slash Commands Documentation](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- Claude Code Settings and File Access Documentation