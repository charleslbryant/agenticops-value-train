# Rules System User Guide

This guide explains how to work within the Value Train rules system as an operator. The rules system ensures consistent, high-quality outcomes across all Value Train operations.

## What Are Rules?

Rules are the foundational guidelines that define how Value Train operates. They ensure:
- **Consistency**: Every operation follows the same standards
- **Quality**: All deliverables meet defined criteria  
- **Predictability**: You know what to expect from each mode and transition
- **Compliance**: Work follows established best practices

## Types of Rules

### Universal Rules
Apply to all modes and contexts:

- **Session Workflow** - How sessions start, progress, and complete
- **Task Management** - GitHub issue workflow and project management
- **Git Workflow** - Branch management and commit standards
- **Documentation** - Requirements for all documentation

### Mode-Specific Rules
Apply to specific Value Train modes:

- **Intake Rules** - Requirements gathering and context understanding
- **Discover Rules** - Deep discovery of constraints and feasibility  
- **Scope Rules** - Technical approach definition and timeline planning
- **Build Rules** - Implementation standards and quality gates

### Context-Specific Rules
Adapt based on your work type:

- **Business Context** - Strategic analysis and opportunity evaluation
- **ML Engineering Context** - Data requirements and model development
- **Software Engineering Context** - Code development and system integration

## Working With Rules

### Rule Enforcement Levels

#### 1. Documentation Guidelines
- Human-readable rules in `/docs/rules/`
- Provide context and examples
- Explain the "why" behind each rule

#### 2. Command Integration
- Slash commands (like `/intake`) reference applicable rules
- Commands guide you through rule compliance
- Built-in checklists ensure nothing is missed

#### 3. Automated Validation
- CLI commands automatically enforce critical rules
- Immediate feedback when rules are violated
- Prevents progression until requirements are met

### Following Rules During Operations

#### Starting a Session
1. **Read Session Startup Rules** - Always review `/docs/rules/session-workflow.md`
2. **Load Context** - Read product documentation and current state
3. **Select One Task** - Focus on single GitHub issue at a time
4. **Create Feature Branch** - Follow git workflow rules

#### During Mode Execution
1. **Check Mode Rules** - Review checklist for current mode
2. **Follow Template Requirements** - Use appropriate artifact templates
3. **Validate Quality Gates** - Ensure all criteria are met before proceeding
4. **Update Session Context** - Keep active session information current

#### Completing Work
1. **Complete All Checklist Items** - No unchecked items allowed
2. **Follow Git Workflow** - Proper commit messages and PR process
3. **Update Documentation** - Required for user-facing features
4. **Transition Properly** - Follow allowed mode transitions only

## Common Rule Categories

### Session Management Rules

**One Task Focus**
- Work on ONE GitHub issue at a time
- Complete current task before starting new one  
- If scope expands, check with operator before proceeding

**Session Lifecycle**
- Read all startup context files
- Select task from "Now" priority
- Create feature branch following git-workflow.md
- Complete session with proper handoff

### Quality Standards

**Documentation Requirements**
- User-facing features need user guides
- Technical features need developer guides
- Update existing guides when making changes
- Include documentation review in PR process

**Testing Standards**
- Write failing test first (TDD)
- Implement minimum code to pass
- Refactor and improve
- Maintain test coverage

### GitHub Workflow Rules

**Issue Hierarchy**
- **PRDs** - Product requirements (too broad for single session)
- **CRDs** - User stories (implementable within feature branch)  
- **Tasks** - Specific implementation items (completable in single session)

**Priority Management**
- **Now** - Current active work (limit 1-2 tasks)
- **Next** - Ready for work after current tasks
- **Future** - Planned but not yet ready

**One Piece Flow**
- Only one PRD with "now" priority per project
- Only one CRD with "now" priority per operator
- Only one Task with "now" priority per session

## Rule Violations and Resolution

### When Rules Are Violated

**Automatic Prevention**
- CLI commands block invalid operations
- Git hooks prevent non-compliant commits
- CI/CD blocks merges with incomplete checklists

**Warning Indicators**
- Missing required artifacts
- Unchecked checklist items
- Invalid mode transitions
- Incomplete documentation

### Resolving Rule Violations

1. **Review the Specific Rule** - Understand what's required
2. **Check Current State** - Use validation commands to assess
3. **Complete Missing Requirements** - Address each violation systematically
4. **Validate Compliance** - Run checks to confirm resolution
5. **Proceed with Confidence** - Continue once all rules are satisfied

### Getting Help

**Rule Documentation**
- `/docs/rules/` contains all rule definitions
- Each rule file includes examples and rationale
- TodoWrite templates show exactly what's required

**Validation Commands**
```bash
# Check if all artifacts are present
agenticops artifacts check --phase current --strict

# Verify checklist completion
agenticops todos check --strict --mode current

# Validate session state
agenticops session validate --current
```

## Benefits of Following Rules

### For You as an Operator
- **Clear Expectations** - Always know what's required
- **Quality Assurance** - Confidence in your deliverables
- **Efficient Workflow** - No time wasted on rework
- **Professional Growth** - Learn best practices systematically

### For the Team
- **Consistent Quality** - All work meets same standards
- **Smooth Handoffs** - Predictable artifact structure  
- **Reduced Bugs** - Quality gates prevent issues
- **Knowledge Sharing** - Common standards enable collaboration

### For the Project
- **Reliable Delivery** - Predictable timelines and quality
- **Maintainable Codebase** - Consistent patterns and documentation
- **Compliance Ready** - Built-in adherence to standards
- **Continuous Improvement** - Rules evolve based on lessons learned

## Advanced Rule Usage

### Context Detection
The system automatically detects whether you're working on:
- **Business** opportunities (market analysis, strategy)
- **ML Engineering** projects (data science, model development)
- **Software Engineering** tasks (application development, integration)

### Rule Customization
While core rules are mandatory, some aspects can be adapted:
- Template selection based on context
- Tool availability based on mode
- Validation criteria based on work type

### Rule Evolution
Rules improve over time based on:
- Team feedback and lessons learned
- New best practices and standards
- Tool and technology changes
- Project-specific requirements

## Quick Reference

### Essential Commands
```bash
# Start session with rule validation
/begin

# Check current rule compliance  
agenticops rules validate --current

# Advance to next mode (with rule checks)
/discover
```

### Key Rule Files
- `/docs/rules/session-workflow.md` - Session lifecycle
- `/docs/rules/task-management.md` - GitHub workflow
- `/docs/rules/git-workflow.md` - Code management
- `/docs/rules/documentation-rules.md` - Documentation standards

### Mode Checklists
- `/docs/rules/checklists/intake-checklist.md`
- `/docs/rules/checklists/discover-checklist.md`
- `/docs/rules/checklists/scope-checklist.md`
- And more for each mode...

Remember: Rules exist to help you succeed. When in doubt, check the documentation, use validation commands, and ask for clarification. Following rules consistently leads to better outcomes for everyone involved in the Value Train process.