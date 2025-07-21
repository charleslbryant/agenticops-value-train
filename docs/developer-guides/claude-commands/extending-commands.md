# Extending Claude Commands - Developer Guide

This guide explains how to create, modify, and extend Claude slash commands for the Value Train system. Claude commands are the primary interface for mode-based operations and agent interactions.

## Understanding Claude Commands

### What Are Claude Commands?

Claude commands are slash commands (like `/intake`, `/discover`) that:
- **Switch Claude into specific modes** with defined behaviors and constraints
- **Load relevant context** including rules, session state, and project information
- **Guide structured workflows** through comprehensive checklists and validation
- **Enforce quality gates** before allowing mode transitions
- **Integrate with CLI commands** for deterministic business logic

### Command Architecture

```
Claude Command (/intake)
├── YAML Front Matter (metadata, tools, description)
├── Mode Header & Status Display
├── Workflow Description & Context Loading
├── TodoWrite Checklist (required activities)
├── Mode-Specific Rules & Guidelines
├── Exit Criteria & Transition Rules
└── Quality Gates & Validation
```

### Three-Layer Integration

Claude commands work within a three-layer architecture:

1. **Documentation Layer** - Human-readable command definitions
2. **LLM Guidance Layer** - Commands guide AI behavior through structured prompts
3. **CLI Enforcement Layer** - Deterministic validation and rule enforcement

## Command Structure Standards

### File Location and Naming

```
/.claude/commands/
├── intake.md          # Core mode commands
├── discover.md
├── scope.md
├── design.md
├── build.md           # Or extract.md, features.md, train.md for ML
├── evaluate.md
├── deliver.md
├── operate.md
├── improve.md
└── utility/           # Utility commands (future)
    ├── plan.md
    ├── clear.md
    └── begin.md
```

### Required Front Matter

Every Claude command must start with YAML front matter:

```yaml
---
description: Brief description of what this mode does (required)
allowed-tools: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), WebSearch, WebFetch
---
```

**Key Fields:**
- **`description`**: Clear, concise explanation of the command's purpose
- **`allowed-tools`**: Specific tools Claude can use in this mode (security constraint)

### Standard Command Template

```markdown
---
description: [Brief description of mode purpose]
allowed-tools: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), WebSearch, WebFetch
---

# [Mode] Mode - [Agent] Agent

Always start your chats with `🤖 [[Mode] Mode - [Agent] Agent]`

Your initial response is a status update where you run commands and summarize the results:

```
🤖 [[Mode] Mode - [Agent] Agent]

## Current Status
**Active PRD/CRD:**
!`gh issue list --label "PRD,now" --limit 1 || gh issue list --label "CRD,now" --limit 1`

**Current Branch:**
!`git branch --show-current`

**Session Context:**
!`cat docs/session-context/ACTIVE_SESSION.md | head -20`
```

## Workflow

[Detailed explanation of what this mode does, when to use it, and how it fits into the Value Train pipeline]

### Mode Context Files

Before starting the checklist, reread all mode context files. This ensures clean memory boundaries between modes.

**Rule Files:**
* `/docs/rules/session-workflow.md`
* `/docs/rules/task-management.md`
* `/docs/rules/documentation-rules.md`
* `/docs/product/`

**Session Context Files:**
* `/docs/session-context/CURRENT_STATE.md`
* `/docs/session-context/ACTIVE_SESSION.md`

### [Mode] Checklist (TodoWrite)

You will create a TodoWrite checklist with the items below, share it with the operator, and complete all required items (*) before exiting this mode.

0. **Read Mode Context Files***: Read all rule and session context files
1. **[Required Activity]***: [Specific, measurable activity]
2. **[Required Activity]***: [Specific, measurable activity]
[... continue with all required activities]

### Context-Specific Adaptations

#### Business Context  
- Focus on [business-specific concerns]
- **Output**: [Business-appropriate artifact]

#### ML Engineering Context
- Focus on [ML-specific concerns]
- **Output**: [ML-appropriate artifact]

#### Software Engineering Context
- Focus on [software-specific concerns]
- **Output**: [Software-appropriate artifact]

### Mode Rules

* **[Important Rule]**: [Explanation of rule and why it matters]
* **[Important Rule]**: [Explanation of rule and why it matters]

### Mode Exit Requirement

Before exiting this mode:
* All required checklist items must be complete
* [Specific deliverable] created
* Session context updated with [specific information]
* Wait for operator to `/clear` context before switching modes

### Available Transitions

* `/[next-mode]` - [Description of when to use this transition]
* `/[alternative-mode]` - [Description of alternative path]

---

*[Mode] Mode Active - [Brief reminder of mode purpose]*
```

