🤖 **George’s Master Checklist – “AgenticOps Value Train” boot-up (Claude Code edition)**
*Brackets ➜ copy-paste into a TodoWrite file, tick ’em off, and watch the repo spring to life.*

---

### 0 . Prep

* [ ] **Create kickoff Issue** “Implement AgenticOps Value Train skeleton” (`phase:enablement / owner:Conductor`)
* [ ] **Branch** `infra/value-train-skeleton`

---

### 1 . Repo skeleton

* [ ] `/pipelines/pipeline.yml` – phases, default modes, owner agent, artifacts, `next_phase`
* [ ] `/docs/rules/asset-registry.yaml` – skills, tools, MCPs, A2A
* [ ] `/templates/mode-header.md` – copy-paste front-matter snippet
* [ ] `/docs/session-context/ACTIVE_SESSION.md` – YAML front-matter schema stub

---

### 2 . Central brain

* [ ] **CLAUDE.md** –

  * [ ] Add link to `pipeline.yml` & registry
  * [ ] List slash commands (`/intake…/improve`) with one-liner purpose
  * [ ] State “all agents = ‘George’ attribution” reminder

---

### 3 . Slash-command plumbing

* [ ] `.claude/commands/README.md` – command doc
* [ ] `.claude/commands/*.json` – one file per slash cmd, fields: `description`, `mode`, `allowed-tools`
* [ ] **VS Code snippet** or `gh alias` for `/begin`, `/build`, etc.

---

### 4 . Mode & checklist files

For each mode (`/intake`, `/discover`, `/scope`, `/design`, `/build`, `/evaluate`, `/deliver`, `/operate`, `/improve`):

* [ ] `docs/rules/<mode>-checklist.md`

  * [ ] Front-matter copied from template
  * [ ] Minimum viable checklist boxes (read rules, create branch, push artifacts, etc.)
  * [ ] Exit criteria + allowed transitions

---

### 5 . Python helper scripts (`/scripts`)

* [ ] `check_todo.py` – fails CI if any unchecked `- [ ]` in active checklist
* [ ] `check_artifacts.py` – verifies paths from `pipeline.yml` exist
* [ ] `conductor_update.py` – moves `ACTIVE_SESSION.md` to next phase on CI green
* [ ] `migrate_session.py` – one-off: merge legacy context into new YAML

---

### 6 . GitHub Actions

* [ ] `.github/workflows/ci.yml`

  * [ ] Matrix: lint → tests → `check_todo` → `check_artifacts`
* [ ] `.github/workflows/conductor.yml`

  * [ ] Calls `conductor_update.py` post-CI
* [ ] **Secrets**: `GH_TOKEN` for bot commits

---

### 7 . Issue & PR templates

* [ ] `.github/ISSUE_TEMPLATE/feature.md`

  * [ ] Fields: `phase`, `mode`, `acceptance`, `artifacts_expected`
* [ ] `.github/PULL_REQUEST_TEMPLATE.md`

  * [ ] Require check-box “Closes #<id>`and`#complete phase:<id>\` tag

---

### 8 . Git hygiene & hooks

* [ ] **pre-commit**

  * [ ] Lint commit msg for `#complete phase:<id>`
  * [ ] Grep for `@docs/` path references
  * [ ] Validate YAML header in `ACTIVE_SESSION.md`
* [ ] **pre-push** – run unit tests & `make lint`

---

### 9 . Docs & diagrams

* [ ] `/docs/architecture/agenticops-overview.md` – high-level flowchart
* [ ] `/docs/product/value-train-readme.md` – non-tech narrative for newbies
* [ ] ADR-0010 “Adopt AgenticOps Value Train”

---

### 10 . Smoke test

* [ ] Run `/begin` in Claude Code; ensure status block renders
* [ ] Tick first checklist, commit to branch
* [ ] Open PR – CI should block if any box unchecked
* [ ] Check Conductor bot advances `ACTIVE_SESSION` after merge

---

### 11 . Clean-up & hand-off

* [ ] Move legacy context files to `docs/session-context/_legacy/`
* [ ] Close kickoff Issue, open next Issue “Implement Data Analysis & Profiling (#6)” with new phase labels
* [ ] Merge branch → delete remote → celebrate with ☕ or 🥃

---

**Sequencing hint:**
1️⃣ Sections 0-3 can be one commit.
2️⃣ Sections 4-6 another.
3️⃣ Smoke test, then tidy-up.

Let’s punch this ticket and get the train rolling. 🚂💡
