# /scope Command User Guide

## Overview

The `/scope` command switches Claude into **Scope Mode** as the **Conductor Agent**. This mode synthesizes requirements and discovery findings into a concrete technical approach, timeline, and deliverable plan.

## When to Use

Use `/scope` when you need to:
- Define technical approach based on validated requirements
- Create implementation timeline and resource plan
- Break down complex solutions into manageable phases
- Plan risk mitigation strategies
- Establish success criteria and quality gates

## Prerequisites

Before running `/scope`, ensure:
- Requirements have been gathered using `/intake`
- Discovery has been completed using `/discover`
- Key constraints and feasibility have been validated
- Stakeholder alignment on high-level approach exists

## Command Behavior

When you invoke `/scope`, Claude will:

1. **Switch to Scope Mode** - Activate Conductor Agent role
2. **Display Status** - Show current PRD/CRD, branch, and session context
3. **Read Context Files** - Load all rule and session files for clean boundaries
4. **Create TodoWrite Checklist** - Generate structured task list for scope planning
5. **Context Adaptation** - Adapt approach based on project type:
   - **Business Context**: Strategic implementation and go-to-market planning
   - **ML Engineering Context**: ML pipeline architecture and model development
   - **Software Engineering Context**: System architecture and development methodology

## Context-Specific Outputs

### Business Context
- **Business Scope Document** with strategic implementation plan
- Go-to-market strategy and business process changes
- Stakeholder communication and change management approach
- Business case validation and success measurement plan

### ML Engineering Context
- **ML Scope Document** with technical ML implementation plan
- ML pipeline architecture and model development approach
- Data preparation, training, and deployment strategy
- MLOps and monitoring implementation plan

### Software Engineering Context
- **Technical Scope Document** with software development plan
- System architecture and development methodology
- Technology stack, integration, and deployment strategy
- DevOps and operational implementation plan

## Scope Planning Framework

The command follows a comprehensive planning framework:

### Solution Architecture Definition
- Technology selection and framework choices
- System design and component interactions
- Integration strategy with existing systems
- Scalability and performance considerations
- Security requirements and implementation

### Implementation Strategy
- Development methodology (Agile, waterfall, hybrid)
- Phase planning with logical work grouping
- Risk management with specific mitigation plans
- Quality assurance and testing strategy
- Deployment and rollout approach

### Resource and Timeline Planning
- Team composition and required skills
- Realistic timeline development with buffers
- Dependency management and critical path analysis
- Budget planning and resource allocation
- Success metrics and measurable outcomes

## Exit Criteria

The command will not exit until:
- All required checklist items are complete
- Scope document created with comprehensive plan
- Technical approach validated and stakeholder-approved
- Timeline and resource plan are realistic and achievable
- Risk mitigation strategies defined for major risks
- Success criteria and quality gates clearly defined
- Session context updated with scope decisions

## Common Use Cases

### Software Development Project
```
You: /scope
Claude: [Switches to Scope Mode, analyzes requirements from /intake and discovery from /discover]
Claude: [Creates technical scope document with system architecture, development phases, and deployment strategy]
```

### ML Model Development
```
You: /scope
Claude: [Switches to Scope Mode, reviews ML requirements and data discovery findings]
Claude: [Creates ML scope document with pipeline architecture, model approach, and MLOps strategy]
```

### Business Process Implementation
```
You: /scope
Claude: [Switches to Scope Mode, synthesizes business requirements and operational constraints]
Claude: [Creates business scope document with implementation strategy and change management plan]
```

## Best Practices

### Before Scoping
- Ensure requirements are well-defined and validated
- Complete thorough discovery of constraints and feasibility
- Validate key assumptions with stakeholders
- Gather all necessary technical and business context

### During Scoping
- Be realistic about timelines and resource requirements
- Account for identified risks with specific mitigation plans
- Validate critical decisions with stakeholders
- Document all assumptions and decision rationale

### After Scoping
- Review scope document with all stakeholders
- Validate technical approach with technical teams
- Confirm resource availability and timeline feasibility
- Update session context with scope decisions

## Integration with Other Commands

**Prerequisites:**
- `/intake` - Gathers requirements and context
- `/discover` - Validates feasibility and constraints

**Next Steps:**
- `/design` - Create detailed technical design (recommended)
- `/discover` - Return if scope reveals major gaps
- `/intake` - Return if fundamental changes needed

## Troubleshooting

### Command Not Working
- Verify you have the latest Claude commands
- Check that session context files exist
- Ensure proper rule files are in place

### Incomplete Scope Planning
- Review all requirements from intake phase
- Validate discovery findings are comprehensive
- Check that all stakeholders have provided input
- Ensure technical constraints are well understood

### Stakeholder Misalignment
- Return to `/discover` for additional validation
- Schedule stakeholder alignment sessions
- Document and resolve conflicting requirements
- Escalate decisions to appropriate authority

## Related Commands

- `/intake` - Requirements gathering and context understanding
- `/discover` - Deep discovery of constraints and feasibility
- `/design` - Detailed technical design and architecture
- `/build` - Implementation phase commands (extract, features, train)

## Support

For issues with the `/scope` command:
1. Check this user guide for common solutions
2. Review the [developer guide](../developer-guides/claude-commands/extending-commands.md) for technical details
3. Ensure all prerequisite files and context exist
4. Validate that previous mode requirements are complete