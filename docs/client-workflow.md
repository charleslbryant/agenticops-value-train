# Client Project Workflow

How to use Value Train for client work, from initial meeting to delivery.

## Overview

Client work requires balancing business needs with technical realities. The Value Train helps structure this process:

- **Plan** - Understand client's business needs
- **Research** - Investigate their technical landscape
- **Scope** - Define the simplest solution that delivers value
- **Design** through **Deliver** - Build and ship
- **Operate** & **Improve** - Ongoing support

## Mode-by-Mode Client Workflow

### Plan Mode - Client Discovery

**Purpose:** Understand what the client really needs (not just what they ask for)

**Activities:**
```markdown
## Client Meeting Agenda
1. Current situation - What's the problem?
2. Desired outcome - What does success look like?
3. Stakeholders - Who will use this?
4. Timeline - When do they need it?
5. Budget - What resources are available?
6. Constraints - Technical, regulatory, organizational
```

**Key Questions:**
- What business problem are we solving?
- How are they doing it now?
- What's the impact of not solving this?
- Who are the end users?
- What's the ROI expectation?

**Deliverables:**
- Meeting notes
- Business requirements document
- Success criteria
- GitHub issues for each requirement

**Example:**
```markdown
## Issue #101: Dashboard for Sales Metrics

### Business Need
Sales managers need real-time visibility into team performance to make daily decisions.

### Current State
- Using Excel spreadsheets updated weekly
- No mobile access
- 3 hours/week manual data entry

### Desired State
- Real-time dashboard
- Mobile responsive
- Automated data sync from CRM

### Success Criteria
- Reduce reporting time by 80%
- Daily usage by all 5 sales managers
- Zero manual data entry
```

### Research Mode - Technical Discovery

**Purpose:** Understand client's technical environment and constraints

**Activities:**
```markdown
## Technical Assessment Checklist
- [ ] Current tech stack
- [ ] Integration points (APIs, databases)
- [ ] Authentication systems
- [ ] Security requirements
- [ ] Compliance needs
- [ ] Performance expectations
- [ ] Existing documentation
- [ ] Access to systems
```

**Investigation Areas:**
- What systems need to integrate?
- What data sources are available?
- What are the security constraints?
- What's their deployment process?
- Who maintains their systems?

**Document Findings:**
```markdown
## Technical Findings

### Environment
- AWS hosted
- PostgreSQL database
- REST API available
- OAuth 2.0 authentication

### Constraints
- Must work in IE11 (corporate policy)
- No access to production database
- Deploy only on Thursdays
- Requires SOC 2 compliance

### Risks
- API rate limiting (100 calls/hour)
- No test environment available
- Limited documentation
```

### Scope Mode - MVP Definition

**Purpose:** Find the simplest solution that delivers business value

**MVP Strategy:**
```markdown
## Scoping Decision Framework

### Must Have (MVP)
- Core functionality that solves the primary problem
- What they'll actually use daily
- What delivers immediate value

### Nice to Have (Phase 2)
- Enhanced features
- Additional integrations
- Advanced analytics

### Defer (Future)
- Bells and whistles
- Edge cases
- "Wouldn't it be cool if..."
```

**Example Scope:**
```markdown
## Project Scope

### Phase 1 (MVP) - 2 weeks
- Basic dashboard with 5 key metrics
- Daily data refresh
- Mobile responsive design
- Single sign-on integration

### Phase 2 - 1 week
- Real-time updates
- Export to PDF
- Email alerts

### Out of Scope
- Custom report builder
- Historical data migration
- Multi-language support
```

### Design Mode - Technical Specification

**Purpose:** Create detailed specifications the client can review

**Client-Friendly Specs:**
```markdown
## Technical Specification

### User Flow
1. User logs in with corporate credentials
2. Dashboard loads with today's metrics
3. User can filter by date range
4. User can drill down into details

### Data Flow
CRM API → Our Backend → Database → Dashboard

### Security
- All data encrypted in transit (HTTPS)
- No sensitive data stored locally
- Session timeout after 30 minutes

### Performance
- Initial load < 3 seconds
- Updates every 5 minutes
- Works on 3G mobile connection
```

**Include Mockups/Wireframes:**
- Use tools like Figma, Excalidraw
- Show key screens
- Get client approval before building

### Build Mode - Implementation

**Client Communication During Build:**

**Daily Updates (if needed):**
```markdown
## Daily Status - Day 3

### Completed
- Authentication integration ✅
- Database schema ✅

### In Progress
- Dashboard layout 🚧
- API integration 🚧

### Blockers
- Waiting for API credentials from client

### Tomorrow
- Complete API integration
- Start mobile responsive design
```

**Demo Preparation:**
- Set up staging environment
- Use realistic test data
- Prepare demo script
- Have fallback plan

### Evaluate Mode - Client Testing

**UAT (User Acceptance Testing):**
```markdown
## UAT Checklist for Client

### Functionality
- [ ] Can you log in with your credentials?
- [ ] Do you see all expected metrics?
- [ ] Can you filter by date?
- [ ] Does export work?

### Usability
- [ ] Is the interface intuitive?
- [ ] Are load times acceptable?
- [ ] Does it work on your phone?

### Data
- [ ] Are the numbers accurate?
- [ ] Is data fresh enough?
- [ ] Are calculations correct?
```

