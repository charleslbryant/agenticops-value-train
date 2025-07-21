# /train Command User Guide

## Overview

The `/train` command switches Claude into **Train Mode** as the **Studio Agent**. This mode specializes in model training, hyperparameter optimization, and experiment management, creating optimized models and analytical frameworks from engineered features.

## When to Use

Use `/train` when you need to:
- Train machine learning models for predictive analytics
- Build statistical models for business forecasting
- Create analytical frameworks for decision support
- Optimize model hyperparameters and performance
- Implement experiment tracking and model management

## Prerequisites

Before running `/train`, ensure:
- Feature engineering has been completed using `/features`
- Engineered features are available and validated
- Training objectives and success criteria are defined
- Computational resources are available for training

## Command Behavior

When you invoke `/train`, Claude will:

1. **Switch to Train Mode** - Activate Studio Agent role specialized in model training
2. **Display Status** - Show current PRD/CRD, branch, and session context
3. **Read Context Files** - Load all rule and session files for clean boundaries
4. **Create TodoWrite Checklist** - Generate structured task list for model training
5. **Context Adaptation** - Adapt approach based on project type:
   - **Business Context**: Analytical models and business intelligence frameworks
   - **ML Engineering Context**: Predictive machine learning model training
   - **Software Engineering Context**: System optimization and algorithmic solutions

## Context-Specific Outputs

### Business Context
- **Business Model** with analytical framework and insights
- Statistical models for business forecasting and analysis
- Business rule engines and decision frameworks
- Models optimized for business interpretability and actionable insights

### ML Engineering Context
- **ML Model** with trained algorithms and performance metrics
- Advanced ML algorithms and deep learning model implementation
- Production-ready model artifacts and deployment pipelines
- Models optimized for predictive accuracy and generalization

### Software Engineering Context
- **System Model** with algorithmic solutions and optimizations
- Performance models and system behavior predictors
- Intelligent automation and optimization algorithms
- Models optimized for system efficiency and operational performance

## Training Framework

The command follows a comprehensive training framework:

### Model Architecture Design
- Algorithm selection based on problem type and requirements
- Architecture planning with component interaction design
- Hyperparameter strategy and optimization approach definition
- Validation strategy with cross-validation and holdout testing
- Performance metrics and comprehensive evaluation criteria

### Training Pipeline Implementation
- Data preparation with preprocessing and augmentation
- Robust training loops with checkpointing and recovery
- Comprehensive model validation and testing frameworks
- Experiment tracking and artifact management systems
- Resource optimization for available computational infrastructure

### Model Optimization
- Systematic hyperparameter tuning and optimization
- Model comparison and selection of best performing variants
- Performance enhancement with regularization and ensemble methods
- Training convergence analysis and stability monitoring
- Resource optimization for training efficiency

## Exit Criteria

The command will not exit until:
- All required checklist items are complete
- Model training pipeline implemented and tested
- Model performance validated and documented
- Training experiments tracked and analyzed
- Model artifacts created and properly versioned
- Model monitoring and tracking operational
- Session context updated with training results

## Common Use Cases

### Predictive Model Training
```
You: /train
Claude: [Switches to Train Mode, analyzes ML features]
Claude: [Implements ML algorithms, optimizes hyperparameters, validates model performance]
```

### Business Analytics Model
```
You: /train
Claude: [Switches to Train Mode, reviews business features]
Claude: [Creates statistical models, business forecasts, and analytical frameworks for decision support]
```

### System Optimization Model
```
You: /train
Claude: [Switches to Train Mode, examines system features]
Claude: [Builds performance models, optimization algorithms, and intelligent automation systems]
```

## Best Practices

### Before Training
- Validate feature quality and data splits
- Define clear training objectives and success criteria
- Ensure computational resources are adequate
- Plan experiment tracking and model management strategy

### During Training
- Start with simple baseline models
- Implement comprehensive experiment tracking
- Monitor training convergence and stability
- Validate models on appropriate test datasets

### After Training
- Document model performance and limitations
- Package model artifacts with comprehensive metadata
- Setup model monitoring and drift detection
- Prepare models for evaluation and deployment

