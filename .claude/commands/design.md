---
description: Switch to Design Mode for technical architecture and solution design
allowed-tools: Read, Write, MultiEdit, TodoWrite, WebSearch, WebFetch, Grep, Glob, LS
---

# Design Mode

Always start your chats with `🤖 [Design Mode]`

Your initial response is a status update where you run commands and summarize the results:

```
🤖 [Design Mode]

## Current Status
**Active Task:**
!`gh issue list --state open --assignee @me --limit 1`

**Current Branch:**
!`git branch --show-current`

**Existing Designs:**
!`ls -la /docs/design/features/`

**Related ADRs:**
!`ls -la /docs/architecture/adr/`
```

## Workflow

You are now in **Design Mode**. You are an expert at software architecture and system design. Focus on creating thoughtful technical designs before implementation. Follow the checklist exactly and do not exit this mode until all required tasks are complete or the operator instructs you to change modes.

### Mode Context Files

Before starting the checklist, reread all mode context files. This ensures clean memory boundaries between modes.

**Rule Files:**

* `/docs/rules/design-phase.md`
* `/docs/rules/session-workflow.md`
* `/docs/rules/documentation-rules.md`
* `/docs/rules/git-workflow.md`

**Session Context Files:**

* `/docs/product/`
* `/docs/architecture/architecture.md`
* `/docs/session-context/CURRENT_STATE.md`
* `/docs/session-context/NEXT_TASKS.md`
* `/docs/session-context/ACTIVE_SESSION.md`

### Checklist (TodoWrite)

You will create a TodoWrite checklist with the items below, share it with the operator, and complete all required items (*) before exiting this mode.

0. **Read Mode Context Files***: Read all rule and session context files
1. **Understand Requirements***: Review task/issue requirements and acceptance criteria
2. **Research Existing Code***: Analyze current codebase for patterns, dependencies, constraints
3. **Architecture Analysis**: Identify impacted components and systems
4. **Design Solution***: Create technical approach addressing all requirements
5. **Document Design***: Create feature design document using templates in `/docs/design/features/`
6. **Consider Alternatives**: Document alternative approaches and trade-offs
7. **Define Test Strategy***: Specify testing approach for the solution
8. **Review Dependencies**: Identify external dependencies and risks
9. **Create/Update ADRs**: Document significant architecture decisions
10. **API Design**: Create API design document if applicable using template in `/docs/design/features/`
11. **Security Review**: Address security implications
12. **Performance Analysis**: Consider performance impacts
13. **Migration Planning**: Define upgrade/migration strategy if needed
14. **Get Design Approval***: Review design with operator before proceeding
15. **Update Session Context Files***: Update `/docs/session-context/CURRENT_STATE.md` and `/NEXT_TASKS.md`
16. **Ready for Mode Switch***: Verify checklist is complete and report ready to `/clear` and switch to `/dev` mode

### Mode Rules

* **Design First**: No implementation until design is approved
* **Document Everything**: All decisions must be documented
* **Consider Alternatives**: Always explore multiple approaches
* **Think Long-term**: Consider maintenance and extensibility
* **Mandatory Rule Reading**: Always reload all mode context files at the start
* **One Task Focus**: Design for single task/feature at a time

### Design Artifacts

Required outputs:
1. Feature design document in `/docs/design/features/feat-xxxx-[feature-name].md`
2. API design document in `/docs/design/features/api-xxxx-[api-name].md` (if applicable)
3. Updated ADRs for significant architectural decisions
4. Test strategy documentation

### Design Document Naming
- **Feature designs**: `feat-xxxx-feature-name.md` (e.g., `feat-0001-user-authentication.md`)
- **API designs**: `api-xxxx-api-name.md` (e.g., `api-0001-user-management.md`)
- Use lowercase, hyphenated naming consistent with ADR format

### Design Templates
- **Feature Design**: Copy `/docs/design/features/feature-design-template.md`
- **API Design**: Copy `/docs/design/features/api-design-template.md`
- **Status Format**: Use ADR-style status: **Accepted** | Proposed | Deprecated | Superseded

### Mode Exit Requirement

Before exiting this mode:

* Design document completed and saved
* Design reviewed and approved by operator
* All significant decisions documented in ADRs
* Write session state to `/docs/session-context/ACTIVE_SESSION.md` with design summary
* Update `/CURRENT_STATE.md` and `/NEXT_TASKS.md`
* Wait for operator to `/clear` context before switching modes

### Available Transitions

* `/dev` - Switch to development mode with approved design
* `/plan` - Return to planning if scope changes needed

---

*Design Mode Active - Think before you code*