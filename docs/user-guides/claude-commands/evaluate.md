# /evaluate Command User Guide

## Overview

The `/evaluate` command switches Claude into **Evaluate Mode** as the **Evaluator Agent**. This mode specializes in comprehensive evaluation, validation, and quality assurance of trained models, business solutions, and system implementations against defined success criteria.

## When to Use

Use `/evaluate` when you need to:
- Conduct formal validation of trained models or implemented solutions
- Assess solution performance against business requirements
- Perform comprehensive quality assurance and testing
- Validate stakeholder acceptance and user satisfaction
- Generate evaluation reports and improvement recommendations

## Prerequisites

Before running `/evaluate`, ensure:
- Solution has been implemented (via `/train` or other implementation modes)
- Success criteria and evaluation metrics are clearly defined
- Test data and validation environments are available
- Stakeholders are available for validation sessions

## Command Behavior

When you invoke `/evaluate`, Claude will:

1. **Switch to Evaluate Mode** - Activate Evaluator Agent role specialized in validation
2. **Display Status** - Show current PRD/CRD, branch, and session context
3. **Read Context Files** - Load all rule and session files for clean boundaries
4. **Create TodoWrite Checklist** - Generate structured task list for comprehensive evaluation
5. **Context Adaptation** - Adapt approach based on project type:
   - **Business Context**: Business value validation and ROI assessment
   - **ML Engineering Context**: Model performance and generalization validation
   - **Software Engineering Context**: System performance and reliability assessment

## Context-Specific Outputs

### Business Context
- **Business Evaluation Report** with ROI and stakeholder validation
- Business value assessment and KPI validation
- User acceptance testing and stakeholder sign-off
- Business process integration and change management impact analysis

### ML Engineering Context
- **ML Evaluation Report** with model performance and validation metrics
- Model accuracy, bias, and fairness assessment
- Robustness testing and interpretability validation
- Production readiness and deployment requirement verification

### Software Engineering Context
- **Technical Evaluation Report** with system quality and performance metrics
- Comprehensive testing including unit, integration, and system tests
- Code quality, security, and architectural compliance assessment
- Scalability, performance, and operational readiness validation

## Evaluation Framework

The command follows a comprehensive evaluation framework:

### Comprehensive Assessment Strategy
- Success criteria validation against original objectives
- Performance benchmarking against baselines and industry standards
- Quality assurance across all relevant solution dimensions
- Risk assessment with mitigation strategy identification
- Stakeholder validation and expectation verification

### Testing and Validation
- Functional testing to verify requirement compliance
- Performance testing under various load and stress conditions
- Security testing for vulnerabilities and compliance
- Usability testing for user experience effectiveness
- Integration testing with existing systems and processes

### Quality Metrics and Analysis
- Quantitative metrics for objective performance indicators
- Qualitative assessment of subjective aspects like usability
- Comparative analysis against alternatives and benchmarks
- Trend analysis for performance stability over time
- Impact assessment for overall value delivery

## Exit Criteria

The command will not exit until:
- All required checklist items are complete
- Comprehensive evaluation completed across all critical dimensions
- Solution validated against all success criteria and requirements
- Evaluation results documented with clear findings and recommendations
- Stakeholder validation completed with sign-off where required
- Risk assessment completed with mitigation strategies identified
- Session context updated with evaluation results and decisions

## Common Use Cases

### ML Model Validation
```
You: /evaluate
Claude: [Switches to Evaluate Mode, analyzes trained model]
Claude: [Conducts performance testing, bias assessment, validates against test data, generates ML evaluation report]
```

### Business Solution Assessment
```
You: /evaluate
Claude: [Switches to Evaluate Mode, reviews business implementation]
Claude: [Performs ROI analysis, user acceptance testing, stakeholder validation, creates business evaluation report]
```

### System Quality Assurance
```
You: /evaluate
Claude: [Switches to Evaluate Mode, examines system implementation]
Claude: [Executes comprehensive testing, security assessment, performance validation, produces technical evaluation report]
```

## Best Practices

### Before Evaluation
- Ensure all success criteria and metrics are clearly defined
- Prepare representative test data and validation environments
- Schedule stakeholder availability for validation sessions
- Plan comprehensive evaluation coverage across all requirements

### During Evaluation
- Maintain objective and evidence-based assessment approaches
- Document all findings, issues, and recommendations thoroughly
- Involve stakeholders in validation processes appropriately
- Test edge cases and stress conditions comprehensively

### After Evaluation
- Generate clear, actionable recommendations for improvements
- Communicate evaluation results to all relevant stakeholders
- Update project documentation with evaluation findings
- Plan next steps based on evaluation outcomes

