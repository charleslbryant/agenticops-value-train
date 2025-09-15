# Value Train Examples

Real-world examples of using Value Train for different types of work.

## Example 1: API Endpoint

**Task:** Add a new REST endpoint to return user statistics

### /intake
- Marketing team needs user engagement metrics
- Dashboard will consume this data
- Must return daily/weekly/monthly stats
- Performance requirement: < 200ms response time

### /discover
- Current database has the raw data
- Need to research aggregation approach
- Redis available for caching

### /scope
- MUST: Basic stats endpoint
- NICE: Real-time updates
- DEFER: Historical trends
- CONSTRAINT: Use existing database

### /design
```
GET /api/users/{id}/stats?period=daily|weekly|monthly
Response: { visits: 123, actions: 45, duration: 3400 }
Cache strategy: Redis with 1hr TTL
```

### /build
- Added endpoint to UserController
- Created StatsService for aggregation
- Implemented Redis caching
- Added unit tests

### /evaluate
- All tests passing
- Load tested: 150ms average response
- Code reviewed by team

### /deliver
- Merged PR #234
- Deployed to production
- Updated API documentation

## Example 2: Bug Fix

**Task:** Users can't upload files larger than 10MB

### /intake
- Support tickets reporting upload failures
- Affects document upload feature
- Works for small files, fails for large ones

### /discover
- Found nginx config limiting to 10MB
- Application code has no limit
- Cloud storage supports up to 5GB

### /build
- Updated nginx.conf: `client_max_body_size 100M;`
- Added progress indicator for large uploads
- Added file size validation in UI

### /evaluate
- Tested with 50MB file - success
- Verified progress bar works
- No performance degradation

### /deliver
- Applied config change
- Deployed UI updates
- Notified support team

## Example 3: New Feature

**Task:** Add two-factor authentication

### /intake
- Security requirement for enterprise customers
- Support TOTP (Google Authenticator style)
- Optional for users, mandatory for admins
- Need backup codes

### /discover
- Research TOTP libraries for our stack
- Review security best practices
- Check compliance requirements
- Study recovery flow patterns

### /scope
- MUST: TOTP support, backup codes, admin enforcement
- NICE: Remember device option, better UX
- DEFER: SMS-based 2FA, biometric support
- CONSTRAINT: Must be FIDO2 compliant

### /design
- Use Speakeasy library for TOTP
- Store encrypted secrets in database
- 10 backup codes per user
- QR code generation for setup
- Grace period for enforcement

### /build
- Implemented TOTP generation/validation
- Added 2FA setup flow
- Created backup code system
- Updated login flow
- Added admin enforcement

### /evaluate
- Security review passed
- Penetration testing completed
- User acceptance testing done
- Performance impact negligible

### /deliver
- Gradual rollout over 2 weeks
- Documentation updated
- Support team trained
- Monitoring alerts configured

### /operate
- Monitoring adoption rate: 45% in first month
- Support tickets: 12 (mostly setup questions)
- No security incidents

### /improve
- Added setup video tutorial
- Improved QR code display on mobile
- Cached validation to reduce latency

## Example 4: Performance Optimization

**Task:** Dashboard loading too slowly

### /intake
- Dashboard takes 8+ seconds to load
- Affects all users
- Worse with large datasets
- Business impact: user frustration

### /discover
- Profiled database queries: 47 queries per load
- N+1 query problem in reports section
- No pagination on data tables
- Missing database indexes

### /scope
- MUST: Sub-2 second load time
- NICE: Sub-1 second, fancy animations
- DEFER: Complete rewrite
- CONSTRAINT: No breaking changes

### /design
- Batch queries using includes/joins
- Implement virtual scrolling
- Add composite indexes
- Cache frequent queries

### /build
- Reduced to 5 queries total
- Added virtual scrolling to tables
- Created migration for indexes
- Implemented 5-minute cache

### /evaluate
- Load time: 8s → 1.2s
- Tested with largest customer dataset
- Memory usage stable

### /deliver
- Deployed during maintenance window
- Monitored for issues
- Communicated improvement to customers

## Example 5: Technical Debt

**Task:** Refactor legacy authentication code

### /discover
- 5 years old, multiple patches
- No tests
- Security vulnerabilities possible
- Blocking new features

### /scope
- MUST: Secure, testable, maintainable
- NICE: Performance improvements
- DEFER: New features until after refactor
- CONSTRAINT: Zero downtime, backward compatible

### /design
- Extract to AuthenticationService
- Add comprehensive test suite
- Use modern security practices
- Create migration plan

### /build
- Wrote 50+ tests for existing behavior
- Refactored into clean service
- Updated all references
- Added security headers

### /evaluate
- All tests passing
- Security audit passed
- No breaking changes
- Performance improved 20%

### /deliver
- Phased migration over 2 weeks
- Monitored error rates
- No customer impact

## Patterns to Notice

1. **Not every task uses every mode** - Bug fixes often skip design
2. **Discover can be quick or extensive** - Based on unknowns
3. **Evaluate before deliver** - Always test before shipping
4. **Operate reveals improve opportunities** - Real usage drives improvements
5. **Documentation matters** - Update docs in deliver mode

## Your Turn

Take a current task and run it through the modes:
1. What problem are you solving? (intake)
2. What do you need to learn? (discover)
3. What's most important? (scope)
4. What's your approach? (design)
5. Build it (build)
6. Test it (evaluate)
7. Ship it (deliver)