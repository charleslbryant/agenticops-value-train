# Task Management Rules

## GitHub Issue Types

### PRD (Product Requirement Document)
- **Scope**: High-level feature specifications  
- **Action**: Do NOT implement directly - too broad for single session
- **Process**: Break down into CRDs (specific user stories)
- **Linking**: Reference parent PRD in each CRD

### CRD (Change Request Document)  
- **Scope**: Specific user stories with acceptance criteria
- **Process**: 
  1. Review "Tasks Breakdown" section in CRD
  2. Create separate GitHub task issues for each breakdown item
  3. Work on ONE task at a time
  4. Use single feature branch for entire CRD

### Task Issues
- **Creation**: One GitHub issue per CRD task breakdown item
- **Format**:
  ```bash
  gh issue create --title "Task: [specific task description]" \
    --body "Part of CRD #[CRD-number] - [CRD title]
  
  ## Summary
  [Task description]
  
  ## Acceptance Criteria
  - [ ] [Specific criteria for this task]
  
  ## Parent Issues
  - Resolves part of #[CRD-number]
  - Depends on #[previous-task-number] (if applicable)"
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

## Work Process

### Task Assignment
1. Assign "now" priority task to yourself
2. Move from "next" to "now" when ready for new work
3. Work on ONE task at a time until completion

### Task Completion
1. Complete implementation and tests
2. Mark GitHub issue as completed with comment
3. Move to next task in same CRD or switch CRDs

### Scope Management
- If work expands beyond original task: STOP and check with operator
- If multiple concerns discovered: create separate tasks/branches
- When in doubt about scope: ask operator before proceeding

## TodoWrite Integration
Task management todos:
- [ ] Review task breakdown in assigned CRD
- [ ] Create GitHub issues for each CRD task if not already created
- [ ] Assign current "now" priority task to self
- [ ] Verify current branch matches the task being worked on
- [ ] Complete current task before starting new work