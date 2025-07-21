# /operate Command User Guide

## Overview

The `/operate` command switches Claude into **Operate Mode** as the **Ops Agent**. This mode specializes in production monitoring, operational management, and system reliability to ensure stable operation of deployed solutions.

## When to Use

Use `/operate` when you need to:
- Monitor deployed solutions in production environments
- Setup comprehensive monitoring and alerting systems
- Manage operational performance and SLA compliance
- Implement incident response and escalation procedures
- Ensure continuous operational excellence and reliability

## Prerequisites

Before running `/operate`, ensure:
- Solution has been deployed to production using `/deliver`
- Production environment is accessible and operational
- Monitoring infrastructure requirements are defined
- Operational procedures and SLAs are established

## Command Behavior

When you invoke `/operate`, Claude will:

1. **Switch to Operate Mode** - Activate Ops Agent role specialized in operations
2. **Display Status** - Show current PRD/CRD, branch, and session context
3. **Read Context Files** - Load all rule and session files for clean boundaries
4. **Create TodoWrite Checklist** - Generate structured task list for operational management
5. **Context Adaptation** - Adapt approach based on project type:
   - **Business Context**: Business KPI monitoring and value delivery tracking
   - **ML Engineering Context**: Model performance monitoring and drift detection
   - **Software Engineering Context**: System performance and reliability monitoring

## Context-Specific Outputs

### Business Context
- **Business Operations Dashboard** with KPI and value metrics
- User engagement, adoption metrics, and business outcome monitoring
- Revenue impact, cost savings, and operational efficiency tracking
- Business continuity and stakeholder communication management

### ML Engineering Context
- **ML Operations Dashboard** with model performance and health metrics
- Model performance monitoring and prediction accuracy tracking
- Data quality monitoring and model drift detection
- Automated retraining triggers and model version management

### Software Engineering Context
- **System Operations Dashboard** with performance and reliability metrics
- Application metrics, error rates, and user experience monitoring
- System health, resource utilization, and capacity planning
- Security monitoring and compliance validation

## Operations Framework

The command follows a comprehensive operations framework:

### Monitoring and Observability
- Comprehensive metric collection across all system components
- Centralized logging with structured log analysis
- Distributed tracing for performance analysis and debugging
- Real-time dashboards for operational visibility
- Proactive alerting for issues and anomaly detection

### Performance Management
- Service level agreement compliance tracking and reporting
- Resource utilization analysis and capacity forecasting
- Continuous performance tuning and optimization
- Auto-scaling and load management implementation
- Resource cost monitoring and optimization

### Incident Response
- Automated anomaly detection and alert generation
- Standardized incident response and escalation procedures
- Systematic root cause analysis and resolution
- Stakeholder communication management during incidents
- Post-incident review and continuous improvement

## Exit Criteria

The command will not exit until:
- All required checklist items are complete
- Monitoring infrastructure operational with comprehensive coverage
- Performance tracking and SLA monitoring active
- Alert management and incident response procedures operational
- Operational dashboards providing real-time visibility
- Documentation complete for all operational procedures
- Session context updated with operational status and metrics

## Common Use Cases

### Production System Monitoring
```
You: /operate
Claude: [Switches to Operate Mode, analyzes deployed system]
Claude: [Sets up comprehensive monitoring, creates dashboards, implements alerting for system health]
```

### ML Model Operations
```
You: /operate
Claude: [Switches to Operate Mode, reviews deployed ML models]
Claude: [Implements model monitoring, drift detection, performance tracking, and retraining triggers]
```

### Business Solution Operations
```
You: /operate
Claude: [Switches to Operate Mode, examines business solution deployment]
Claude: [Creates business KPI dashboards, monitors user adoption, tracks value delivery metrics]
```

## Best Practices

### Before Operations Setup
- Define clear SLAs and performance targets
- Establish monitoring requirements and alerting thresholds
- Plan incident response procedures and escalation paths
- Prepare operational documentation and runbooks

### During Operations Management
- Implement comprehensive monitoring across all critical components
- Maintain proactive alerting for early issue detection
- Ensure rapid incident response and resolution
- Continuously optimize performance and resource utilization

### After Operations Establishment
- Regularly review and update operational procedures
- Conduct post-incident analysis for continuous improvement
- Monitor and report operational metrics to stakeholders
- Plan capacity and performance improvements

## Common Operations Patterns

### Infrastructure Monitoring
- **System Metrics**: CPU, memory, disk, and network utilization tracking
- **Application Metrics**: Response times, error rates, and throughput monitoring
- **Business Metrics**: User activity, transaction volumes, and revenue tracking
- **Security Metrics**: Authentication failures and intrusion attempt monitoring

### Performance Optimization
- **Resource Scaling**: Auto-scaling based on demand patterns and load
- **Load Balancing**: Traffic distribution and failover management
- **Caching Strategies**: Performance improvement through intelligent caching
- **Database Optimization**: Query optimization and efficient index management

