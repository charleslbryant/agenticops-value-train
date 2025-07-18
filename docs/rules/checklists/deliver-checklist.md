# Deliver Mode Checklist

## Mode Configuration
- **Mode**: deliver
- **Description**: Final tests, package artifacts, create PR or release
- **Primary Agents**: studio, ops
- **Allowed Tools**: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*), Bash(test:*)

## Entry Criteria
- [ ] Model evaluation completed and approved
- [ ] All quality gates passed
- [ ] Business stakeholders approved for deployment
- [ ] Production environment prepared and validated

## Core Activities Checklist

### Pre-Deployment Testing
- [ ] Execute final integration testing suite
- [ ] Perform end-to-end system testing
- [ ] Validate production environment compatibility
- [ ] Test deployment and rollback procedures
- [ ] Execute performance and load testing

### Deployment Preparation
- [ ] Package model artifacts and dependencies
- [ ] Create deployment configuration and scripts
- [ ] Prepare monitoring and alerting configuration
- [ ] Document deployment procedures and runbooks
- [ ] Set up backup and disaster recovery

### Production Deployment
- [ ] Deploy model to production environment
- [ ] Configure monitoring and logging systems
- [ ] Implement health checks and status endpoints
- [ ] Set up automated alerting and notifications
- [ ] Validate production deployment functionality

### Documentation and Handoff
- [ ] Create comprehensive deployment documentation
- [ ] Prepare operations and maintenance guides
- [ ] Document troubleshooting and support procedures
- [ ] Create user guides and training materials
- [ ] Prepare handoff materials for operations team

### Quality Assurance
- [ ] Validate production deployment against requirements
- [ ] Test all monitoring and alerting systems
- [ ] Verify security and compliance measures
- [ ] Confirm performance and scalability benchmarks
- [ ] Document final validation and sign-off

## Deliverables
- [ ] `deploy.yaml` - Production deployment configuration
- [ ] `deployment-config.md` - Deployment procedures and settings
- [ ] Production deployment artifacts
- [ ] Operations and maintenance documentation
- [ ] User training and support materials

## Exit Criteria
- [ ] Model successfully deployed to production
- [ ] All monitoring and alerting systems operational
- [ ] Performance benchmarks met in production
- [ ] Documentation complete and approved
- [ ] Operations team trained and handed off

## Quality Gates
- [ ] Production deployment passes all validation tests
- [ ] Monitoring systems detecting and alerting properly
- [ ] Performance meets or exceeds requirements
- [ ] Security and compliance measures validated
- [ ] User acceptance testing completed successfully

## Transition Rules
- **Proceed**: Move to `operate` mode for ongoing monitoring
- **Rollback**: Return to `build` mode if critical issues discovered
- **Iterate**: Continue deployment with patches or improvements

## Common Pitfalls
- Insufficient production environment testing
- Missing or inadequate monitoring and alerting
- Poor deployment documentation and procedures
- Inadequate rollback and disaster recovery planning
- Insufficient user training and support preparation

## Mode-Specific Tools
- Deployment automation and CI/CD tools
- Infrastructure as code and configuration management
- Monitoring and observability platforms
- Documentation and knowledge management systems
- Testing and validation frameworks