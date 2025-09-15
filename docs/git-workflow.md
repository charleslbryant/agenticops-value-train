# Git Workflow Guide

A disciplined git workflow that prevents merge conflicts and keeps your repository clean.

## Core Principles

1. **Always work in branches** - Never commit directly to main
2. **Pull before push** - Stay synchronized with remote
3. **Merge main frequently** - Resolve conflicts locally
4. **Clean up after merge** - Delete merged branches

## Starting New Work

### 1. Ensure main is up to date
```bash
git checkout main
git pull origin main
```

### 2. Create feature branch from latest main
```bash
git checkout -b feature/issue-123-short-description
```

**Branch naming conventions:**
- `feature/issue-123-description` - New features
- `fix/issue-456-description` - Bug fixes
- `refactor/issue-789-description` - Code refactoring
- `docs/issue-321-description` - Documentation

### 3. Push branch to remote immediately
```bash
git push -u origin feature/issue-123-short-description
```
This sets up tracking and makes your branch visible to others.

## During Development

### Commit Often
```bash
# Stage changes
git add -A

# Commit with clear message
git commit -m "feat: add dark mode toggle component"
```

**Commit message format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Formatting, no code change
- `refactor:` - Code restructuring
- `test:` - Adding tests
- `chore:` - Maintenance

### Stay Synchronized
```bash
# Before pushing, pull to get any remote changes
git pull origin feature/issue-123-short-description

# Then push your commits
git push origin feature/issue-123-short-description
```

### Keep Up with Main
```bash
# Periodically merge main into your branch
git pull origin main
git merge main

# Resolve any conflicts locally
# Test to ensure everything works
git push origin feature/issue-123-short-description
```

## Before Creating Pull Request

### 1. Get latest main
```bash
git pull origin main
```

### 2. Merge main into your branch
```bash
git merge main
```

### 3. Resolve conflicts if any
```bash
# If conflicts exist:
# 1. Open conflicted files
# 2. Resolve conflicts
# 3. Test thoroughly
git add -A
git commit -m "fix: resolve merge conflicts with main"
```

### 4. Run tests
```bash
npm test  # or your test command
```

### 5. Push updated branch
```bash
git push origin feature/issue-123-short-description
```

## Creating Pull Request

### PR Description Template
```markdown
## Description
Brief description of changes

## Related Issue
Closes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Refactoring
- [ ] Documentation

## Testing Done
- [ ] Unit tests pass
- [ ] Manual testing completed
- [ ] No console errors

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings
```

### Link to Issue
Always include `Closes #123` to automatically close the issue when PR merges.

## After PR Merge

### Clean Up Immediately
```bash
# 1. Switch to main
git checkout main

# 2. Pull the merged changes
git pull origin main

# 3. Delete local feature branch
git branch -d feature/issue-123-short-description

# 4. Delete remote feature branch
git push origin --delete feature/issue-123-short-description

# 5. Confirm clean state
git branch -a  # Should not show deleted branch
```

## Common Scenarios

### Scenario: Stashing Changes
When you need to switch branches but have uncommitted changes:
```bash
# Save current changes
git stash save "WIP: dark mode implementation"

# Switch branches and do other work
git checkout other-branch

# Come back and restore changes
git checkout feature/issue-123-short-description
git stash pop
```

### Scenario: Fixing Last Commit
Made a typo in commit message or forgot a file:
```bash
# Add forgotten file
git add forgotten-file.js

# Amend last commit
git commit --amend

# Force push if already pushed (use carefully!)
git push --force origin feature/issue-123-short-description
```

### Scenario: Undoing Changes
Need to undo uncommitted changes:
```bash
# Undo changes to specific file
git checkout -- file-to-undo.js

# Undo all changes
git checkout -- .

# Remove untracked files
git clean -fd
```

### Scenario: Conflict Resolution
When merging main creates conflicts:
```bash
# Merge main
git merge main

# See conflicted files
git status

# Open each conflicted file
# Look for <<<<<<< HEAD markers
# Resolve conflicts
# Remove conflict markers

# Add resolved files
git add -A

# Complete merge
git commit -m "fix: resolve merge conflicts with main"

# Test everything works!
npm test

# Push resolved branch
git push origin feature/issue-123-short-description
```

## Best Practices

### Do's ✅
- Pull main before creating branches
- Create descriptive branch names
- Commit frequently with clear messages
- Pull before pushing
- Merge main into feature branch regularly
- Delete branches after merge
- Use PR templates
- Link PRs to issues

### Don'ts ❌
- Work directly on main
- Force push to shared branches
- Leave stale branches
- Ignore merge conflicts
- Push without pulling first
- Merge without testing
- Use generic commit messages
- Leave console.logs in code

## Git Aliases (Optional)

Add these to your `.gitconfig` for shortcuts:
```bash
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
    pl = pull
    ps = push
    sync = !git pull origin main && git merge main
    cleanup = !git checkout main && git pull origin main && git branch -d
```

Usage:
```bash
git co main           # checkout main
git sync              # pull and merge main
git cleanup feature   # switch to main and delete feature branch
```

## Troubleshooting

### "Branch has diverged"
```bash
# This happens when local and remote have different histories
git pull --rebase origin feature/branch-name
```

### "Cannot delete branch (not fully merged)"
```bash
# Force delete if you're sure
git branch -D feature/branch-name
```

### "Permission denied (publickey)"
```bash
# Check SSH keys
ssh -T git@github.com

# If fails, add SSH key to GitHub
```

### "Detached HEAD state"
```bash
# Get back to branch
git checkout main
# or
git checkout feature/your-branch
```

## Summary Workflow

1. `git checkout main && git pull origin main`
2. `git checkout -b feature/issue-123-description`
3. Work and commit frequently
4. `git pull origin feature/issue-123-description` before pushing
5. `git push origin feature/issue-123-description`
6. Before PR: `git pull origin main && git merge main`
7. Create PR with "Closes #123"
8. After merge: Clean up branches

Following this workflow ensures:
- No lost work
- Clean git history
- Minimal merge conflicts
- Easy collaboration
- Traceable changes