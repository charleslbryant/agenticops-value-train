# Build Mode Checklist

## Mode Configuration
- **Mode**: build
- **Description**: Extract data, engineer features, train models
- **Primary Agents**: lab, studio
- **Allowed Tools**: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), Bash(python:*), Bash(test:*)

## Entry Criteria
- [ ] Data architecture and model design approved
- [ ] Infrastructure and development environment ready
- [ ] Data access and permissions configured
- [ ] Feature engineering plan documented

## Core Activities Checklist

### Data Extraction and Processing
- [ ] Implement data extraction scripts and pipelines
- [ ] Build data validation and quality checks
- [ ] Create data transformation and cleaning processes
- [ ] Implement data partitioning and sampling
- [ ] Build data monitoring and alerting

### Feature Engineering
- [ ] Implement feature extraction and transformation
- [ ] Build feature validation and selection
- [ ] Create feature store and management system
- [ ] Implement feature pipeline testing
- [ ] Document feature engineering processes

### Model Development
- [ ] Implement model training pipeline
- [ ] Build hyperparameter tuning and optimization
- [ ] Create model validation and testing
- [ ] Implement model versioning and artifact management
- [ ] Build model performance monitoring

### Testing and Validation
- [ ] Create unit tests for all pipeline components
- [ ] Implement integration tests for data flows
- [ ] Build model validation and testing frameworks
- [ ] Create performance and load testing
- [ ] Implement security and compliance testing

### Documentation and Logging
- [ ] Document all code and pipeline components
- [ ] Implement comprehensive logging and monitoring
- [ ] Create troubleshooting and debugging guides
- [ ] Build performance and metrics dashboards
- [ ] Document deployment and operations procedures

## Deliverables
- [ ] `extract.py` - Data extraction pipeline
- [ ] `extraction-log.md` - Extraction process documentation
- [ ] `prepared.csv` - Processed and cleaned dataset
- [ ] `schema-spec.md` - Data schema specification
- [ ] `profile.ipynb` - Data profiling and analysis
- [ ] `profile-report.md` - Data profiling summary
- [ ] `feature-map.md` - Feature engineering documentation
- [ ] `feature-config.yaml` - Feature pipeline configuration
- [ ] `train.ipynb` - Model training pipeline
- [ ] `mlflow-runs.md` - Training experiment logs

## Exit Criteria
- [ ] Data pipeline fully implemented and tested
- [ ] Feature engineering pipeline validated
- [ ] Model training pipeline producing valid results
- [ ] All tests passing and code quality metrics met
- [ ] Performance benchmarks achieved

## Quality Gates
- [ ] Data quality meets requirements and thresholds
- [ ] Feature engineering produces expected results
- [ ] Model training is reproducible and stable
- [ ] Code coverage and quality standards met
- [ ] Performance and scalability requirements satisfied

## Transition Rules
- **Proceed**: Move to `evaluate` mode for formal validation
- **Iterate**: Continue building with additional features or improvements
- **Debug**: Address quality or performance issues before evaluation

## Common Pitfalls
- Insufficient data validation and quality checks
- Over-engineering feature pipelines for MVP
- Inadequate testing and error handling
- Missing performance and scalability considerations
- Poor documentation and code maintainability

## Mode-Specific Tools
- Data processing and ETL frameworks
- Feature engineering and ML libraries
- Model training and experiment tracking
- Testing and validation frameworks
- Code quality and documentation tools