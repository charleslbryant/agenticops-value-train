# Good Practices Guide

Best practices to follow at each mode of the Value Train.

## Plan Mode Practices

### Focus on Business Value
- **Define the problem** before jumping to solutions
- **Identify stakeholders** and their needs
- **Document success criteria** - how will we know it's working?
- **Consider business impact** - ROI, user experience, competitive advantage

### Create Clear Issues
- **One issue per feature/bug** - keep them focused
- **Use templates** - consistency helps
- **Label appropriately** - feature, bug, enhancement, etc.
- **Assign to yourself** when starting work

### Questions to Answer
- What problem are we solving?
- Who will benefit from this?
- What's the business value?
- How will we measure success?

## Research Mode Practices

### Investigate Thoroughly
- **Research existing solutions** before building from scratch
- **Identify technical unknowns** early
- **Document findings in the issue** - keep research visible
- **Time-box research** - don't get lost in analysis paralysis

### Technical Discovery
- **Spike when needed** - create throwaway code to learn
- **Research libraries and tools** - don't reinvent the wheel
- **Check compatibility** - browsers, versions, dependencies
- **Identify risks** - what could go wrong?

### Document Everything
- **Update the issue** with findings
- **Link to resources** - articles, docs, examples
- **Note decisions** - why you chose approach A over B
- **List unknowns** that still need investigation

## Scope Mode Practices

### Find the Simplest Solution
- **Define MVP first** - what's the minimum that delivers value?
- **List must-haves** - can't ship without these
- **Identify nice-to-haves** - would be good but not critical
- **Explicitly defer items** - future iterations

### Be Ruthless About Priorities
- **Ship incrementally** - small working pieces
- **Avoid scope creep** - stick to the plan
- **Question every feature** - is this really needed now?
- **Prefer simple over clever** - maintainability matters

### Clear Boundaries
- **Document what's NOT included** - manage expectations
- **Set clear constraints** - technical, time, resources
- **Define acceptance criteria** - when is it "done"?

## Design Mode Practices

### Specifications Before Code
- **Write specs BEFORE tests** - clear requirements
- **Define acceptance criteria** - testable outcomes
- **Document technical decisions** - architecture, patterns
- **Create API contracts** - interfaces, data models

### Think Through Edge Cases
- **Error handling** - what happens when things fail?
- **Boundary conditions** - min/max values, empty states
- **Concurrency** - race conditions, deadlocks
- **Security** - input validation, authentication

### Keep It Simple
- **Choose boring technology** - proven over trendy
- **Follow existing patterns** - consistency in codebase
- **Design for testability** - dependency injection, mocking
- **Plan for change** - loose coupling, high cohesion

## Build Mode Practices

### Git Workflow
```bash
# Always start from latest main
git checkout main
git pull origin main
git checkout -b feature/issue-123-description

# Work in feature branch
git add -A
git commit -m "feat: implement dark mode toggle"

# Push regularly
git pull origin feature/issue-123-description
git push origin feature/issue-123-description
```

### Test-Driven Development
1. **Write test first** (RED)
   ```javascript
   test('should toggle theme', () => {
     expect(toggleTheme('light')).toBe('dark');
   });
   ```

2. **Write minimal code to pass** (GREEN)
   ```javascript
   function toggleTheme(current) {
     return current === 'light' ? 'dark' : 'light';
   }
   ```

3. **Refactor if needed** (REFACTOR)
   - Improve code quality
   - Remove duplication
   - Ensure tests still pass

### Commit Practices
- **Commit frequently** - small, atomic commits
- **Clear commit messages** - what and why
- **Follow conventions** - feat:, fix:, docs:, test:
- **Reference issues** - "implements #123"

### Code Quality
- **Follow style guide** - consistent formatting
- **Write self-documenting code** - clear names
- **Add comments for "why"** not "what"
- **Handle errors gracefully** - no silent failures

## Evaluate Mode Practices

### Testing Thoroughly
- **All tests must pass** - no exceptions
- **Check edge cases** - boundary conditions
- **Test error paths** - failures matter too
- **Verify acceptance criteria** - meets requirements

### Code Review
- **Create PR for review** - fresh eyes catch issues
- **Link PR to issue** - "Closes #123"
- **Provide context** - what, why, how
- **Include screenshots** for UI changes
- **Respond to feedback** - discuss, don't defend

### Quality Checks
- **Run linter** - catch style issues
- **Check test coverage** - aim for meaningful coverage
- **Performance testing** - load times, memory usage
- **Security review** - vulnerabilities, secrets

## Deliver Mode Practices

### Pull Request Process
```bash
# Before creating PR
git pull origin main
git merge main  # Resolve conflicts locally
npm test        # Ensure all tests pass

# Create PR with good description
# Link to issue: "Closes #123"
# Include screenshots if UI changes
# List testing done
```

### After PR Merge
```bash
# Clean up your workspace
git checkout main
git pull origin main
git branch -d feature/issue-123-description
git push origin --delete feature/issue-123-description
```

### Deployment
- **Deploy to staging first** - test in production-like env
- **Smoke test** - verify basic functionality
- **Monitor after deploy** - watch for errors
- **Have rollback plan** - know how to revert

### Documentation
- **Update user docs** if needed
- **Update API docs** for interface changes
- **Update README** for new features
- **Add to CHANGELOG** - track changes

## Operate Mode Practices

### Monitoring
- **Watch error logs** - catch issues early
- **Track key metrics** - response time, usage
- **Set up alerts** - know when things break
- **Review regularly** - weekly/monthly reviews

### Incident Response
- **Acknowledge quickly** - let users know you're aware
- **Investigate root cause** - don't just fix symptoms
- **Document incidents** - what happened and why
- **Post-mortem** - learn from failures

## Improve Mode Practices

### Analyze Usage
- **Review metrics** - what features are used?
- **Gather feedback** - user complaints/requests
- **Identify bottlenecks** - performance issues
- **Track errors** - recurring problems

### Plan Improvements
- **Prioritize by impact** - biggest wins first
- **Consider effort** - quick wins vs major work
- **Create new issues** - feed back to Plan mode
- **Schedule refactoring** - technical debt matters

### Continuous Learning
- **Retrospectives** - what worked, what didn't
- **Share knowledge** - document learnings
- **Update practices** - evolve this guide
- **Celebrate wins** - recognize good work

## General Best Practices

### Always
- ✅ Work from an issue
- ✅ Use feature branches
- ✅ Write tests first
- ✅ Commit frequently
- ✅ Create PRs for review
- ✅ Update documentation
- ✅ Clean up after merge

### Never
- ❌ Work directly on main
- ❌ Push without pulling first
- ❌ Skip tests
- ❌ Ignore linter warnings
- ❌ Leave console.logs in production
- ❌ Commit secrets or passwords
- ❌ Merge without review

## Workflow Summary

1. **Pick an issue** (or create one)
2. **Pull latest main**
3. **Create feature branch**
4. **Work through modes** (Plan → Research → Scope → Design → Build → Evaluate → Deliver)
5. **Create PR** with issue link
6. **After merge**, clean up branches
7. **Monitor** in production
8. **Learn and improve**

Remember: These practices guide you toward quality, but adapt them to your context. The goal is shipping valuable, maintainable software, not following rules blindly.