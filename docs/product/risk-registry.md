# AgenticOps Value Train: Risk Registry

The Risk Registry defines and tracks the known ways the Value Train can go off the rails — and the mitigation strategies that keep us on track. Each risk is tied to a GitHub Issue labeled `risk`, and each mitigation is tracked with a `mitigation` label. This lets us trace features back to why they exist, how they help, and where we still have gaps.

## Why Track Risks?

We build agentic systems that automate real work. That means real failure modes — and real consequences if we ignore them. Managing risk isn't a compliance checkbox. It's how we:

-   See the cracks before they widen
-   Design resilient systems
-   Turn failure into feedback
-   Keep agents, operators, and teams aligned
-   Grow safely and with confidence

### TL;DR

A Risk Registry is how you build antifragility into an AI-driven system. It's not red tape. It’s a proactive design tool for building safer, faster, smarter systems.

### Makes the Invisible Visible

Without a registry, risks are tribal knowledge or vague gut feelings. When something breaks, everyone scrambles. A Risk Registry turns invisible failure modes into visible, trackable, and preventable issues.

→ Benefit: You gain *awareness* before you need *emergency response*.

### Improves System Design

When risks are defined, they can be designed *against*. You can build guardrails, gates, and mitigations directly into Auto-Pilot, checklists, or CI.

→ Benefit: You architect resilience, not just functionality.

### Feeds Evaluation and Continuous Improvement

Each risk gives you a signal to track (like checklist regression or phase stall). That feeds into Nucleus and FlowForge for scoring, triggers, and process evolution.

→ Benefit: Risks become feedback loops, not fire drills.

### Clarifies Agent and Operator Roles

It forces you to ask: “Who’s responsible for spotting or resolving this?” Some risks are best handled by bots. Others need humans. A registry defines that line.

→ Benefit: Reduces finger-pointing and makes ownership explicit.

### Enables Auditability and Trust

When clients or teams ask, “How do you know the system is safe or effective?”, you can point to structured risk management—not vibes, not hope.

→ Benefit: Builds trust with clients, regulators, and teams.

### De-risks Scaling

When you scale from one team to many, or one project to dozens, small risks compound fast. A registry lets you proactively identify and neutralize those compounds.

→ Benefit: Enables safe growth and smooth onboarding.

### Closes the Loop

Most failures aren’t *new*—they’re recurring. A registry ensures that when a risk causes an issue, you learn from it and adjust the system to prevent it again.

→ Benefit: Transforms failure into institutional memory.

## How It Works

### Labels

-   `risk` — Used for long-lived issues that define a specific failure mode
-   `mitigation` — Used for mitigations tied to risks
-   `meta` — Excludes an issue from flow metrics (so risk and mitigation tickets don’t skew WIP, cycle time, etc.)

### Relationships

-   Each `mitigation` issue is linked to one or more `risk` issues
-   Each feature (task or PR) that implements a mitigation links back to that mitigation
-   We trace: `Feature` → `Mitigation` → `Risk`

### Metrics

-   Risks without mitigations = system blind spots
-   Mitigations without features = planning gaps
-   Risks with complete implementation = stronger rails

We track these relationships with GitHub queries, boards, and tags — and optionally visualize coverage in WarRoom.

### Risk Watch Panel

This panel lives in WarRoom (e.g. side-tab, sub-dashboard, or scroll section), summarizing the state of known risks and system health.

#### Layout Sketch (Text Version)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛑 Risk Watch
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Open Risks:         12
Mitigated Risks:     3
Unmitigated Risks:   4
In Progress:         5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ High Attention Risks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[R010] Resource Blowout
→ No mitigation defined

[R009] No Eval Baseline
→ Mitigation planned, not implemented