## Creating New Commands

### 1. Identify Command Requirements

Before creating a new command, determine:

**Mode Purpose**
- What specific problem does this mode solve?
- When in the Value Train pipeline does this occur?
- What agent role is responsible for this mode?

**Context Adaptations**
- How does this mode differ for business vs. ML vs. software contexts?
- What different artifacts or approaches are needed?
- Are there context-specific rules or constraints?

**Integration Points**
- What commands typically precede this mode?
- What commands can follow this mode?
- How does this integrate with CLI commands and validation?

### 2. Define Mode Checklist

Create comprehensive checklist covering:

**Entry Activities**
- Context loading and validation
- Prerequisites verification
- Stakeholder identification

**Core Activities**
- Main work items specific to this mode
- Artifact creation requirements
- Quality validation steps

**Exit Activities**
- Deliverable completion verification
- Session context updates
- Handoff preparation

### 3. Implement Command File

Create the command file following the standard template:

```bash
# Create new command file
touch .claude/commands/[new-mode].md

# Follow naming convention: lowercase, hyphen-separated if needed
# Examples: discover.md, build.md, extract-data.md
```

**Implementation Checklist:**
- [ ] YAML front matter with description and allowed tools
- [ ] Mode header with agent assignment
- [ ] Status update commands for context loading
- [ ] Comprehensive workflow description
- [ ] Rule file references for context loading
- [ ] TodoWrite checklist with all required activities
- [ ] Context-specific adaptations (business/ML/software)
- [ ] Mode rules and constraints
- [ ] Exit criteria and transition rules
- [ ] Quality gates and validation requirements

### 4. Create Supporting Documentation

**Required User Guide**
Create user guide at `/docs/user-guides/claude-commands/[mode].md`:

```markdown
# /[mode] Command - User Guide

[Comprehensive user documentation following the intake.md pattern]

## When to Use /[mode]
## What /[mode] Does  
## How Context Detection Works
## Using the /[mode] Command
## The [Mode] Process
## Required Checklist Items
## Quality Standards
## Transitioning from /[mode]
## Examples and Troubleshooting
```

**Optional Developer Guide**
For complex modes, create developer guide at `/docs/developer-guides/claude-commands/[mode]-development.md`

### 5. Integrate with CLI Commands

Define corresponding CLI commands for deterministic logic:

```csharp
// ValueTrain.Application/Features/[Mode]Mode/
public class Execute[Mode]Command : IRequest<Execute[Mode]Response>
{
    public string Context { get; set; }
    public int? IssueId { get; set; }
    // Mode-specific parameters
}

public class Execute[Mode]CommandHandler : IRequestHandler<Execute[Mode]Command, Execute[Mode]Response>
{
    public async Task<Execute[Mode]Response> Handle(Execute[Mode]Command request, CancellationToken cancellationToken)
    {
        // Implement deterministic mode logic
        // - Context detection
        // - Rule validation  
        // - Artifact generation
        // - Quality checks
    }
}
```

## Modifying Existing Commands

### Safe Modification Process

1. **Read Current Implementation** - Understand existing behavior and dependencies
2. **Identify Impact** - Determine what changes and what remains the same
3. **Update Incrementally** - Make small, testable changes
4. **Validate Behavior** - Test with different contexts and scenarios
5. **Update Documentation** - Ensure user guide reflects changes

### Common Modifications

#### Adding Context-Specific Behavior

```markdown
### Context-Specific Adaptations

#### [New Context] Context
- Focus on [context-specific concerns]
- Document [context-specific requirements]  
- **Output**: [Context-appropriate artifact using new template]
```

#### Adding New Activities

```markdown
### [Mode] Checklist (TodoWrite)

[Existing items...]
X. **[New Required Activity]***: [Clear description of new requirement]
Y. **[New Optional Activity]**: [Description of optional enhancement]
```

#### Updating Quality Gates

