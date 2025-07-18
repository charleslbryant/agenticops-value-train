# Design Mode Checklist

## Mode Configuration
- **Mode**: design
- **Description**: Architect data flow, feature plan, model approach
- **Primary Agents**: studio, lab
- **Allowed Tools**: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), Bash(python:*)

## Entry Criteria
- [ ] MVP scope and requirements defined
- [ ] Technical architecture approved
- [ ] Data sources and access confirmed
- [ ] Project team and resources allocated

## Core Activities Checklist

### Data Architecture
- [ ] Design data ingestion and extraction pipelines
- [ ] Define data storage and processing architecture
- [ ] Plan data validation and quality checks
- [ ] Design data transformation and feature engineering
- [ ] Document data lineage and governance

### Model Design
- [ ] Select appropriate ML algorithms and techniques
- [ ] Design model architecture and hyperparameters
- [ ] Plan model training and validation strategy
- [ ] Define model evaluation metrics and thresholds
- [ ] Design model versioning and artifact management

### System Architecture
- [ ] Design inference and prediction pipeline
- [ ] Plan API and integration architecture
- [ ] Define monitoring and alerting systems
- [ ] Design scalability and performance architecture
- [ ] Plan security and access control

### Feature Engineering
- [ ] Identify and design input features
- [ ] Plan feature extraction and transformation
- [ ] Design feature selection and validation
- [ ] Plan feature store and management
- [ ] Document feature engineering pipeline

### Infrastructure Design
- [ ] Design cloud and compute infrastructure
- [ ] Plan development and deployment environments
- [ ] Design backup and disaster recovery
- [ ] Plan cost optimization and resource management
- [ ] Design CI/CD and automation pipelines

## Deliverables
- [ ] `source-map.md` - Data source mapping and access plan
- [ ] `data-access-plan.md` - Detailed data access strategy
- [ ] Technical architecture diagrams
- [ ] Model design specifications
- [ ] Infrastructure deployment plans

## Exit Criteria
- [ ] Data architecture designed and validated
- [ ] Model approach selected and documented
- [ ] System architecture approved by stakeholders
- [ ] Infrastructure plan cost-optimized
- [ ] Implementation plan detailed and resourced

## Quality Gates
- [ ] Data architecture supports all use case requirements
- [ ] Model approach is appropriate for problem and data
- [ ] System architecture is scalable and maintainable
- [ ] Infrastructure plan is cost-effective
- [ ] Security and compliance requirements addressed

## Transition Rules
- **Proceed**: Move to `build` mode for implementation
- **Revise**: Return to `scope` for architecture changes
- **Validate**: Prototype critical components before building

## Common Pitfalls
- Over-engineering architecture for MVP scope
- Selecting inappropriate ML approaches
- Underestimating data pipeline complexity
- Missing performance and scalability requirements
- Inadequate security and compliance planning

## Mode-Specific Tools
- Data architecture design tools
- ML model selection frameworks
- System architecture diagramming
- Infrastructure as code templates
- Feature engineering libraries