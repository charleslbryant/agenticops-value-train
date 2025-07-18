# Wave A Product & Tech Strategy (0–3 Months)

**Scope:** Translate the Business Case for the *Refill Prediction System* into an executable **Wave A (Stand-Up) product + technology strategy**. Wave A corresponds to the initial 0–3 month push (fits within the 16‑week DiscoverTec engagement) where the goal is to *prove value fast*, establish *repeatable technical foundations*, and gather *cost + performance data* that de‑risks later scale waves (B–D).

Wave A is about disciplined speed: ship a working refill‑date prediction MVP into a controlled pilot environment, instrument everything, and document the pipeline so it can be industrialized in Wave B. This approach follows staged MLOps capability build guidance from Google and Microsoft (start with repeatable pipeline components, then automate), leverages AWS SageMaker pipeline patterns for rapid path from data to deploy, and deliberately manages early technical debt highlighted in Hidden Technical Debt research. We will also instrument cloud usage early in keeping with FinOps AI cost forecasting guidance and use stream‑aligned team principles from Team Topologies to keep cognitive load low. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*papers.neurips.cc*](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf?utm_source=chatgpt.com), [*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com), [*teamtopologies.com*](https://teamtopologies.com/key-concepts?utm_source=chatgpt.com))

## Objectives

**Primary Business Objective:** Demonstrate that automated refill‑date predictions can trigger proactive outreach that drives measurable lift in adherence and retention in a pilot customer segment.

**Technical Objectives:**

1.  Stand up secure data ingestion from 2–3 highest‑value pharmacy systems into a cloud landing zone.
2.  Produce a *reproducible* training dataset snapshot (\~1M rows) with documented label logic.
3.  Train 3 baseline models (e.g., gradient boosted trees variants) and compare to heuristic baseline.
4.  Deploy predictions via *Lean* AWS pattern (Serverless inference + nightly batch) into a **pilot environment**.
5.  Capture experiment metadata, model metrics, and cost telemetry from day 1 to feed Wave B automation & FinOps forecast.
6.  Deliver decision‑ready artifact pack (data quality report, model cards lite, pilot results deck) to support go/no‑go for Wave B scale‑up.

These objectives ladder directly to Level 1 → Level 2 transitions in the Google & Microsoft MLOps maturity ladders: move from ad‑hoc notebooks to scripted repeatability w/ early automation hooks. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com))

## Success Metrics

### Business Pilot KPIs

-   **Pilot Adherence Lift** vs control (% fills completed on time).
-   **Pilot Retention Lift** (customer 90‑day continuing active Rx lines).
-   **Engagement Conversion Rate** (customers who act on outreach).
-   **Avoided Manual Calls** (labor savings) traced to automated reminders.

### Technical KPIs

-   **Pipeline Reproducibility Pass Rate** (train → score reproducible hash match \>95%).
-   **Data Quality Rule Pass %** (critical fields \>99% valid; warning \<5% missingness tolerance where business acceptable).
-   **Model Offline Performance** (AUC/PR, MAE days to refill, whichever appropriate) vs heuristic baseline.
-   **Prediction Service Latency (p95)** under 1s (serverless acceptable; cold starts allowed) & **Success Rate** \>99%.
-   **Tagged Cost Visibility**: 100% AWS resources tagged; daily cost export enabled.

Instrumentation of metrics early is emphasized in Google’s continuous delivery guide (CI/CD/CT telemetry), AWS MLOps pipeline patterns (tracking & registry), and FinOps guidance on forecasting AI workloads (measure early, track unit economics). ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com))

## MVP Definition

**In Scope:**

-   Refill‑date prediction for maintenance medications (exclude acute scripts in Wave A).
-   Top 2–3 dispensing channels (mail, in‑clinic, e‑commerce) that cover \~70% volume.
-   Historical data backfill 12–18 months for modeling.
-   Outreach trigger export (CSV/API) to CRM or marketing automation (manual integration acceptable in Wave A).

**Out of Scope (defer to Wave B+):**