**Bug Tracking:**
```markdown
## Client Feedback Tracker

| Item | Priority | Status | Notes |
|------|----------|--------|-------|
| Logo too small | Low | Fixed | Increased size |
| Wrong timezone | High | Fixed | Now uses user's timezone |
| Add percentage | Medium | Added | Shows % change |
```

### Deliver Mode - Deployment

**Delivery Checklist:**
```markdown
## Delivery Package

### Code
- [ ] Source code in client's repository
- [ ] Production build created
- [ ] Environment variables documented

### Documentation
- [ ] User guide created
- [ ] Admin guide created
- [ ] API documentation
- [ ] Deployment instructions

### Training
- [ ] User training scheduled
- [ ] Admin training scheduled
- [ ] Support handoff

### Sign-off
- [ ] Client testing complete
- [ ] Acceptance criteria met
- [ ] Invoice sent
```

### Operate Mode - Support

**Post-Launch Support:**
```markdown
## Support Plan

### Week 1 - Hypercare
- Daily check-ins
- Immediate bug fixes
- Usage monitoring

### Week 2-4 - Stabilization
- Weekly check-ins
- Bug fixes within 48 hours
- Performance optimization

### Ongoing - Maintenance
- Monthly check-ins
- Feature requests tracked
- Quarterly reviews
```

### Improve Mode - Enhancements

**Gathering Feedback:**
```markdown
## Monthly Review Template

### Usage Metrics
- Daily active users
- Most used features
- Performance metrics

### Feedback
- User complaints
- Feature requests
- Process improvements

### Recommendations
- Quick wins (< 1 day)
- Enhancements (1 week)
- Major features (new project)
```

## Client Communication Templates

### Project Kickoff Email
```
Subject: Project Kickoff - [Project Name]

Hi [Client],

Excited to start working on [project]! Here's our plan:

**This Week:**
- Technical research
- Finalize requirements
- Begin development

**Deliverables:**
- Week 1: Design mockups for approval
- Week 2: Working prototype
- Week 3: Final delivery

**From You:**
- API credentials by [date]
- Test data by [date]
- Feedback on mockups by [date]

Let's schedule a quick call to review.

Best,
[Your name]
```

### Status Update Template
```
Subject: Status Update - [Project Name] - Week 2

Hi [Client],

Quick update on progress:

**Completed This Week:**
- ✅ Authentication integration
- ✅ Dashboard layout
- ✅ Mobile responsive design

**In Progress:**
- 🚧 API integration (75% complete)
- 🚧 Testing

**Blockers:**
- None

**Next Week:**
- Complete testing
- Deploy to staging
- Schedule demo

On track for delivery by [date].

Best,
[Your name]
```

### Issue Escalation Template
```
Subject: Action Needed - [Issue]

Hi [Client],

We've encountered an issue that needs your input:

**Issue:** [Clear description]

**Impact:** [What this affects]

**Options:**
1. [Option A] - Pros/Cons
2. [Option B] - Pros/Cons

**Recommendation:** [Your suggestion]

Please let me know how you'd like to proceed by [date] to stay on schedule.

Best,
[Your name]
```

## Managing Client Expectations

### Be Transparent
- Share progress regularly
- Communicate blockers immediately
- Show work in progress
- Explain technical decisions in business terms

### Set Boundaries
- Define scope clearly
- Document change requests
- Explain impact of changes
- Protect development time

### Build Trust
- Deliver incremental value
- Meet deadlines
- Exceed expectations on quality
- Be responsive

## Common Client Scenarios

### Scenario: Scope Creep
**Client:** "Can we also add feature X?"

**Response:**
```
"Great idea! Let me assess the impact:
- Additional time: 3 days
- Affects: Testing timeline
- Options:
  1. Add to Phase 2
  2. Replace feature Y
  3. Extend timeline

What works best for your priorities?"
```

### Scenario: Urgent Bug
**Client:** "This is broken and we need it fixed NOW!"

**Response:**
```
"I understand the urgency. Let me investigate:
1. I'll diagnose within 1 hour
2. Provide fix timeline
3. Deploy emergency patch if critical

Can you describe what you're seeing?"
```

### Scenario: Vague Requirements
**Client:** "Make it more user-friendly"

**Response:**
```
"I want to ensure we improve the right things. Could you help me understand:
- Which parts feel difficult?
- What tasks take too long?
- What would 'user-friendly' look like to you?

Could we do a quick screen share?"
```

## Success Factors

### What Clients Value
1. **Reliability** - Do what you say
2. **Communication** - Keep them informed
3. **Business Understanding** - Speak their language
4. **Problem Solving** - Offer solutions, not problems
5. **Results** - Deliver business value

### Red Flags to Watch
- Unclear requirements
- No designated decision maker
- Constantly changing priorities
- Unrealistic timelines
- Poor communication
- No access to needed resources

## Summary

The Value Train for client work emphasizes:
1. **Understanding business needs** (Plan)
2. **Researching constraints** (Research)
3. **Finding simple solutions** (Scope)
4. **Clear communication** throughout
5. **Delivering value** incrementally
6. **Building relationships** for future work

Remember: Clients hire you to solve business problems, not write code. Keep the business value front and center in every mode.