## Common Evaluation Patterns

### Model Evaluation
- **Performance Metrics**: Accuracy, precision, recall, F1-score, AUC-ROC
- **Bias Assessment**: Fairness validation across demographic groups
- **Robustness Testing**: Performance under adversarial conditions
- **Interpretability**: Model explanation and decision transparency

### Business Solution Evaluation
- **ROI Analysis**: Return on investment and cost-benefit assessment
- **User Acceptance**: Stakeholder satisfaction and adoption readiness
- **Process Impact**: Integration with existing business processes
- **Change Management**: Organizational readiness and change impact

### System Evaluation
- **Performance Testing**: Load, stress, and scalability testing
- **Security Assessment**: Vulnerability scanning and penetration testing
- **Reliability Testing**: Availability, fault tolerance, and recovery testing
- **Maintainability**: Code quality, documentation, and support readiness

### Data Quality Evaluation
- **Accuracy Assessment**: Data correctness and validity verification
- **Completeness Testing**: Missing data and coverage analysis
- **Consistency Validation**: Data consistency across sources and time
- **Timeliness Evaluation**: Data freshness and update frequency

## Integration with Other Commands

**Prerequisites:**
- `/train` - Provides trained models for evaluation
- `/features` - Provides feature engineering for data quality assessment
- `/design` - Defines evaluation criteria and success metrics

**Next Steps:**
- `/deliver` - Proceed to delivery if evaluation passes (recommended)
- `/improve` - Address identified issues and optimization opportunities
- `/train` - Return to training if model performance issues identified
- `/features` - Return to feature engineering if data quality issues found

## Troubleshooting

### Evaluation Setup Issues
- Verify test data availability and quality
- Check evaluation environment configuration
- Validate success criteria and metric definitions
- Ensure stakeholder availability for validation

### Performance Validation Problems
- Review baseline and benchmark definitions
- Check test data representativeness
- Validate performance measurement approaches
- Analyze performance variation and consistency

### Stakeholder Validation Challenges
- Clarify stakeholder expectations and requirements
- Schedule appropriate validation sessions
- Provide clear documentation and demonstrations
- Address stakeholder concerns and feedback

## Quality Assurance Framework

### Performance Validation
- Meet all defined performance criteria and benchmarks
- Demonstrate consistent metrics across test scenarios
- Validate under realistic production conditions
- Ensure stable and sustainable performance trends

### Functional Completeness
- Fulfill all functional requirements and specifications
- Validate all user stories and acceptance criteria
- Handle edge cases and error conditions properly
- Confirm solution completeness for production use

### Quality Standards
- Meet all quality standards and best practices
- Verify security, privacy, and compliance requirements
- Ensure maintainability, scalability, and operational readiness
- Satisfy all quality gates and checkpoints

### Stakeholder Satisfaction
- Validate solution meets stakeholder needs
- Confirm satisfactory user experience and interface effectiveness
- Deliver expected business value and ROI
- Gain stakeholder confidence for deployment readiness

## Risk Assessment

### Technical Risks
- Identify performance bottlenecks and scalability issues
- Assess security vulnerabilities and compliance gaps
- Evaluate technical debt and maintainability concerns
- Analyze integration and dependency risks

### Business Risks
- Assess business value delivery and ROI realization
- Evaluate user adoption and change management risks
- Identify process integration and operational challenges
- Analyze market and competitive risks

### Operational Risks
- Evaluate deployment and rollout risks
- Assess monitoring and support requirements
- Identify disaster recovery and business continuity needs
- Analyze resource and skill requirements

## Reporting and Documentation

### Evaluation Reports
- Comprehensive findings and assessment results
- Clear recommendations and improvement suggestions
- Risk analysis and mitigation strategies
- Stakeholder feedback and validation results

### Quality Metrics
- Quantitative performance indicators and benchmarks
- Qualitative assessment summaries
- Trend analysis and stability measurements
- Comparative analysis results

### Stakeholder Communication
- Executive summaries for leadership
- Technical details for implementation teams
- User-focused documentation for end users
- Training and support materials

## Related Commands

- `/train` - Model training and optimization
- `/design` - Solution architecture and evaluation criteria
- `/deliver` - Solution delivery and deployment
- `/improve` - Solution optimization and enhancement

## Support

For issues with the `/evaluate` command:
1. Check this user guide for common solutions
2. Review the [developer guide](../developer-guides/claude-commands/extending-commands.md) for technical details
3. Validate evaluation criteria and success metrics are well-defined
4. Ensure test data and validation environments are properly configured