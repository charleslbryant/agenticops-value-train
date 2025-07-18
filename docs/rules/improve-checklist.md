# Improve Mode Checklist

## Mode Configuration
- **Mode**: improve
- **Description**: Root-cause analysis, retraining, roadmap updates
- **Primary Agents**: improver, lab
- **Allowed Tools**: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), Bash(python:*), Bash(test:*)

## Entry Criteria
- [ ] Model operating in production with monitoring data
- [ ] Performance metrics and trends available
- [ ] Improvement opportunities identified
- [ ] Business case for improvement validated

## Core Activities Checklist

### Performance Analysis
- [ ] Analyze model performance trends and degradation
- [ ] Identify root causes of performance issues
- [ ] Evaluate impact of data drift and distribution changes
- [ ] Assess feature importance and model behavior
- [ ] Analyze user feedback and business impact

### Improvement Planning
- [ ] Prioritize improvement opportunities by impact
- [ ] Design experiments and A/B testing strategies
- [ ] Plan data collection and annotation improvements
- [ ] Design feature engineering and model enhancements
- [ ] Create improvement roadmap and timeline

### Data Enhancement
- [ ] Collect additional training data and samples
- [ ] Improve data quality and labeling processes
- [ ] Enhance feature engineering and selection
- [ ] Optimize data preprocessing and augmentation
- [ ] Implement active learning and data collection

### Model Optimization
- [ ] Retrain models with updated data and features
- [ ] Optimize hyperparameters and architecture
- [ ] Implement ensemble methods and model stacking
- [ ] Optimize model inference and performance
- [ ] Validate improvements against baselines

### System Enhancement
- [ ] Optimize infrastructure and deployment pipeline
- [ ] Improve monitoring and alerting systems
- [ ] Enhance user experience and interface
- [ ] Optimize cost and resource utilization
- [ ] Implement automation and workflow improvements

## Deliverables
- [ ] `improvement-roadmap.md` - Prioritized improvement plan
- [ ] `retraining-plan.md` - Model retraining strategy
- [ ] `retrain.ipynb` - Updated model training pipeline
- [ ] `performance-comparison.md` - Before/after analysis
- [ ] Enhanced model artifacts and documentation

## Exit Criteria
- [ ] Improvements implemented and validated
- [ ] Model performance enhanced measurably
- [ ] Business value and ROI demonstrated
- [ ] System reliability and efficiency improved
- [ ] Improvement roadmap updated for next iteration

## Quality Gates
- [ ] Model improvements exceed minimum performance thresholds
- [ ] Business metrics show measurable improvement
- [ ] System reliability and uptime maintained or improved
- [ ] Cost optimization targets achieved
- [ ] User satisfaction and adoption improved

## Transition Rules
- **Continue**: Ongoing improvement with regular optimization cycles
- **Operate**: Return to `operate` mode for stable operations
- **Retrain**: Move to `build` mode for major model changes

## Common Pitfalls
- Optimizing for metrics without business impact
- Over-engineering improvements without clear ROI
- Insufficient A/B testing and validation
- Poor change management and rollback procedures
- Missing stakeholder communication and alignment

## Mode-Specific Tools
- Experiment tracking and A/B testing platforms
- Model retraining and optimization frameworks
- Performance analysis and visualization tools
- Data collection and annotation tools
- Continuous improvement and DevOps tools