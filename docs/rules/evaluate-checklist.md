# Evaluate Mode Checklist

## Mode Configuration
- **Mode**: evaluate
- **Description**: Formal validation against metrics and business KPIs
- **Primary Agent**: evaluator
- **Allowed Tools**: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), Bash(python:*), Bash(test:*)

## Entry Criteria
- [ ] Model training pipeline completed
- [ ] Initial model artifacts available
- [ ] Test datasets prepared and validated
- [ ] Success criteria and metrics defined

## Core Activities Checklist

### Model Performance Evaluation
- [ ] Execute comprehensive model testing suite
- [ ] Evaluate model accuracy and precision metrics
- [ ] Test model robustness and stability
- [ ] Validate model performance across data segments
- [ ] Compare model performance to baseline approaches

### Business Impact Assessment
- [ ] Measure alignment with business objectives
- [ ] Calculate ROI and business value metrics
- [ ] Assess user experience and usability
- [ ] Evaluate operational impact and efficiency gains
- [ ] Document business case validation

### Technical Validation
- [ ] Validate model inference performance and latency
- [ ] Test scalability and resource utilization
- [ ] Evaluate model interpretability and explainability
- [ ] Test model security and privacy compliance
- [ ] Validate integration and API performance

### Quality Assurance
- [ ] Execute comprehensive regression testing
- [ ] Validate data quality and pipeline integrity
- [ ] Test error handling and edge cases
- [ ] Evaluate monitoring and alerting systems
- [ ] Document quality metrics and thresholds

### Risk Assessment
- [ ] Evaluate model bias and fairness
- [ ] Assess model drift and degradation risks
- [ ] Test model robustness to adversarial inputs
- [ ] Validate security and privacy measures
- [ ] Document risk mitigation strategies

## Deliverables
- [ ] `eval-results.pdf` - Comprehensive evaluation report
- [ ] `validation-report.md` - Technical validation summary
- [ ] Model performance benchmarks
- [ ] Business impact assessment
- [ ] Risk analysis and mitigation plan

## Exit Criteria
- [ ] Model performance meets all success criteria
- [ ] Business objectives validated and documented
- [ ] Technical requirements satisfied
- [ ] Quality gates passed
- [ ] Risk assessment completed and acceptable

## Quality Gates
- [ ] Model accuracy exceeds baseline by defined margin
- [ ] Business KPIs show measurable improvement
- [ ] Technical performance meets latency/throughput requirements
- [ ] Security and compliance requirements satisfied
- [ ] Model interpretability meets stakeholder needs

## Transition Rules
- **Proceed**: Move to `deliver` mode for deployment
- **Iterate**: Return to `build` mode for improvements
- **Pivot**: Return to `design` mode for architecture changes

## Common Pitfalls
- Insufficient test coverage across data segments
- Over-optimizing for accuracy at expense of business value
- Missing bias and fairness evaluation
- Inadequate performance and scalability testing
- Poor documentation of evaluation methodology

## Mode-Specific Tools
- Model evaluation and testing frameworks
- Statistical analysis and visualization tools
- Performance benchmarking and profiling tools
- Bias detection and fairness assessment tools
- Business impact measurement frameworks