```markdown
### Mode Exit Requirement

Before exiting this mode:
* [Existing requirements...]
* [New requirement with clear validation criteria]
```

### Backward Compatibility

When modifying commands:
- **Preserve core workflow** - Don't break existing user expectations
- **Add, don't remove** - Extend functionality rather than replacing it
- **Clear migration path** - If changes are breaking, provide clear guidance
- **Version documentation** - Update user guides to reflect changes

## Advanced Command Patterns

### Multi-Context Commands

For commands that significantly differ by context:

```markdown
### Workflow

You are now in **[Mode] Mode** as the **[Agent] Agent**. This mode adapts based on task type:

**Business Context**: [Business-specific workflow description]
**ML Engineering Context**: [ML-specific workflow description]  
**Software Engineering Context**: [Software-specific workflow description]

### Context Detection and Routing

1. **Analyze Task Context** - Examine issue labels, description, and project type
2. **Select Appropriate Workflow** - Choose business, ML, or software approach
3. **Load Context-Specific Rules** - Reference appropriate rule files and templates
4. **Execute Adapted Checklist** - Follow context-appropriate activities
```

### Command Composition

For commands that include sub-workflows:

```markdown
### [Mode] Workflow

This mode consists of multiple phases:

#### Phase 1: [Sub-workflow Name]
[Phase-specific checklist and activities]

#### Phase 2: [Sub-workflow Name]  
[Phase-specific checklist and activities]

#### Phase 3: [Sub-workflow Name]
[Phase-specific checklist and activities]

### Phase Transition Rules
- Complete all Phase N activities before proceeding to Phase N+1
- Validate Phase N deliverables before transition
- Update session context at each phase boundary
```

### Command Dependencies

For commands with strict ordering requirements:

```markdown
### Entry Criteria

Before entering [Mode] Mode, ensure:
- [ ] Previous mode ([Previous Mode]) completed successfully
- [ ] Required artifacts from previous mode are validated
- [ ] Session context contains necessary information from previous work

### Dependency Validation

Use CLI commands to validate prerequisites:
```bash
# Validate previous mode completion
agenticops session validate --mode [previous-mode] --complete

# Check required artifacts exist
agenticops artifacts check --phase [previous-phase] --strict
```
```

## CLI Integration Patterns

### Context Detection Integration

```markdown
### Mode Context Files

Before starting the checklist, use CLI commands for deterministic context detection:

```bash
# Detect work context automatically
!`agenticops context detect --issue-id current --format yaml`

# Validate context detection result
!`agenticops context validate --detected [context] --issue-id current`
```

**Rule Files** (loaded based on detected context):
* Base rules: `/docs/rules/session-workflow.md`, `/docs/rules/task-management.md`
* Context-specific rules: `/docs/rules/contexts/[detected-context]-context.md`
```

### Artifact Management Integration

```markdown
### [Mode] Checklist (TodoWrite)

X. **Create Structured Document***: 
   ```bash
   # Generate appropriate template based on context
   !`agenticops artifacts create --template auto --context [detected-context] --mode [current-mode]`
   
   # Validate artifact completeness
   !`agenticops artifacts validate --artifact [artifact-path] --template [template-name]`
   ```

Y. **Validate Artifact Quality***:
   ```bash
   # Check artifact against quality standards
   !`agenticops quality check --artifact [artifact-path] --mode [current-mode]`
   ```
```

### Rule Enforcement Integration

```markdown
### Mode Rules

* **Deterministic Rule Enforcement**: Critical business logic validated by CLI
  ```bash
  # Validate all applicable rules for current mode and context
  !`agenticops rules validate --mode [current-mode] --context [detected-context]`
  
  # Check specific rule compliance
  !`agenticops rules check --rule [rule-name] --current-state`
  ```

* **Quality Gate Validation**: All quality gates must pass before mode exit
  ```bash
  # Validate mode completion before transition
  !`agenticops mode validate --mode [current-mode] --exit-criteria`
  ```
```

## Testing Commands

### Manual Testing Process

1. **Context Variation Testing**
   - Test command with business context scenarios
   - Test command with ML engineering context scenarios  
   - Test command with software engineering context scenarios

2. **Workflow Integration Testing**
   - Test transitions from expected previous modes
   - Test transitions to expected next modes
   - Test error handling for invalid transitions

