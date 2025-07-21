# /extract Command User Guide

## Overview

The `/extract` command switches Claude into **Extract Mode** as the **Lab Agent**. This mode specializes in data extraction, initial processing, and source validation, implementing robust data extraction pipelines based on validated data access plans.

## When to Use

Use `/extract` when you need to:
- Implement data extraction from identified sources
- Build robust data pipelines with quality validation
- Create initial data processing and transformation
- Establish data monitoring and quality assurance
- Prepare raw data for feature engineering

## Prerequisites

Before running `/extract`, ensure:
- Data access plan has been designed using `/design`
- Data sources have been identified and mapped
- Access credentials and permissions are available
- Technical architecture for data pipeline is approved

## Command Behavior

When you invoke `/extract`, Claude will:

1. **Switch to Extract Mode** - Activate Lab Agent role specialized in data processing
2. **Display Status** - Show current PRD/CRD, branch, and session context
3. **Read Context Files** - Load all rule and session files for clean boundaries
4. **Create TodoWrite Checklist** - Generate structured task list for data extraction
5. **Context Adaptation** - Adapt approach based on project type:
   - **Business Context**: Business data sources and operational metrics
   - **ML Engineering Context**: ML training data and feature source systems
   - **Software Engineering Context**: Application data and system integration points

## Context-Specific Outputs

### Business Context
- **Business Data Extract** with customer and operational data
- Extraction of business metrics, customer data, and operational processes
- Compliance with data privacy and security requirements
- Business intelligence and reporting data preparation

### ML Engineering Context
- **ML Data Extract** with versioned training datasets
- Training, validation, and test dataset preparation
- Data versioning and lineage tracking
- Data quality monitoring and drift detection systems

### Software Engineering Context
- **Application Data Extract** with system and configuration data
- Application state data and configuration extraction
- Data migration and synchronization processes
- System integration and data consistency validation

## Data Extraction Framework

The command follows a comprehensive extraction framework:

### Source Discovery and Mapping
- Source inventory and access method cataloging
- Access validation with credentials and permissions
- Schema discovery and data structure mapping
- Volume assessment and extraction timeframe estimation
- Dependency mapping for source system constraints

### Pipeline Implementation
- Robust, reusable extraction script development
- Comprehensive error handling and retry logic
- Data validation and quality check implementation
- Detailed logging and monitoring setup
- Performance optimization for throughput and efficiency

### Data Quality and Validation
- Schema validation against expected structures
- Completeness checks for missing or incomplete data
- Consistency validation for anomalies and inconsistencies
- Quality metrics and threshold establishment
- Comprehensive data profiling and statistics

## Exit Criteria

The command will not exit until:
- All required checklist items are complete
- Data extraction pipeline implemented and tested
- Data quality validated and documented
- Extraction process monitored and stable
- Schema documentation complete and accurate
- Error handling and monitoring operational
- Session context updated with extraction results

## Common Use Cases

### Database Data Extraction
```
You: /extract
Claude: [Switches to Extract Mode, reviews database access plan]
Claude: [Implements database extraction with connection pooling, incremental updates, and query optimization]
```

### API Data Collection
```
You: /extract
Claude: [Switches to Extract Mode, analyzes API specifications]
Claude: [Creates API extraction pipeline with rate limiting, authentication handling, and response validation]
```

### File-Based Data Processing
```
You: /extract
Claude: [Switches to Extract Mode, reviews file source requirements]
Claude: [Builds file processing pipeline with format detection, compression handling, and integrity validation]
```

## Best Practices

### Before Extraction
- Validate all data source access and credentials
- Review data privacy and security requirements
- Understand data volume and performance expectations
- Confirm extraction timeline and resource constraints

### During Extraction
- Implement comprehensive error handling and retry logic
- Add detailed logging and monitoring throughout the pipeline
- Validate data quality at each stage of the process
- Test with sample data before full-scale extraction

### After Extraction
- Document all extraction processes and data schemas
- Validate extracted data quality and completeness
- Setup monitoring and alerting for ongoing operations
- Update session context with extraction results and learnings

## Common Extraction Patterns

### Database Extraction
- **Connection Management**: Pool connections with proper timeout handling
- **Incremental Processing**: Use watermarks for efficient incremental updates
- **Query Optimization**: Optimize queries for performance and resource efficiency
- **Transaction Handling**: Ensure proper isolation and consistency

### API Data Extraction
- **Rate Limiting**: Implement throttling and respect API limits
- **Authentication**: Handle token refresh and credential management
- **Pagination**: Process large datasets with proper batch handling
- **Error Recovery**: Handle API failures and implement retry strategies

### File-Based Extraction
- **Format Detection**: Automatically detect and handle various file formats
- **Compression Handling**: Process compressed files efficiently
- **Streaming Processing**: Handle large files without memory issues
- **Integrity Validation**: Verify file integrity with checksums

## Integration with Other Commands

**Prerequisites:**
- `/design` - Provides data architecture and access plan
- `/scope` - Defines technical approach and constraints

**Next Steps:**
- `/features` - Feature engineering from extracted data (recommended)
- `/design` - Return if extraction reveals architecture issues
- `/scope` - Return if extraction reveals fundamental constraints

## Troubleshooting

### Extraction Pipeline Failures
- Check data source connectivity and credentials
- Review error logs for specific failure patterns
- Validate data source schemas haven't changed
- Confirm resource availability and performance constraints

### Data Quality Issues
- Review data validation rules and thresholds
- Check for upstream data source changes
- Validate extraction logic and transformations
- Analyze data profiling results for anomalies

### Performance Problems
- Optimize extraction queries and data access patterns
- Review resource utilization and scaling needs
- Implement incremental processing where applicable
- Consider parallel processing for large datasets

## Security Considerations

### Data Privacy
- Ensure all extraction follows privacy regulations (GDPR, CCPA, etc.)
- Implement data anonymization where required
- Validate access permissions and data usage rights
- Document data lineage and usage for compliance

### Access Security
- Use secure credential management systems
- Implement least-privilege access principles
- Encrypt data in transit and at rest
- Audit all data access and extraction activities

## Monitoring and Alerting

### Pipeline Monitoring
- Track extraction job success/failure rates
- Monitor data volume and quality metrics
- Alert on pipeline failures or performance degradation
- Dashboard key extraction metrics and trends

### Quality Monitoring
- Monitor data completeness and consistency over time
- Track data quality score trends and thresholds
- Alert on significant data quality degradation
- Compare extracted data against expected baselines

## Related Commands

- `/design` - Data architecture and pipeline design
- `/scope` - Technical approach and implementation planning
- `/features` - Feature engineering from extracted data
- `/train` - Model training with processed data

## Support

For issues with the `/extract` command:
1. Check this user guide for common solutions
2. Review the [developer guide](../developer-guides/claude-commands/extending-commands.md) for technical details
3. Validate data source access and credentials
4. Ensure design phase deliverables are complete and accessible