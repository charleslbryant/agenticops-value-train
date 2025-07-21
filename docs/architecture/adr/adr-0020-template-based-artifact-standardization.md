# ADR-0020: Template-Based Artifact Standardization

## Status
**Accepted**

## Context
Value Train agents need to produce consistent, high-quality artifacts across different contexts (business, ML engineering, and software engineering). Without standardization, artifacts vary in structure, completeness, and quality, making it difficult to evaluate work quality and ensure systematic handoffs between agents.

Current challenges include:
- **Inconsistent Format**: Agents create artifacts with different structures and levels of detail
- **Quality Variance**: No standard for evaluating artifact completeness or adherence to best practices  
- **Context Adaptation**: Need artifacts to adapt to business, ML engineering, and software engineering contexts while maintaining consistency
- **Domain Specificity**: ML and software engineering have fundamentally different requirements structures
- **Evaluation Difficulty**: No systematic way to assess artifact quality for handoffs

## Decision
We will implement a template-based artifact standardization system where:

1. **Standardized Templates**: All artifact types have corresponding templates in `/docs/templates/`
2. **Context-Specific Templates**: Three distinct templates for different work contexts:
   - **Business Context**: Opportunity Brief for strategic analysis
   - **ML Engineering Context**: ML Requirements Document for machine learning projects
   - **Software Engineering Context**: Requirements Document for traditional software development
3. **Structured Placeholders**: Templates include clear placeholder text and directional comments
4. **Quality Evaluation**: Artifacts evaluated against template completeness and adherence
5. **Agent Integration**: Commands explicitly reference and enforce template usage

## Architecture

### Template Structure
```
/docs/templates/
├── opportunity-brief.md          # Business context artifacts
├── requirements-document.md      # Software engineering context artifacts
├── ml-requirements-document.md   # ML engineering context artifacts
├── [future templates...]
```

### Template Format Standards
- **Placeholder Text**: `[Replace with specific content]` format for clear replacement guidance
- **Directional Comments**: `<!-- Instructions for this section -->` to guide completion
- **Section Structure**: Consistent headings and organization across all templates
- **Metadata Footer**: Standard metadata (agent name, date, status) on all artifacts

### Command Integration
- Commands detect context type (business, ML engineering, or software engineering)
- Commands reference specific templates in checklists based on detected context
- Commands include template usage instructions for all three context types
- Commands enforce artifact completion before mode transitions

### Quality Evaluation Framework
- **Completeness**: All template sections addressed
- **Adherence**: Proper use of template structure and format
- **Placeholder Replacement**: All placeholders replaced with actual content
- **Direction Removal**: Template directions and comments removed from final artifact

## Consequences

### Positive
- **Consistency**: Standardized artifact structure across all agents and contexts
- **Quality Assurance**: Clear criteria for evaluating artifact completeness and quality
- **Handoff Reliability**: Consistent format enables smooth agent-to-agent handoffs
- **Context Adaptation**: Different templates allow specialization while maintaining standards
- **Training Efficiency**: Templates serve as training aids for agent behavior
- **Evaluation Automation**: Systematic evaluation enables quality automation

### Negative
- **Template Maintenance**: Templates require ongoing maintenance and updates
- **Rigidity**: Structured approach may limit creative or novel formatting
- **Initial Overhead**: Agents must learn and follow template requirements
- **Template Proliferation**: Risk of creating too many specialized templates

### Neutral
- **Context Flexibility**: Templates can be adapted for different domains and use cases
- **Evolution Path**: Template system can evolve with changing requirements

## Rationale
Template-based standardization provides several key benefits:

1. **Quality Consistency**: Ensures all artifacts meet minimum standards regardless of agent or context
2. **Evaluation Framework**: Enables systematic quality assessment for agent handoffs
3. **Context Adaptation**: Allows specialization for business vs. engineering while maintaining consistency
4. **Knowledge Capture**: Templates encode organizational knowledge and best practices
5. **Scalability**: Standardized approach scales across multiple agents and work types

## Implementation Details

### Template Creation Process
1. Identify artifact types needed across Value Train workflows
2. Create templates with comprehensive section structure
3. Include clear placeholder text and directional comments
4. Add metadata standards and formatting requirements
5. Integrate template references into relevant commands

### Agent Training Integration
- Commands explicitly reference templates in checklists
- Template usage instructions provided in command documentation
- Quality evaluation criteria clearly communicated
- Examples and best practices documented

### Quality Gates
- Artifact completeness checked against template structure
- Placeholder replacement validation
- Template adherence assessment
- Handoff quality evaluation based on template standards

## Related Decisions
- [ADR-0001: Adopt AgenticOps Value Train™ Methodology](adr-0001-adopt-agenticops-value-train.md)
- [ADR-0004: Adopt Session-Based Context Management](adr-0004-adopt-session-based-context-management.md)

## References
- [Value Train Pipeline Guide](../../user-guides/value-train-pipeline.md)
- [Opportunity Brief Template](../templates/opportunity-brief.md)
- [Requirements Document Template](../templates/requirements-document.md)
- [ML Requirements Document Template](../templates/ml-requirements-document.md)