3. **Checklist Completeness Testing**
   - Verify all required activities can be completed
   - Test partial completion and resumption
   - Validate quality gates and exit criteria

### Automated Testing

```bash
# Validate command file format
agenticops commands validate --command [mode]

# Test context detection with command
agenticops commands test --command [mode] --context business
agenticops commands test --command [mode] --context ml-engineering  
agenticops commands test --command [mode] --context software-engineering

# Validate command integration
agenticops commands integration-test --workflow intake,discover,scope
```

## Best Practices

### Command Design

1. **Single Responsibility** - Each command should have one clear purpose
2. **Context Awareness** - Adapt behavior appropriately for different work types
3. **Clear Boundaries** - Well-defined entry/exit criteria and transitions
4. **Quality Focus** - Built-in validation and quality gates
5. **Comprehensive Checklists** - Cover all necessary activities for success

### Documentation Standards

1. **Complete User Guides** - Every command needs comprehensive user documentation
2. **Clear Examples** - Provide concrete examples for each context type
3. **Troubleshooting** - Include common issues and solutions
4. **Integration Guidance** - Show how commands fit into broader workflows

### Maintainability

1. **Consistent Structure** - Follow established patterns and templates
2. **Version Control** - Track changes and maintain backward compatibility
3. **Regular Review** - Update commands based on user feedback and lessons learned
4. **Cross-Reference Updates** - Keep all related documentation synchronized

### Security Considerations

1. **Tool Restrictions** - Only allow necessary tools in allowed-tools list
2. **Input Validation** - Validate all inputs and parameters
3. **Access Control** - Ensure commands only access appropriate resources
4. **Audit Trail** - Log command usage and outcomes for review

## Common Pitfalls

### Design Issues

**Over-Complex Commands**
- *Problem*: Trying to do too much in one command
- *Solution*: Break complex workflows into multiple focused commands

**Insufficient Context Adaptation**
- *Problem*: One-size-fits-all approach doesn't work for different contexts
- *Solution*: Design clear adaptations for business/ML/software contexts

**Weak Quality Gates**
- *Problem*: Commands allow progression without proper validation
- *Solution*: Implement comprehensive quality checks and exit criteria

### Implementation Issues

**Missing CLI Integration**
- *Problem*: Relying solely on LLM for critical business logic
- *Solution*: Implement deterministic CLI commands for validation and enforcement

**Incomplete Documentation**
- *Problem*: Commands without proper user guides
- *Solution*: Create comprehensive documentation following established patterns

**Poor Error Handling**
- *Problem*: Commands fail gracefully without clear guidance
- *Solution*: Anticipate failure modes and provide clear recovery paths

### Maintenance Issues

**Outdated References**
- *Problem*: Commands reference moved or changed files
- *Solution*: Regular validation and updates of file references

**Inconsistent Updates**
- *Problem*: Command updates without corresponding documentation updates
- *Solution*: Include documentation review in command change process

**Missing Integration Testing**
- *Problem*: Commands work in isolation but fail in workflows
- *Solution*: Test command integration and workflow transitions regularly

## Contributing Guidelines

### Proposing New Commands

1. **Create RFC** - Document the need and proposed design
2. **Gather Feedback** - Review with team and stakeholders
3. **Prototype** - Create minimal viable implementation
4. **Test Thoroughly** - Validate across all contexts and scenarios
5. **Document Completely** - Create all required documentation
6. **Review Process** - Code review and approval before merging

### Modifying Existing Commands

1. **Impact Analysis** - Understand what will change and what depends on current behavior
2. **Backward Compatibility** - Ensure existing workflows continue to work
3. **Incremental Changes** - Make small, testable modifications
4. **Update Documentation** - Keep user guides synchronized with changes
5. **User Communication** - Inform users of significant changes

### Quality Standards

All command contributions must meet:
- **Complete implementation** following standard template
- **Comprehensive user documentation** with examples and troubleshooting
- **CLI integration** for deterministic business logic
- **Context adaptations** for business/ML/software engineering
- **Quality gates** and validation requirements
- **Integration testing** with existing workflow

Commands are the primary interface for Value Train operations. By following these patterns and practices, you can create powerful, reliable commands that enhance the Value Train experience while maintaining consistency and quality across the entire system.