[R006] Orchestration Breakdown
→ 2 mitigations in progress, status mixed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧯 Mitigation Coverage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  9/12 Risks Covered
▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇      6/12 Implemented

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🕵️‍♀️ Unlinked Features
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[#212] "CI: Add file size gate"
→ Missing mitigation link

[#225] "Refactor Auto-Pilot retry logic"
→ Might cover [R011], but not tagged
```

#### Triggers & Inputs

-   Pulls issues with `risk` and `mitigation` labels (and optional `meta`)
-   Uses GitHub-linked issue references for coverage tracking
-   Optionally queries Nucleus eval results for “rising risks” based on system signals
-   Flags risks with no linked mitigation, or mitigations with no implementation

#### Bonus Features (Future)

-   **Drift Monitor**: Show if a mitigated risk has become “active again” based on recent failures
-   **Mitigation Effectiveness Score**: Based on incident count, retries, Nucleus evaluations
-   **Risk Aging**: Surface risks that have been open the longest without action

#### Implementation Guidance

| What                      | Where                               |
|---------------------------|-------------------------------------|
| Metrics queries           | GitHub API + Labels                 |
| Dashboard rendering       | WarRoom Risk Panel                  |
| Visual scoring            | Eval integration or rule heuristics |
| Triggering `/review-risk` | Manual or post-deploy hook          |

### Risk Issue Template (`.github/ISSUE_TEMPLATE/risk.yml`)

```yaml
name: 🛑 System Risk
description: Log a potential failure mode that could derail delivery, flow, or safety.
labels: [risk, meta]
body:
  - type: input
    id: title
    attributes:
      label: Risk Title
      placeholder: e.g. "Checklist Regression"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      placeholder: What could go wrong? Where and how might it happen?
    validations:
      required: true

  - type: textarea
    id: cause
    attributes:
      label: Cause
      placeholder: What would trigger or allow this risk to occur?

  - type: textarea
    id: impact
    attributes:
      label: Impact
      placeholder: What would break? What’s the consequence?

  - type: textarea
    id: signal
    attributes:
      label: Signal / Early Warning
      placeholder: What symptoms or indicators might this show?

  - type: input
    id: owner
    attributes:
      label: Responsible Agent or Operator
      placeholder: e.g. "Conductor" or "cbryant"

  - type: checkboxes
    id: risk-tags
    attributes:
      label: Additional Tags
      options:
        - label: security
        - label: data
        - label: evaluation
        - label: ops
        - label: flow
```

### Mitigation Template (`.github/ISSUE_TEMPLATE/mitigation.yml`)

```yaml
name: ✅ Risk Mitigation
description: Propose or implement a way to reduce or eliminate a known risk.
labels: [mitigation, meta]
body:
  - type: input
    id: title
    attributes:
      label: Mitigation Title
      placeholder: e.g. "Enforce Checklist Monotonicity in CI"
    validations:
      required: true

  - type: textarea
    id: strategy
    attributes:
      label: Strategy
      placeholder: How will this mitigation prevent or reduce the risk?

  - type: input
    id: links
    attributes:
      label: Related Risk(s)
      placeholder: e.g. "#123, #125"
    validations:
      required: true

  - type: dropdown
    id: status
    attributes:
      label: Implementation Status
      options:
        - Planned
        - In Progress
        - Implemented
        - Abandoned
    validations:
      required: true

  - type: checkboxes
    id: delivery-impact
    attributes:
      label: Where will this mitigation be applied?
      options:
        - label: CI
        - label: Auto-Pilot
        - label: Agent Prompting
        - label: Documentation
        - label: WarRoom Dashboard
```

## Top Risks and How We Mitigate Them

This table is an illustrative example. Each Risk (Rxxx) and Mitigation (Mxxx) would correspond to a GitHub Issue in  
[*https://github.com/charleslbryant/agenticops-value-train/issues*](https://github.com/charleslbryant/agenticops-value-train/issues),  
labeled with risk, mitigation, and optionally meta.

| ID                                                                            | Title                   | Description                                                            | Mitigated By                                                                                                                                                 | Owner         | Status      |
|-------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------|
| [*R001*](https://github.com/charleslbryant/agenticops-value-train/issues/101) | Scope Drift             | Agents operate without clear roles, checklists, or measurable outcomes | [*M001*](https://github.com/charleslbryant/agenticops-value-train/issues/201), [*M002*](https://github.com/charleslbryant/agenticops-value-train/issues/202) | Conductor     | Mitigated   |
| [*R002*](https://github.com/charleslbryant/agenticops-value-train/issues/102) | Context Poisoning       | Prompts are too long, vague, or misaligned, causing agent misfire      | [*M003*](https://github.com/charleslbryant/agenticops-value-train/issues/203)                                                                                | Studio        | Partial     |
| [*R003*](https://github.com/charleslbryant/agenticops-value-train/issues/103) | Artifact Chaos          | Output artifacts are missing, misnamed, or inconsistent                | [*M004*](https://github.com/charleslbryant/agenticops-value-train/issues/204), [*M005*](https://github.com/charleslbryant/agenticops-value-train/issues/205) | Lab           | In Progress |
| [*R004*](https://github.com/charleslbryant/agenticops-value-train/issues/104) | Checklist Regression    | Completed tasks get unchecked through merge errors or force pushes     | [*M006*](https://github.com/charleslbryant/agenticops-value-train/issues/206)                                                                                | Conductor     | Mitigated   |
| [*R005*](https://github.com/charleslbryant/agenticops-value-train/issues/105) | Disconnected Team       | Agents act invisibly or outside daily team ops                         | [*M007*](https://github.com/charleslbryant/agenticops-value-train/issues/207), [*M008*](https://github.com/charleslbryant/agenticops-value-train/issues/208) | Onboarder     | Planned     |
| [*R006*](https://github.com/charleslbryant/agenticops-value-train/issues/106) | Orchestration Breakdown | Hand-offs between agents or phases silently fail                       | [*M009*](https://github.com/charleslbryant/agenticops-value-train/issues/209), [*M010*](https://github.com/charleslbryant/agenticops-value-train/issues/210) | Conductor     | In Progress |
| [*R007*](https://github.com/charleslbryant/agenticops-value-train/issues/107) | Stale or Invalid Inputs | Agents act on outdated, invalidated, or unverified inputs              | [*M011*](https://github.com/charleslbryant/agenticops-value-train/issues/211), [*M012*](https://github.com/charleslbryant/agenticops-value-train/issues/212) | Lab, Improver | Partial     |
| [*R008*](https://github.com/charleslbryant/agenticops-value-train/issues/108) | Mode Misfire            | Agent enters the wrong operating mode for its phase                    | [*M013*](https://github.com/charleslbryant/agenticops-value-train/issues/213)                                                                                | Conductor     | Mitigated   |
| [*R009*](https://github.com/charleslbryant/agenticops-value-train/issues/109) | No Eval Baseline        | Work is marked complete without clear metrics or review                | [*M014*](https://github.com/charleslbryant/agenticops-value-train/issues/214)                                                                                | Evaluator     | Planned     |
| [*R010*](https://github.com/charleslbryant/agenticops-value-train/issues/110) | Resource Blowout        | Token/cost/time usage grows unchecked                                  | [*M015*](https://github.com/charleslbryant/agenticops-value-train/issues/215)                                                                                | Ops           | Not Started |
| [*R011*](https://github.com/charleslbryant/agenticops-value-train/issues/111) | Silent Failure          | Agent failures aren’t logged or surfaced to operators                  | [*M016*](https://github.com/charleslbryant/agenticops-value-train/issues/216), [*M017*](https://github.com/charleslbryant/agenticops-value-train/issues/217) | Evaluator     | In Progress |
| [*R012*](https://github.com/charleslbryant/agenticops-value-train/issues/112) | Security Breach         | Agents access or expose sensitive data improperly                      | [*M018*](https://github.com/charleslbryant/agenticops-value-train/issues/218), [*M019*](https://github.com/charleslbryant/agenticops-value-train/issues/219) | Ops           | Planned     |

## Operator Guidelines

-   When you encounter a recurring failure or systemic issue, open a new issue labeled `risk`
-   When designing a system safeguard or automation to prevent it, create a `mitigation` issue and link it to the relevant `risk`
-   When building a feature that implements the mitigation, link it in the body of the PR or issue
-   Add the `meta` label to `risk` and `mitigation` issues to exclude them from delivery flow metrics

### `/plan-risk` Slash Command Template

Used by agents/operators to create a new `risk` issue.

```markdown
---
description: Capture a newly identified system risk
allowed-tools: Write, IssueWrite
---

# 🛑 [Plan Risk]

Please complete the following template to log a system risk.

### Risk Title
> Summarize the failure mode in 5–10 words

### Description
> What could go wrong? Where and how might it happen?

### Cause
> What would trigger or allow this risk to occur?

### Impact
> What would break? What’s the consequence?

### Signal
> What early indicators or symptoms would surface if this risk emerged?

### Owner
> Who (agent or operator) is responsible for monitoring and addressing this?

### Labels
risk
meta

---

### ✅ Example Output (in a GitHub Issue body)

```markdown
### Risk Title
Checklist Regression

### Description
Previously completed checklist bullets can be reverted to unchecked due to merge conflicts or manual edits, causing CI to pass on incomplete work.

### Cause
A force-push, bot race condition, or unresolved conflict can silently uncheck required bullets.

### Impact
Undelivered work gets marked as done. The pipeline moves forward with missing outputs.

### Signal
Checklist.md shows fewer checked bullets in HEAD than in base branch. Monotonicity check fails.

### Owner
Conductor

### Labels
risk, meta
```

### `/review-risk` Slash Command

Used during retros or delivery planning to review open risks.

```markdown
---
description: Review all open risks, their status, and related mitigations
allowed-tools: IssueRead, CommentWrite
---

# 🔍 [Review Risk]

## Risk Overview

- Open Risks: 12
- Unmitigated Risks: 4
- In-Progress Mitigations: 5
- Fully Mitigated: 3

## Priority Gaps

- R010 – Resource Blowout → No mitigation defined  
- R009 – No Eval Baseline → Mitigation not implemented  

## Suggested Actions

- Create mitigation issue for R010  
- Assign M014 to upcoming sprint to cover R009  
- Confirm that CI includes check_artifacts.py for R003
```

## Roadmap

### Risk Type Classification

**Why:** Helps with filtering, reporting, and prioritization. Not all risks are equal — some are systemic, others tactical.

**How:** Add a `type` field or label to risk issues:

-   `type:system` – architectural, framework-level (e.g. artifact chaos)
-   `type:workflow` – delivery or ops risk (e.g. silent failure)
-   `type:prompting` – LLM instruction-related (e.g. context poisoning)
-   `type:data` – upstream input risks (e.g. stale inputs)
-   `type:security` – data leakage, IAM, compliance

>   Could be a dropdown in the `risk.yml` template or inferred from tags.

### Status Automation

**Why:** Manual tracking of status is brittle. If the linked mitigation or PR is merged, status should auto-update.

**How:**

-   GitHub Actions that:
    -   Close mitigations when linked PRs are merged
    -   Update risk issues when all mitigations are marked implemented
    -   Auto-comment with a progress summary during `/review-risk`

### Risk Archive Protocol

**Why:** Over time, risks may become obsolete. But you don't want to delete them — they're valuable for learning.

**How:**

-   Create a status label: `archived`
-   Move old risks to a folder or board column
-   Add a closing comment:

>   “Risk closed as obsolete. Retained for audit and analysis.”

### Add Risk to PR Template

**Why:** Ensure every PR considers whether it addresses an existing risk — or creates a new one.

**How:** Update `.github/PULL_REQUEST_TEMPLATE.md`:

```md
### Risk Coverage
- [ ] This PR addresses a known risk: `#Rxxx`
- [ ] This PR introduces a new risk (please open a `risk` issue)
- [ ] This PR is not related to any current risks
```

### Risk Insights in `/eval` Mode or Nucleus

**Why:** If your eval agent is scoring output, it should know about open risks.

**How:**

-   Inject current top risks into `/evaluate` mode context
-   Let Nucleus flag outputs that correlate with active risks (e.g., prompt drift, artifact failure, etc.)

## Why This Matters

Risk isn't just theoretical. It shows up as missed deadlines, broken hand-offs, hallucinated outputs, and frustrated operators. The Risk Registry lets us:

-   See what could go wrong
-   Show how we’re preventing it
-   Spot where we still need to act

You wouldn't launch a train without brakes. Don’t ship agentic systems without a risk registry.

Want to see open risks or mitigations? [*Search GitHub for label:risk*](https://github.com/search?q=label%3Arisk) [*Search GitHub for label:mitigation*](https://github.com/search?q=label%3Amitigation)

Let’s keep the train on the rails.