## Common Training Patterns

### Supervised Learning
- **Classification Models**: Logistic regression, random forests, neural networks
- **Regression Models**: Linear regression, ensemble methods, deep learning
- **Model Selection**: Cross-validation, grid search, Bayesian optimization
- **Performance Metrics**: Accuracy, precision, recall, F1-score, AUC

### Unsupervised Learning
- **Clustering Models**: K-means, hierarchical clustering, DBSCAN
- **Dimensionality Reduction**: PCA, t-SNE, UMAP for data exploration
- **Anomaly Detection**: Isolation forests, one-class SVM, autoencoders
- **Association Rules**: Market basket analysis and frequent pattern mining

### Deep Learning
- **Neural Architecture**: Feedforward, convolutional, recurrent networks
- **Training Optimization**: Adam, SGD with learning rate scheduling
- **Regularization**: Dropout, batch normalization, weight decay
- **Transfer Learning**: Pre-trained models, fine-tuning, feature extraction

### Time Series Models
- **Statistical Models**: ARIMA, seasonal decomposition, exponential smoothing
- **Machine Learning**: Random forests and gradient boosting for time series
- **Deep Learning**: LSTM, GRU, and Transformer models
- **Forecasting Validation**: Time series cross-validation and backtesting

## Integration with Other Commands

**Prerequisites:**
- `/features` - Provides engineered features for model training
- `/design` - Defines model architecture and training approach

**Next Steps:**
- `/evaluate` - Formal model evaluation and validation (recommended)
- `/features` - Return if training reveals feature engineering issues
- `/design` - Return if training reveals architectural problems

## Troubleshooting

### Training Pipeline Issues
- Check data quality and feature availability
- Validate training data splits and preprocessing
- Review computational resource availability
- Examine training convergence and stability

### Model Performance Problems
- Analyze feature importance and model predictions
- Review hyperparameter settings and optimization
- Check for overfitting or underfitting issues
- Validate model on different data subsets

### Experiment Tracking Issues
- Verify experiment logging and artifact storage
- Check model versioning and metadata tracking
- Validate experiment reproducibility
- Review artifact management and storage systems

## Training Quality Assurance

### Training Robustness
- Ensure deterministic and reproducible training processes
- Handle data edge cases and anomalies appropriately
- Monitor training convergence and stability consistently
- Build resilient training pipelines for failure recovery

### Model Performance
- Meet defined performance criteria and business objectives
- Validate models on appropriate and representative test datasets
- Ensure prediction consistency and reliability
- Assess model generalization across different scenarios

### Experiment Management
- Track and document all training experiments comprehensively
- Enable reproduction and validation of training results
- Properly version and manage all model artifacts
- Maintain searchable and analyzable experiment history

## Model Validation Strategies

### Cross-Validation
- Implement k-fold cross-validation for robust performance estimates
- Use stratified sampling for imbalanced datasets
- Apply time series split validation for temporal data
- Validate model stability across different data splits

### Holdout Testing
- Maintain strict separation between training and test data
- Use representative test sets that reflect production data
- Validate model performance on completely unseen data
- Test model robustness with challenging edge cases

### Performance Metrics
- Choose appropriate metrics for the problem type
- Balance multiple objectives (accuracy, interpretability, speed)
- Monitor both statistical and business metrics
- Track model performance across different data segments

## Resource Optimization

### Computational Efficiency
- Optimize training algorithms for available hardware
- Implement efficient data loading and preprocessing
- Use parallel processing where appropriate
- Monitor and optimize memory usage

### Cost Management
- Balance model complexity with training costs
- Optimize hyperparameter search strategies
- Use early stopping to prevent unnecessary training
- Implement efficient resource scheduling

## Related Commands

- `/features` - Feature engineering and data preparation
- `/design` - Model architecture and training strategy design
- `/evaluate` - Model evaluation and validation
- `/operate` - Model deployment and operational monitoring

## Support

For issues with the `/train` command:
1. Check this user guide for common solutions
2. Review the [developer guide](../developer-guides/claude-commands/extending-commands.md) for technical details
3. Validate feature data quality and availability
4. Ensure computational resources meet training requirements