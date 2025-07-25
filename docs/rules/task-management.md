# Task Management Rules

## GitHub Issue Hierarchy

### PRD (Product Requirement Document)
- **Purpose**: High-level product requirements that define user problems and solutions
- **Template**: Use `.github/ISSUE_TEMPLATE/prd-requirement.md`
- **Structure**:
  - Overview and user problem
  - Jobs-to-be-Done framework
  - User journey mapping
  - Requirements checklist
  - Success criteria and measurable outcomes
  - Dependencies, risks, and assumptions
  - Roadmap priority (Now/Next/Future)
- **Scope**: Too broad for single session implementation
- **Process**: Break down into multiple CRDs (user stories)
- **Labels**: `PRD`, phase label, priority label
- **Ownership**: Product management focus

### CRD (Change Request Document)
- **Purpose**: Specific user stories with concrete acceptance criteria
- **Template**: Use `.github/ISSUE_TEMPLATE/crd-user-story.md`
- **Structure**:
  - User story format: "As a [user type], I want [capability] so that [benefit]"
  - Parent PRD reference
  - Acceptance criteria checklist
  - Implementation tasks breakdown (In Progress, On Hold, To Do, Done, Cancelled)
  - Dependencies and external blockers
  - Notes and considerations
- **Scope**: Implementable within single feature branch
- **Process**: 
  1. Reference parent PRD issue
  2. Review implementation tasks section
  3. Create separate GitHub Task issues for each breakdown item
  4. Work on ONE task at a time
  5. Use single feature branch for entire CRD
- **Labels**: `CRD`, phase label, agent label, priority label
- **Ownership**: Development team focus

### Task Issues
- **Purpose**: Specific, actionable implementation items from CRD breakdown
- **Template**: Use `.github/ISSUE_TEMPLATE/personal-task.md`
- **Structure**:
  - Task description (brief and specific)
  - Parent PRD/CRD reference
  - Acceptance criteria (specific deliverables)
  - Implementation details (technical approach, files, dependencies)
  - Time estimate and priority
  - Notes and blockers
- **Scope**: Completable in single development session
- **Process**: One issue per CRD task breakdown item
- **Labels**: `Task`, phase label, agent label, priority label
- **Ownership**: Individual developer focus

## Issue Relationship Flow
```
PRD (Product Vision)
├── CRD #1 (User Story)
│   ├── Task #1 (Implementation)
│   ├── Task #2 (Implementation)
│   └── Task #3 (Implementation)
├── CRD #2 (User Story)
│   ├── Task #4 (Implementation)
│   └── Task #5 (Implementation)
└── CRD #3 (User Story)
    └── Task #6 (Implementation)
```

## Task Prioritization

### Priority Labels
- **now**: Current active work (limit 1-2 tasks)
- **next**: Ready for work after current tasks
- **future**: Planned but not yet ready

### Agent Role Labels
- **agent:conductor**: Work for Conductor agent role - leads value train, coordinates handoffs
- **agent:onboarder**: Work for Onboarder agent role - owns pre-engagement success
- **agent:lab**: Work for Lab agent role - handles data profiling, extraction, modeling
- **agent:studio**: Work for Studio agent role - designs models and architecture
- **agent:ops**: Work for Ops agent role - provisions resources, manages deployment
- **agent:evaluator**: Work for Evaluator agent role - validates model quality
- **agent:improver**: Work for Improver agent role - optimizes features and retraining

### Phase Labels

#### Infrastructure Phase
- **phase:enablement**: Infrastructure and tooling setup phase

#### Pre-Engagement Phases
- **phase:opportunity**: Opportunity Triage - Qualify and assess AI opportunity
- **phase:discovery**: Discovery & Framing - Define use case and align objectives
- **phase:readiness**: Client Readiness - Assess data, systems, and constraints
- **phase:scope**: Scope & Pitch - Define MVP and delivery plan
- **phase:pre-kickoff**: Pre-Kickoff Logistics - Confirm legal and technical alignment