### Incident Management
- **Alert Prioritization**: Critical, warning, and informational alert classification
- **Escalation Procedures**: Automated escalation based on severity and duration
- **Communication Protocols**: Stakeholder notification and status updates
- **Resolution Tracking**: Incident lifecycle management and resolution metrics

### Capacity Planning
- **Usage Forecasting**: Predictive analysis of future resource needs
- **Scalability Testing**: Load testing and capacity validation
- **Resource Optimization**: Cost-effective resource allocation and management
- **Growth Planning**: Infrastructure scaling for anticipated business growth

## Integration with Other Commands

**Prerequisites:**
- `/deliver` - Provides deployed solutions for operational management
- `/evaluate` - Defines operational criteria and success metrics

**Next Steps:**
- `/improve` - Optimization based on operational insights (recommended)
- `/evaluate` - Return if operational issues reveal fundamental problems
- `/deliver` - Return if deployment issues are identified

## Troubleshooting

### Monitoring Setup Issues
- Verify access to production environments and systems
- Check monitoring tool configuration and connectivity
- Validate metric collection and data pipeline functionality
- Ensure proper permissions for monitoring and alerting

### Performance Problems
- Analyze performance metrics and identify bottlenecks
- Review resource utilization and capacity constraints
- Check for configuration issues or system anomalies
- Validate load balancing and scaling configurations

### Incident Response Issues
- Review alert configuration and escalation procedures
- Check notification systems and communication channels
- Validate incident response procedures and documentation
- Ensure proper training and awareness of response teams

## Operational Excellence Framework

### Monitoring Completeness
- Comprehensive coverage of all critical system components
- Sufficient visibility into system health and performance
- Appropriate metric granularity and collection frequency
- Complete monitoring across all operational dimensions

### Performance Management
- Consistent SLA compliance and performance target achievement
- Stable and predictable system performance over time
- Proactive identification and resolution of performance bottlenecks
- Adequate capacity planning for current and projected usage

### Incident Response Readiness
- Responsive and accurate incident detection and alerting
- Well-defined and regularly tested response procedures
- Effective escalation and communication during incidents
- Quick incident resolution with minimal business impact

### Operational Excellence
- Documented and regularly updated operational procedures
- Trained and capable operations team for system management
- Regular tracking and reporting of operational metrics
- Culture of continuous improvement in operational practices

## Monitoring and Alerting Best Practices

### Monitoring Strategy
- **Comprehensive Coverage**: Monitor all critical components and dependencies
- **Proactive Alerting**: Alert on trends and anomalies before issues occur
- **Context-Rich Dashboards**: Provide actionable insights and operational context
- **Historical Analysis**: Track performance trends and patterns over time

### Alert Management
- **Alert Fatigue Prevention**: Balance alert sensitivity with actionability
- **Priority Classification**: Clearly categorize alerts by severity and urgency
- **Escalation Automation**: Automate escalation based on response time
- **False Positive Reduction**: Continuously tune alerts to reduce noise

### Dashboard Design
- **Role-Based Views**: Tailor dashboards for different operational roles
- **Real-Time Updates**: Ensure dashboards reflect current system state
- **Drill-Down Capability**: Enable detailed investigation from high-level views
- **Mobile Accessibility**: Ensure dashboards are accessible on mobile devices

## Security and Compliance Operations

### Security Monitoring
- **Access Control Monitoring**: Track authentication and authorization events
- **Vulnerability Scanning**: Regular security vulnerability assessments
- **Intrusion Detection**: Monitor for unauthorized access attempts
- **Compliance Reporting**: Generate reports for regulatory requirements

### Data Protection
- **Data Access Auditing**: Track all data access and modification events
- **Encryption Monitoring**: Ensure data encryption compliance
- **Backup Verification**: Validate backup integrity and recovery procedures
- **Privacy Compliance**: Monitor adherence to privacy regulations

## Cost and Resource Management

### Cost Optimization
- **Resource Utilization Tracking**: Monitor and optimize resource usage
- **Cost Allocation**: Track costs by service, team, or business unit
- **Waste Identification**: Identify and eliminate unused or underutilized resources
- **Budget Monitoring**: Track spending against allocated budgets

### Capacity Management
- **Growth Projection**: Forecast resource needs based on business growth
- **Scalability Planning**: Plan infrastructure scaling strategies
- **Performance Benchmarking**: Establish baseline performance metrics
- **Resource Right-Sizing**: Optimize resource allocation for cost-effectiveness

## Related Commands

- `/deliver` - Solution deployment and delivery
- `/evaluate` - Solution validation and quality assurance
- `/improve` - Operational optimization and enhancement
- `/design` - Operational architecture and monitoring design

## Support

For issues with the `/operate` command:
1. Check this user guide for common solutions
2. Review the [developer guide](../developer-guides/claude-commands/extending-commands.md) for technical details
3. Validate production environment access and monitoring permissions
4. Ensure operational requirements and SLAs are clearly defined