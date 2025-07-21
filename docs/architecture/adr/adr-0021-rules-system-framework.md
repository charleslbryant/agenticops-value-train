# ADR-0021: Rules System Framework

## Status
**Accepted**

## Context
Value Train agents need consistent, enforceable business logic to ensure deterministic behavior across all modes and operations. Without a structured rules system, agent behavior becomes inconsistent, unpredictable, and difficult to validate. The current approach relies heavily on prompt engineering, which is susceptible to hallucination and inconsistent interpretation.

Current challenges include:
- **Non-Deterministic Behavior**: LLM-based logic leads to inconsistent rule enforcement
- **Scattered Rules**: Business logic spread across prompts, commands, and documentation
- **Validation Difficulty**: No systematic way to verify rule compliance
- **Maintenance Overhead**: Rules changes require updates in multiple locations
- **Quality Assurance**: Inconsistent enforcement of quality gates and validation criteria

## Decision
We will implement a comprehensive rules system framework where:

1. **Centralized Rule Storage**: All rules stored in `/docs/rules/` with clear organization
2. **Deterministic Enforcement**: Critical business logic implemented in C# CLI commands
3. **Mode-Specific Integration**: Rules referenced and enforced by slash commands
4. **Layered Architecture**: Rules organized by scope (universal, mode-specific, context-specific)
5. **Validation Framework**: Automated rule compliance checking and reporting

## Architecture

### Rule Categories

#### Universal Rules
Rules that apply across all modes and contexts:
- **Session Workflow** (`session-workflow.md`) - Session lifecycle and state transitions
- **Task Management** (`task-management.md`) - GitHub issue workflow and project management
- **Git Workflow** (`git-workflow.md`) - Branch management and commit standards
- **Documentation Rules** (`documentation-rules.md`) - Documentation requirements and standards

#### Mode-Specific Rules
Rules that apply to specific Value Train modes:
- **Checklists** (`checklists/*.md`) - Mode-specific required activities and deliverables
- **Quality Gates** - Entry/exit criteria for each mode
- **Artifact Requirements** - Required outputs and validation criteria

#### Context-Specific Rules
Rules that adapt based on work context (business, ML engineering, software engineering):
- **Template Selection** - Context-appropriate artifact templates
- **Success Criteria** - Context-specific quality and completion standards
- **Tool Restrictions** - Context-appropriate allowed tools and operations

### Rule Enforcement Layers

#### Layer 1: Documentation (Human Reference)
- Markdown files in `/docs/rules/` provide comprehensive rule documentation
- Human-readable explanations with examples and rationale
- Referenced by slash commands for LLM context

#### Layer 2: Command Integration (LLM Guidance)
- Slash commands explicitly reference applicable rules
- Rules included in command context and checklists
- LLM guided to follow rule requirements

#### Layer 3: CLI Enforcement (Deterministic Logic)
- C# CLI commands implement critical business logic
- Automated validation of rule compliance
- Deterministic enforcement independent of LLM interpretation

### Rule Organization Structure

```
/docs/rules/
├── session-workflow.md          # Universal session management
├── task-management.md           # Universal GitHub workflow
├── git-workflow.md              # Universal Git standards
├── documentation-rules.md       # Universal documentation requirements
├── asset-registry.yaml          # Skills, tools, MCPs configuration
├── checklists/                  # Mode-specific requirements
│   ├── intake-checklist.md
│   ├── discover-checklist.md
│   ├── scope-checklist.md
│   └── [other modes...]
└── contexts/                    # Context-specific adaptations (future)
    ├── business-context.md
    ├── ml-engineering-context.md
    └── software-engineering-context.md
```

### CLI Integration Pattern