#### Delivery Phases
- **phase:data-sources**: Identify data assets and export strategies
- **phase:extraction**: Pull and standardize raw input data
- **phase:preparation**: Create model-ready training dataset
- **phase:exploration**: Profile features and identify patterns
- **phase:feature-engineering**: Generate model-input features
- **phase:training**: Train models and tune hyperparameters
- **phase:validation**: Evaluate model performance
- **phase:deployment**: Deploy model to production
- **phase:monitoring**: Track performance and detect issues
- **phase:improvement**: Optimize features and retraining

### Branch Strategy
- **One branch per CRD**: `feature/crd-[number]-[description]`
- **All CRD tasks share the same branch**
- **Complete CRD before merging branch**

## Mode-Based Workflow Integration

### Planning Phase (`/plan` mode)
1. **Review Current PRDs**: Check "now" priority PRDs for active work or select or create a new PRD with operator approval
2. **Break Down PRDs**: Create CRDs for each user story if needed with operator approval
3. **Prioritize CRDs**: Apply "now", "next", "future" labels with operator approval
4. **Review Current CRD**: Understand scope and acceptance criteria
5. **Create Task Issues**: Break down CRD into specific, prioritized, and testable tasks, with operator approval
6. **Select Next Task**: Choose single task "now" priority taskfor immediate implementation

### Development Phase (`/design`, `/dev` modes)
1. **Single Task Focus**: Work on ONE selected task at a time
2. **Feature Branch**: Use single branch for entire CRD scope
3. **Progress Tracking**: Update task status and CRD implementation section

### Delivery Phase (`/deliver` mode)
1. **Complete Task**: Finish implementation and tests
2. **Update Documentation**: Update affected docs and create ADRs
3. **Create Pull Request**: Follow git workflow rules
4. **Close Issue**: Mark issues as completed with PR reference, the current task issue, if all tasks are complete on a CRD, close the CRD issue, if all CRDs are complete on a PRD, close the PRD issue, with operator approval
5. **Update Issue**: Move completed issues to "Done" section

## Work Process

### Task Assignment
1. Use `/plan` mode to review and assign "now" priority tasks
2. Move tasks from "next" to "now" when ready for new work
3. Work on ONE task at a time until completion
4. Update session context files with current work status

### Task Completion
1. Complete implementation and tests in development mode
2. Use `/deliver` mode to create PR and close task
3. Update parent CRD with completed task status
4. Move to next task in same CRD or switch CRDs

### Scope Management
- If work expands beyond original task: STOP and check with operator
- If multiple concerns discovered: create separate tasks/branches
- When in doubt about scope: ask operator before proceeding
- Use `/plan` mode to re-evaluate scope and create additional tasks

## GitHub Project Integration

### Project Management
All issues must be added to the AgenticOps Value Train project:
- **Project URL**: https://github.com/users/charleslbryant/projects/3
- **Project Fields**: Status, Priority, Size, Estimate, Start/End dates

### Status Management
Issues move through project statuses that align with priority labels:
- **Backlog**: Items that haven't been started (priority: future)
- **Ready**: Items ready to be picked up (priority: next)
- **In progress**: Items actively being worked on (priority: now)
- **In review**: Items in review with PRs created (priority: now)
- **Done**: Items that have been completed (priority label removed)

### Priority-Status Alignment Rules
- **Priority "now"**: Must be in "In progress" or "In review" status
- **Priority "next"**: Must be in "Ready" status
- **Priority "future"**: Must be in "Backlog" status
- **No priority label**: Must be in "Done" status (completed issues)

### One Piece Flow Rules
AgenticOps advocates "one piece flow" - focus on one thing at a time to maintain hierarchy and workflow focus. Finish work before starting new work.

**Priority "now" Limitations (unless operator authorizes exception):**
- **One PRD per project**: Only one PRD can have "now" priority across the entire project
- **One CRD per operator**: Only one CRD can have "now" priority per operator/team
- **One Task per session**: Only one Task can have "now" priority per development session