-   Real‑time embedded UI inside full pharmacy workflow suite.
-   Full multi‑species ontology reconciliation; include cats & dogs; defer exotics.
-   Automated A/B testing infrastructure (manual stratified reporting OK).
-   SLA’d 24×7 production; pilot business hours reliability acceptable.

MVP slicing and progressive expansion is a recommended approach in both Google and Microsoft maturity guides to reduce scope and accelerate validation; AWS pipeline blog stresses starting with an end‑to‑end slice even if pieces are lightweight/manual. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com))

## Team Configuration

For Wave A we operate as a value stream‑aligned delivery team augmented by lightweight platform enablement from Azure and AWS managed services; no separate platform team yet.

| Role            | % FTE    | Key Responsibilities                                                   | Deliverables                                                      |
|-----------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| Lead            | 0.75–1.0 | KPI definition, backlog, stakeholder sync, pilot design, cost tracking | Pilot charter; KPI dashboard; exec readouts                       |
| Data            | 1.0      | Ingest, schema capture, data quality rules, prep pipelines             | Data source register; curated training table; data quality report |
| AI Engineer A   | 1.0      | Feature engineering, baseline model dev                                | Feature notebooks; model v0 artifacts                             |
| AI Engineer B   | 0.5–1.0  | Training automation scripts; serverless deploy packaging               | Training scripts; inference package; IaC starter                  |
| Model Evaluator | 0.5      | Eval harness, metric dashboards, model card lite                       | Eval report; model card templates                                 |

Small, cross‑functional, customer‑value oriented teams reduce handoffs, central to stream‑aligned patterns in Team Topologies and echoed in TechRadar’s DevOps+MLOps integration analysis that links silo handoffs to poor productionization rates. ([*teamtopologies.com*](https://teamtopologies.com/key-concepts?utm_source=chatgpt.com), [*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain?utm_source=chatgpt.com))

## Technical Architecture

### Rationale

Wave A traffic is low; resilience needs are pilot‑grade; cost sensitivity high; speed matters. We therefore choose the **Lean** AWS cost pattern (SageMaker Serverless Inference + nightly Processing batch). This minimizes 24×7 burn and infrastructure ownership while still running the full data→model→score loop end‑to‑end. AWS illustrates rapid pipeline assembly with SageMaker Pipelines + GitHub Actions; we’ll adopt the minimal subset needed to get to pilot. ([*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com))

### Component Stack

-   **Landing Storage:** S3 raw + curated buckets (versioned).
-   **Data Prep:** AWS Glue or SageMaker Processing jobs (Python/Spark) run nightly.
-   **Experiment Tracking:** Lightweight MLflow tracking server (or SageMaker Experiments), minimal config.
-   **Model Artifacts:** Stored in S3; manual registration spreadsheet in Wave A (formal registry in Wave B).
-   **Inference:** SageMaker Serverless Endpoint packaging 3 models sequentially in a shared container; cold start acceptable.
-   **Batch Scoring:** SageMaker Processing job writes scores to S3 → CSV to CRM.
-   **Security:** IAM least‑privilege roles; KMS encryption at rest; VPC endpoints optional if client requires.
-   **Cost Tagging:** Mandatory tags: `CostCenter`, `Env`, `Model`, `Client`, exported for FinOps forecast.

CI/CD integration is optional but recommended; AWS MLOps pipeline blueprint shows GitHub Actions integration to automate build/train/eval/deploy; we can script manual triggers in Wave A and upgrade to full pipeline in Wave B. ([*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com))

## Deliverable & Milestone

**Week 0–2: Foundations**

-   Stakeholder kickoff; finalize pilot KPIs; confirm data sources & access.
-   AWS accounts / IAM roles / tagging policy in place.
-   Data ingestion spike (small sample).

**Week 3–4: Data Profiling & Prep V0**

-   Data quality profiling; issue backlog.
-   Define label logic; generate first training snapshot.

**Week 5–6: Baseline Modeling**

-   Feature engineering prototypes.
-   Train baseline heuristic + GBM/XGBoost candidate models; log metrics.

**Week 7–8: Evaluation & Iteration**

-   Holdout eval; segment analysis; pick top 3 models for pipeline.
-   Draft model card lite.

**Week 9–10: Packaging & Serverless Deployment**

-   Containerize models; build SageMaker Serverless endpoint.
-   Nightly batch scoring job to S3.

**Week 11–12: Pilot Wiring & Data Feeds Out**

-   Export predicted refill windows to CRM / outreach tool.
-   Start pilot cohort live.

**Week 13–16: Pilot Run & Readout**

-   Monitor performance & cost; collect adherence/retention early signals.
-   Final Wave A report; Wave B scoping workshop.

Time‑boxed iterative delivery with early stakeholder feedback is consistent with Microsoft’s maturity guidance (“grow in increments”), Google’s staged CI/CD/CT adoption, and AWS’s incremental pipeline build patterns. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com))