Critical rules implemented as C# commands:
```bash
# Rule validation and enforcement
agenticops rules validate --mode intake --context ml-engineering
agenticops rules enforce --rule session-startup --session-id current

# Context detection and configuration
agenticops context detect --issue-id 123 --labels "ml,data-science"
agenticops context configure --mode intake --context ml-engineering

# Artifact and template management
agenticops artifacts create --template ml-requirements --context detected
agenticops artifacts validate --artifact-path /docs/artifacts/intake/...

# Session and workflow management
agenticops session transition --from intake --to discover --validate-gates
agenticops workflow check --mode current --completion-status
```

## Consequences

### Positive
- **Consistency**: Deterministic rule enforcement across all modes and agents
- **Reliability**: Reduced risk of hallucination and inconsistent behavior
- **Maintainability**: Centralized rule management with clear organization
- **Validation**: Automated compliance checking and quality assurance
- **Scalability**: Framework supports adding new rules and contexts
- **Auditability**: Clear rule traceability and compliance reporting

### Negative
- **Complexity**: Additional layer of infrastructure to maintain
- **Development Overhead**: Rules must be implemented in both documentation and CLI
- **Rigidity**: May limit creative problem-solving in edge cases
- **CLI Dependency**: Critical functionality requires C# CLI implementation

### Neutral
- **Evolution Path**: Framework can evolve with changing requirements
- **Flexibility**: Rules can be updated without code changes (documentation layer)
- **Context Adaptation**: System can expand to new work contexts and domains

## Rationale

The rules system framework provides several key benefits:

1. **Deterministic Behavior**: CLI enforcement ensures consistent rule application regardless of LLM state
2. **Quality Assurance**: Systematic validation enables reliable quality gates and compliance checking
3. **Maintainability**: Centralized rule storage simplifies updates and reduces duplication
4. **Scalability**: Framework supports expansion to new modes, contexts, and rule types
5. **Developer Experience**: Clear rule documentation and automated enforcement improves productivity

## Implementation Details

### Rule Documentation Standards
- **Clear Structure**: Consistent format across all rule files
- **Actionable Content**: Specific requirements with clear success criteria
- **TodoWrite Integration**: Rules include TodoWrite templates for task tracking
- **Context References**: Rules clearly specify when and how they apply

### CLI Integration Requirements
- **Rule Validation**: Every rule must have corresponding validation logic
- **Context Awareness**: CLI commands adapt behavior based on detected context
- **Error Reporting**: Clear error messages and remediation guidance
- **Integration Points**: Seamless integration with existing workflows

### Quality Gates
- **Rule Compliance**: All modes must pass rule validation before transitions
- **Artifact Validation**: All outputs must meet rule-defined quality standards
- **Process Adherence**: Workflow steps must follow rule-defined sequences
- **Documentation Updates**: Rule changes must update all affected components

## Migration Strategy

### Phase 1: Documentation Consolidation
- Audit existing rules scattered across documentation
- Consolidate into standardized `/docs/rules/` structure
- Update slash commands to reference centralized rules

### Phase 2: CLI Implementation
- Implement critical business logic in C# CLI commands
- Create rule validation and enforcement capabilities
- Integrate CLI commands with existing workflows

### Phase 3: Advanced Features
- Add context-specific rule adaptations
- Implement automated compliance reporting
- Create rule analytics and optimization capabilities

## Related Decisions
- [ADR-0001: Adopt AgenticOps Value Train™ Methodology](adr-0001-adopt-agenticops-value-train.md)
- [ADR-0004: Adopt Session-Based Context Management](adr-0004-adopt-session-based-context-management.md)
- [ADR-0016: Secure Command Line Tool](adr-0016-secure-command-line-tool.md)
- [ADR-0020: Template-Based Artifact Standardization](adr-0020-template-based-artifact-standardization.md)

## References
- [Session Workflow Rules](../../rules/session-workflow.md)
- [Task Management Rules](../../rules/task-management.md)
- [Git Workflow Rules](../../rules/git-workflow.md)
- [Documentation Rules](../../rules/documentation-rules.md)
- [Value Train Pipeline Guide](../../user-guides/value-train-pipeline.md)