**Rationale:**
- Prevents context switching and maintains focus
- Ensures completion before starting new work
- Maintains clear hierarchy: PRD → CRD → Task
- Reduces work-in-progress (WIP) and improves flow

### Issue Creation Workflow
When creating new issues:
1. Create the GitHub issue with proper labels
2. Add issue to project: `gh project item-add 3 --owner charleslbryant --url [issue-url]`
3. Set appropriate status based on priority (see Status Update Commands below)
4. Update project fields as needed

### Status Update Commands
Use these commands to update project item statuses. Get the project item ID from `gh project item-list 3 --owner charleslbryant`.

**Project Configuration:**
- Project ID: `PVT_kwHOAAL5684A-P-W`
- Status Field ID: `PVTSSF_lAHOAAL5684A-P-Wzgxtdo8`

**Status Options:**
- Backlog: `f75ad846`
- Ready: `61e4505c`
- In progress: `47fc9ee4`
- In review: `df73e18b`
- Done: `98236657`

**Update Commands:**
```bash
# Update to Backlog
gh project item-edit --id [ITEM_ID] --field-id PVTSSF_lAHOAAL5684A-P-Wzgxtdo8 --project-id PVT_kwHOAAL5684A-P-W --single-select-option-id f75ad846

# Update to Ready
gh project item-edit --id [ITEM_ID] --field-id PVTSSF_lAHOAAL5684A-P-Wzgxtdo8 --project-id PVT_kwHOAAL5684A-P-W --single-select-option-id 61e4505c

# Update to In progress
gh project item-edit --id [ITEM_ID] --field-id PVTSSF_lAHOAAL5684A-P-Wzgxtdo8 --project-id PVT_kwHOAAL5684A-P-W --single-select-option-id 47fc9ee4

# Update to In review
gh project item-edit --id [ITEM_ID] --field-id PVTSSF_lAHOAAL5684A-P-Wzgxtdo8 --project-id PVT_kwHOAAL5684A-P-W --single-select-option-id df73e18b

# Update to Done
gh project item-edit --id [ITEM_ID] --field-id PVTSSF_lAHOAAL5684A-P-Wzgxtdo8 --project-id PVT_kwHOAAL5684A-P-W --single-select-option-id 98236657
```

**Quick Reference:**
```bash
# Get project item ID for issue
gh project item-list 3 --owner charleslbryant --format json | jq -r '.items[] | select(.content.number == [ISSUE_NUMBER]) | .id'

# Example: Update issue to In progress
ITEM_ID=$(gh project item-list 3 --owner charleslbryant --format json | jq -r '.items[] | select(.content.number == 3) | .id')
gh project item-edit --id $ITEM_ID --field-id PVTSSF_lAHOAAL5684A-P-Wzgxtdo8 --project-id PVT_kwHOAAL5684A-P-W --single-select-option-id 47fc9ee4
```

### Status Updates
- **Planning**: New issues start in "Backlog" with priority "future"
- **Ready for work**: Move issue from "Backlog" to "Ready" and change priority to "next"
- **Starting work**: Move issue from "Ready" to "In progress" and change priority to "now"
- **Creating PR**: Move issue from "In progress" to "In review" (keep priority "now")
- **Completing work**: Move issue from "In review" to "Done" and remove priority label
- **Blocked work**: Keep in current status but add `blocked` label

### Label Management Rules
- **Adding priority**: When moving from Backlog → Ready → In progress
- **Keeping priority**: "now" priority stays when moving In progress → In review
- **Removing priority**: Remove priority label when moving to "Done" status
- **Blocked items**: Add "blocked" label but maintain priority and status alignment

## TodoWrite Integration
Task management todos:
- [ ] Review task breakdown in assigned CRD
- [ ] Create GitHub issues for each CRD task if not already created
- [ ] Add new issues to GitHub project with proper status
- [ ] Assign current "now" priority task to self
- [ ] Verify current branch matches the task being worked on
- [ ] Update project status when starting/completing work
- [ ] Complete current task before starting new work