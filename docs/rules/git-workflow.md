# Git Workflow Rules

## CRITICAL: Pull Before Push Rule
**MANDATORY SEQUENCE - NEVER SKIP:**
- Make sure all changes are committed before checking out a different branch
```bash
git checkout main
git pull origin main
git checkout feature/branch-name
git merge main
git push
```

## Branch Management Rules

### One Branch Per Task
- Each GitHub task gets its own branch: `feature/issue-[number]-[description]`
- CRDs get their own branch: `feature/crd-[number]-[description]`
- NEVER work on multiple unrelated tasks in same branch

### Branch Creation
```bash
git checkout -b feature/issue-[number]-[brief-description]
# Example: git checkout -b feature/issue-10-new-feature
```

## Commit Standards

### Commit Message Format (MANDATORY)
```bash
git commit -m "$(cat <<'EOF'
Brief descriptive title of changes

- Bullet point list of key changes
- Include technical details and scope
- Reference resolved GitHub issues if applicable
- Resolves GitHub issues #[number], #[number]

🤖 Generated with AI
EOF
)"
```

## Complete Development Workflow

1. **Assignment**: Assign GitHub issue to repository owner
2. **Project Status**: Move issue to "In progress" status and ensure priority is "now"
3. **Branch Creation**: Create feature branch for the issue
4. **Development**: Implement using TDD on feature branch
5. **Testing**: Ensure all tests pass before committing
6. **Commit**: Use standardized message format with assistant attribution
7. **Branch Sync** (CRITICAL): 
   ```bash
   git checkout main
   git pull origin main
   git checkout feature/issue-[number]-[description]
   git merge main
   ```
8. **Push**: `git push -u origin feature/issue-[number]-[description]`
9. **Pull Request**: Create PR with template
10. **Project Update**: Move issue to "In review" status (keep priority "now")
11. **Merge PR**: Merge or approve PR 
12. **Project Update**: Move issue to "Done" status and remove priority label
13. **Post-Merge Cleanup** (CRITICAL):
    ```bash
    # MANDATORY sequence after PR merge
    git checkout main
    git pull origin main
    git branch -d feature/issue-[number]-[description]
    # Update session context files on main
    # Commit context updates and push
    ```

## Troubleshooting

### Uncommitted Changes Error
```bash
# If you get "changes would be overwritten"
git commit -m "WIP: Save current work"
# Then follow normal workflow
```

### Branch Cleanup
```bash
# After PR merge, clean up
git checkout main
git pull origin main
git branch -d feature/issue-[number]-[description]
```

## TodoWrite Integration
When starting git work, automatically add these todos:
- [ ] Pull latest main before any push operations
- [ ] Merge main into feature branch before push
- [ ] Use assistant attribution in commit message
- [ ] Clean up branches after PR merge