## Risk Register & Mitigations

| Risk                       | Probability | Impact | Mitigation                                             | Source Guidance                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------|-------------|--------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data access delays         | Med         | High   | Parallelize access tickets; start w/ sample extracts   | Both Google & Microsoft advise early data readiness gating. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com))                                                |
| Data quality surprises     | High        | Med    | Automated profiling, quality rules before modeling     | Google pipeline & AWS blog stress data validation first. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com)) |
| Model reproducibility gaps | Med         | Med    | Versioned data snapshots; logged params                | Hidden Technical Debt warns on undeclared dependencies. ([*papers.neurips.cc*](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf?utm_source=chatgpt.com))                                                                                                                                                                                                            |
| Cost overruns (pilot)      | Low         | Med    | Enforce tags; daily cost checks; serverless scale‑to‑0 | FinOps AI cost forecast guidance. ([*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com))                                                                                                                                                                                                                                                              |
| Siloed workflow delays     | Med         | Med    | Stream‑aligned pod; weekly syncs; avoid handoffs       | Team Topologies & DevOps+MLOps integration articles. ([*teamtopologies.com*](https://teamtopologies.com/key-concepts?utm_source=chatgpt.com), [*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain?utm_source=chatgpt.com))                                                                                                          |

## Data Strategy

**Data Sources:** Dispensing / Rx transactions; customer master; inventory; limited engagement data (email/SMS logs) if available.

**Backfill Window:** 12–18 months; enough seasonality coverage without ballooning cost.

**Latency:** Daily ingestion; near‑real‑time optional later.

**Data Quality Gates:** Basic schema & null checks auto‑run after ingest; results logged; no production block yet but create tickets.

Early, automated data checks at ingestion reduce downstream rework and are recommended as first‑class pipeline steps in Google’s MLOps architecture and AWS’s MLOps pipeline example; technical debt paper highlights data dependency fragility as a common failure vector. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*papers.neurips.cc*](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf?utm_source=chatgpt.com))

## Modeling Strategy

**Model Families:**

1.  Heuristic baseline (days supply calculation + compliance buffer), always deploy for lift measurement.
2.  Gradient Boosted Trees (XGBoost/LightGBM style) using tabular features.
3.  Time‑to‑event survival variant (optional) to capture censoring.

**Label Definition:** Days until next refill event; adjust for early fills; treat non‑refill \> horizon as churn label for secondary model.

**Feature Themes:** Rx history cadence; species/weight; chronic vs acute drug; inventory shipping latency; engagement signals (open/click); regional holiday effect.

**Training Cadence:** One full Wave A train; optional weekly incremental re‑scoring w/out retrain.

Because Wave A emphasizes rapid validation, we prioritize **simple, well‑understood tabular models** that train fast and are easier to explain, reducing cognitive load and audit burden, a best practice in both Google and Microsoft early maturity guidance; AWS pipeline examples routinely start with XGBoost for tabular health workloads before scaling complexity. ([*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com))

## Evaluation Strategy

**Offline:** Temporal holdout; metrics by species, med class, refill cycle length; calibration plots. **Business Simulation:** Predict refills 7/14 days ahead; simulate outreach; estimate incremental fills & avoided stockouts. **Human Review:** Pharmacy SME sanity checks for top/bottom predictions. **Documentation:** Model Card Lite (inputs, training window, metrics, limitations) produced by Model Evaluator.

