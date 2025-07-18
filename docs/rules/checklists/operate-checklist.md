# Operate Mode Checklist

## Mode Configuration
- **Mode**: operate
- **Description**: Watch live performance, drift, cost, error budgets
- **Primary Agents**: ops, evaluator
- **Allowed Tools**: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), WebFetch

## Entry Criteria
- [ ] Model successfully deployed to production
- [ ] Monitoring and alerting systems operational
- [ ] Operations team trained and ready
- [ ] Performance benchmarks established

## Core Activities Checklist

### Performance Monitoring
- [ ] Monitor model inference latency and throughput
- [ ] Track system resource utilization and costs
- [ ] Monitor API response times and availability
- [ ] Track user engagement and satisfaction metrics
- [ ] Monitor business KPIs and success metrics

### Model Health Monitoring
- [ ] Monitor model accuracy and performance metrics
- [ ] Detect and alert on model drift and degradation
- [ ] Track data quality and input distribution changes
- [ ] Monitor model bias and fairness metrics
- [ ] Track prediction confidence and uncertainty

### Operations Management
- [ ] Manage system capacity and scaling
- [ ] Monitor and optimize cloud costs
- [ ] Maintain security and compliance measures
- [ ] Handle system maintenance and updates
- [ ] Manage backup and disaster recovery

### Incident Response
- [ ] Respond to system alerts and incidents
- [ ] Investigate and diagnose performance issues
- [ ] Implement immediate fixes and workarounds
- [ ] Document incidents and root cause analysis
- [ ] Coordinate with stakeholders during outages

### Continuous Improvement
- [ ] Collect and analyze user feedback
- [ ] Identify optimization opportunities
- [ ] Monitor competitive landscape and benchmarks
- [ ] Track and report on business value delivery
- [ ] Plan and prioritize improvement initiatives

## Deliverables
- [ ] `dashboard-link.txt` - Monitoring dashboard access
- [ ] `monitoring-config.yaml` - Monitoring system configuration
- [ ] Performance and health reports
- [ ] Incident response documentation
- [ ] Continuous improvement recommendations

## Exit Criteria
- [ ] System operating within defined performance parameters
- [ ] All monitoring and alerting systems stable
- [ ] No critical incidents or performance issues
- [ ] Business metrics meeting or exceeding targets
- [ ] Improvement opportunities identified and prioritized

## Quality Gates
- [ ] Model performance maintaining acceptable levels
- [ ] System uptime and availability meeting SLAs
- [ ] Response times within defined thresholds
- [ ] Cost optimization targets being met
- [ ] Security and compliance requirements satisfied

## Transition Rules
- **Continue**: Ongoing operation with regular monitoring
- **Improve**: Move to `improve` mode for optimization
- **Incident**: Escalate to emergency response procedures

## Common Pitfalls
- Insufficient monitoring coverage or alerting
- Slow response to performance degradation
- Inadequate cost monitoring and optimization
- Missing business impact tracking
- Poor incident response procedures

## Mode-Specific Tools
- Application performance monitoring (APM) tools
- Infrastructure monitoring and observability platforms
- Cost management and optimization tools
- Log aggregation and analysis systems
- Incident management and response tools