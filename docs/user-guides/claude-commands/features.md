# /features Command User Guide

## Overview

The `/features` command switches Claude into **Features Mode** as the **Lab Agent**. This mode specializes in feature engineering, data transformation, and feature store management, creating optimized features for model training or business analysis from extracted data.

## When to Use

Use `/features` when you need to:
- Transform raw extracted data into meaningful features
- Create feature engineering pipelines and transformations
- Build feature stores with versioning and management
- Implement feature quality validation and monitoring
- Prepare features for model training or business analysis

## Prerequisites

Before running `/features`, ensure:
- Data extraction has been completed using `/extract`
- Raw data is accessible and validated
- Feature requirements are understood from design phase
- Target objectives for features are clearly defined

## Command Behavior

When you invoke `/features`, Claude will:

1. **Switch to Features Mode** - Activate Lab Agent role specialized in feature engineering
2. **Display Status** - Show current PRD/CRD, branch, and session context
3. **Read Context Files** - Load all rule and session files for clean boundaries
4. **Create TodoWrite Checklist** - Generate structured task list for feature engineering
5. **Context Adaptation** - Adapt approach based on project type:
   - **Business Context**: Business metrics and KPI derivation
   - **ML Engineering Context**: Predictive features and model-ready datasets
   - **Software Engineering Context**: Application features and system metrics

## Context-Specific Outputs

### Business Context
- **Business Features** with KPIs and business intelligence metrics
- Customer segmentation and behavioral feature creation
- Business metrics derivation and reporting features
- Features aligned with business decision-making needs

### ML Engineering Context
- **ML Features** with model-ready training datasets
- Advanced feature engineering with predictive power
- Training, validation, and test feature set creation
- Features optimized for model performance and generalization

### Software Engineering Context
- **System Features** with operational metrics and indicators
- Application monitoring and alerting feature creation
- Performance and health indicator derivation
- Features supporting operational decision-making

## Feature Engineering Framework

The command follows a comprehensive feature engineering framework:

### Feature Discovery and Design
- Requirements analysis mapping objectives to feature needs
- Data exploration for feature engineering opportunities
- Feature ideation and prioritization processes
- Feature selection based on relevance and feasibility
- Transformation design and architecture planning

### Feature Implementation
- Robust, reusable feature transformation function development
- Scalable feature processing pipeline architecture
- Comprehensive feature quality validation implementation
- Error handling and data validation systems
- Performance optimization for speed and resource efficiency

### Feature Management
- Centralized feature store setup with versioning
- Searchable feature catalog with comprehensive metadata
- Feature versioning and lineage tracking systems
- Access control and usage policy implementation
- Feature drift detection and quality monitoring

## Exit Criteria

The command will not exit until:
- All required checklist items are complete
- Feature engineering pipeline implemented and tested
- Feature quality validated and documented
- Feature store operational with proper versioning
- Feature catalog complete with comprehensive documentation
- Feature monitoring and drift detection operational
- Session context updated with feature engineering results

## Common Use Cases

### Business Intelligence Features
```
You: /features
Claude: [Switches to Features Mode, analyzes business data]
Claude: [Creates KPI features, customer segments, and business metrics for reporting and analysis]
```

### ML Model Features
```
You: /features
Claude: [Switches to Features Mode, reviews ML requirements]
Claude: [Engineers predictive features, handles categorical encoding, creates time-series features for model training]
```

### System Monitoring Features
```
You: /features
Claude: [Switches to Features Mode, examines system data]
Claude: [Derives performance metrics, health indicators, and alerting features for operational monitoring]
```

## Best Practices

### Before Feature Engineering
- Understand the target objectives and success criteria
- Analyze raw data distributions and quality
- Identify relevant domain knowledge and business rules
- Plan feature validation and quality metrics

### During Feature Engineering
- Focus on features that align with objectives
- Implement robust error handling and validation
- Document feature business context and rationale
- Test features with edge cases and data variations

### After Feature Engineering
- Validate feature quality and distributions
- Document feature catalog with comprehensive metadata
- Setup monitoring for feature drift and quality
- Prepare features for downstream consumption

## Common Feature Engineering Patterns

### Numerical Features
- **Scaling and Normalization**: Standardize numerical ranges for model compatibility
- **Binning and Discretization**: Convert continuous variables to meaningful categories
- **Mathematical Transformations**: Apply log, square root, or polynomial transformations
- **Statistical Aggregations**: Create moving averages, percentiles, and ratio features

### Categorical Features
- **Encoding Strategies**: Implement one-hot, label, or target encoding approaches
- **Frequency Features**: Generate count, frequency, and rare category handling
- **Categorical Combinations**: Create cross-features and interaction terms
- **Hierarchical Features**: Encode parent-child relationship structures

### Temporal Features
- **Time-Based Features**: Extract hour, day, month, season information
- **Lag Features**: Create historical values and time-based differences
- **Rolling Statistics**: Generate moving averages and rolling statistical measures
- **Trend Features**: Calculate growth rates and seasonal decomposition

### Text Features
- **Text Statistics**: Extract length, word count, and character distributions
- **NLP Features**: Generate TF-IDF, embeddings, and sentiment scores
- **Keyword Extraction**: Identify named entities and key phrases
- **Text Quality**: Calculate readability scores and language detection

## Integration with Other Commands

**Prerequisites:**
- `/extract` - Provides validated raw data for feature engineering
- `/design` - Defines feature requirements and architecture

**Next Steps:**
- `/train` - Model training with engineered features (ML context)
- `/evaluate` - Evaluation with business features (business context)
- `/extract` - Return if feature requirements reveal data gaps
- `/design` - Return if feature engineering reveals architecture issues

## Troubleshooting

### Feature Quality Issues
- Review feature distributions and identify outliers
- Validate feature creation logic and transformations
- Check for data leakage or temporal inconsistencies
- Analyze feature correlation and redundancy

### Pipeline Performance Problems
- Optimize feature transformation algorithms
- Implement parallel processing for large datasets
- Cache intermediate results for complex transformations
- Review memory usage and resource efficiency

### Feature Store Issues
- Validate feature versioning and lineage tracking
- Check feature catalog metadata and documentation
- Verify access control and permission settings
- Test feature retrieval and serving performance

## Feature Quality Assurance

### Feature Relevance
- Ensure features align with business or model objectives
- Validate predictive power for target use cases
- Identify and remove irrelevant or redundant features
- Confirm feature set completeness for intended application

### Feature Quality
- Analyze feature distributions and identify anomalies
- Address data quality issues in feature creation
- Ensure feature stability across different time periods
- Handle outliers and missing values appropriately

### Pipeline Robustness
- Ensure deterministic and reproducible feature processing
- Handle missing or malformed input data gracefully
- Scale feature transformations to production volumes
- Maintain extensible and maintainable feature pipelines

## Monitoring and Alerting

### Feature Drift Detection
- Monitor feature distributions over time
- Detect statistical changes in feature values
- Alert on significant distribution shifts
- Track feature stability and consistency

### Quality Monitoring
- Monitor feature completeness and missing rates
- Track feature correlation changes
- Alert on feature quality degradation
- Validate feature business logic consistency

## Related Commands

- `/extract` - Data extraction and initial processing
- `/design` - Feature architecture and requirements definition
- `/train` - Model training with engineered features
- `/evaluate` - Evaluation and validation of feature effectiveness

## Support

For issues with the `/features` command:
1. Check this user guide for common solutions
2. Review the [developer guide](../developer-guides/claude-commands/extending-commands.md) for technical details
3. Validate extracted data quality and availability
4. Ensure feature requirements are clearly defined from design phase