Structured evaluation checklists and documentation packages are highlighted in Microsoft’s maturity model (governance) and AWS’s model registry pipeline (approval steps); capturing assumptions reduces technical debt per Sculley et al. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*papers.neurips.cc*](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf?utm_source=chatgpt.com))

## Deployment & Ops Strategy

**Mode:** SageMaker Serverless Endpoint (scale‑to‑0) for ad‑hoc scoring; nightly batch Processing for full panel refresh; predictions pushed to S3.

**Environments:** Dev → Pilot (single prod‑like account), skip multi‑AZ HA until Wave B.

**Rollout:** Shadow predictions validated vs historical; then pilot cohort activation.

**Observability:** CloudWatch logs & metrics; simple Grafana/QuickSight dashboard; daily cost export.

AWS shows lightweight pipelines using GitHub Actions to deploy models through SageMaker; serverless endpoints minimize idle cost and simplify infra for early pilots; FinOps recommends early tagging + cost telemetry to prevent surprise spend as usage grows. ([*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com), [*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com))

## Budget

From the AWS Cost Model doc: **Lean scenario ≈ \$75/mo** infra burn at modeled volumes; round to **\$250/mo Wave A ops budget** to cover experimentation, spikes, and logging. (Labor cost dominated by the DiscoverTec engagement.)

**Guardrail Rules:**

-   All resources tagged; untagged = auto shutdown after 24h.
-   Daily Cost Explorer check; alert if MTD \>2× forecast.
-   Use Managed Spot for any training \>30min; serverless inference default.

These controls align with FinOps guidance (forecast → monitor → optimize loop) and AWS pipeline best practices for tagged cost ownership; early cost visibility reduces variance that can derail later scale decisions. ([*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com))

## Exit Criteria

Wave A is complete and we’re ready to industrialize, when ALL of the following are true:

-   Data ingestion automated nightly for top 2–3 sources; quality dashboards in place.
-   1M‑row training snapshot reproducible; documented label logic.
-   Three baseline models trained, versioned, and evaluated against holdout.
-   Serverless inference endpoint live; nightly batch scores exported to pilot outreach.
-   Pilot KPI dashboard shows measurable signal (even directional) in adherence/retention vs control.
-   Cost telemetry captured for 30+ days; forecast vs actual variance \<20%.
-   Risk & issue backlog groomed for Wave B automation.

Formal stage gates with documented artifacts map to Microsoft’s incremental maturity approach, Google’s CI/CD/CT gating recommendations, and AWS registry‑driven promotion flows; capturing exit criteria reduces hidden operational debt. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com))

## Wave B Preview

Wave B will automate what we proved manually: full CI/CD training pipelines, model registry approvals, autoscaled endpoints, drift monitoring, and expanded data coverage. By scoping Wave A tightly, we generate the empirical data (performance lift, cost per prediction, data quality hotspots) needed to justify where to invest automation dollars, a FinOps‑aligned approach to scaling AI responsibly. ([*finops.org*](https://www.finops.org/wg/how-to-forecast-ai-services-costs-in-cloud/?utm_source=chatgpt.com), [*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com))

## Action Checklist

**Immediately:**

-   Confirm pilot cohort & KPIs with pharmacy ops stakeholders.
-   Lock data access paths for top 3 sources.
-   Stand up tagged AWS landing buckets.

**Next 2 Weeks:**

-   Run data profiling; produce issue heatmap.
-   Draft label rules & baseline features.

**By Week 6:**

-   Train & log baseline models.

**By Week 10:**

-   Deploy Lean serverless inference & nightly batch.

**By Week 16:**

-   Pilot results readout; Wave B scope & budget decision.

Time‑boxed, incremental milestones with stakeholder checkpoints mirror the incremental capability build advocated in Microsoft’s MLOps maturity model and Google’s continuous delivery/automation guidance; AWS’s pipeline patterns show similar staged adoption. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model?utm_source=chatgpt.com), [*cloud.google.com*](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/?utm_source=chatgpt.com))

**End of Wave A Product & Tech Strategy**
