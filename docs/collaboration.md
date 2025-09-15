# Collaboration with Value Train

How to use GitHub issues for persistent context and multi-agent collaboration.

## The Problem with Session-Based Work

Traditional development with AI assistants has a major limitation:
- **Context is lost** between sessions
- **No continuity** when switching between people or agents
- **Duplicate work** because previous decisions aren't visible
- **No collaboration** between multiple agents or humans

## The Solution: Issues as Persistent Context

GitHub issues serve as the **single source of truth** for a task, maintaining context across:
- Multiple Claude sessions
- Different human developers
- Various AI agents
- Time zones and async work

## How It Works

### 1. Start with an Issue
Every task begins with a GitHub issue using the Value Train template:
```markdown
## Current Mode
`/build`  <!-- Update as you progress -->

## Session Context
### Session History
- **2024-01-15 Claude:** Completed intake, identified must-haves
- **2024-01-16 Dev:** Built initial implementation
- **2024-01-17 Claude:** Added tests, found edge case
```

### 2. Update After Each Session
When finishing work, update the issue:
```markdown
### Current State
- Branch: `feature/dark-mode`
- Files modified: `ThemeContext.tsx`, `App.css`
- Last action: Added theme toggle component

### Next Steps
- Need to test in Safari
- Add persistence to localStorage
- Update documentation
```

### 3. Read Context When Starting
When beginning work (human or AI):
1. Read the issue to understand current state
2. Check the branch and latest commits
3. Continue from where the last session ended

## Multi-Agent Patterns

### Pattern 1: Human + Claude Pair Programming
```
Morning (Human): Write initial implementation → Update issue
Afternoon (Claude): Add tests and refactor → Update issue  
Next Day (Human): Review and deploy → Close issue
```

### Pattern 2: Multiple Specialized Agents
```
Frontend Claude: Build UI components → Update issue
Backend Claude: Create API endpoints → Update issue
Testing Claude: Write integration tests → Update issue
Human: Final review and merge → Close issue
```

### Pattern 3: Async Global Team
```
US Developer: Start feature → Update issue → Go to bed
UK Claude Session: Continue development → Update issue
India QA Team: Test and report issues → Update issue
US Developer: Wake up to completed feature → Deploy
```

## Best Practices

### 1. Atomic Updates
Update the issue after each meaningful chunk of work:
```markdown
- **2024-01-15 14:30 Claude:** Implemented user service
  - Created `UserService.cs`
  - Added CRUD operations
  - Next: Add authentication
```

### 2. Clear Handoffs
Be explicit about what needs to happen next:
```markdown
### Next Steps
1. ❗ Fix failing test in UserService.Test.cs line 42
2. Add validation for email field
3. Update API documentation
```

### 3. Decision Documentation
Record why decisions were made:
```markdown
### Session History
- **Claude:** Chose Redis for caching (need fast lookups, already in stack)
- **Dev:** Switched from JWT to sessions (simpler for MVP)
```

### 4. Mode Tracking
Update the current mode to show progress:
```markdown
## Current Mode
~~`/intake`~~ ~~`/discover`~~ ~~`/scope`~~ ~~`/design`~~ **`/build`** `/evaluate` `/deliver`
```

## GitHub Integration

### Using @claude in Issues
```markdown
@claude Can you continue implementing the dark mode feature? 
The current state is documented above. Focus on the localStorage persistence.
```

### Automatic Context
Claude can read:
- The entire issue history
- Linked PRs and commits
- Related issues
- Code in the repository

### PR Integration
When creating a PR:
```markdown
Closes #123

Implements dark mode as specified in the issue.
See issue for full context and decision history.
```

## Example: Complete Feature Development

### Issue #42: Add User Authentication

```markdown
## Current Mode
~~`/intake`~~ ~~`/discover`~~ ~~`/scope`~~ ~~`/design`~~ ~~`/build`~~ **`/evaluate`** `/deliver`

## Session Context
### Session History
- **Jan 15 AM - Claude:** Completed intake, identified need for email/password auth
- **Jan 15 PM - Dev:** Researched auth libraries, chose Passport.js
- **Jan 16 - Claude:** Designed database schema, created migration files
- **Jan 17 AM - Dev:** Built registration endpoint
- **Jan 17 PM - Claude:** Added login endpoint and tests
- **Jan 18 - QA:** Found XSS vulnerability in login form
- **Jan 18 - Claude:** Fixed XSS, added input sanitization
- **Jan 19 - Dev:** Deployed to staging

### Current State
- Branch: `feature/auth`
- PR: #45
- Status: In staging, awaiting final testing

### Next Steps
- Verify email validation works
- Test password reset flow
- Deploy to production
```

## Benefits

1. **No Lost Context** - Everything is documented in the issue
2. **Seamless Handoffs** - Anyone can pick up where others left off
3. **Audit Trail** - Complete history of decisions and changes
4. **Parallel Work** - Multiple agents can work on related issues
5. **Async Collaboration** - Works across time zones
6. **Learning** - New team members can read issue history

## Tips for Success

### For Humans
- Update issues immediately after work sessions
- Be specific about what you did and what's next
- Tag @claude when you want AI assistance
- Link commits and PRs to issues

### For Claude/AI
- Always read the issue first
- Update the issue before ending session
- Document decisions and rationale
- Leave clear next steps

### For Teams
- Establish update conventions
- Use labels to show issue state
- Regular issue grooming
- Link related issues

## Integration with Value Train

Each mode naturally creates issue updates:

- **`/intake`** → Document requirements in issue
- **`/discover`** → Add research findings
- **`/scope`** → Update priorities
- **`/design`** → Attach design docs
- **`/build`** → Link commits
- **`/evaluate`** → Add test results
- **`/deliver`** → Note deployment
- **`/operate`** → Add metrics
- **`/improve`** → Create follow-up issues

## Conclusion

GitHub issues aren't just for tracking bugs - they're **persistent collaboration spaces** that enable:
- Continuous development across sessions
- Multi-agent cooperation
- Human-AI collaboration
- Complete project history

By using issues as context stores, the Value Train becomes truly collaborative and continuous, not limited by session boundaries.