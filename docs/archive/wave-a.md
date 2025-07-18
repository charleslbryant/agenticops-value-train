# AI Engineering: Wave A

The goal of the Wave A AI Engineering is to establish a lean, high-impact, cross-functional AI engineering pod that can ship working models to production fast, learn from usage, and evolve into a world-class team.

Designed for a 0–3 month operational maturity window where speed matters but there must be just enough platform discipline to scale. Guidance aligns with Azure MLOps practices, Amazon SageMaker / cross‑cloud MLOps integration patterns, MLflow lifecycle mgmt, OpenTelemetry for vendor‑neutral observability, and DevOps+MLOps convergence research showing failure rates when teams stay siloed. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html), [*aws.amazon.com*](https://aws.amazon.com/otel/), [*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain))

The team is capable of serving enterprise clients that may land in Azure, AWS, or hybrid, we add cross‑cloud tool awareness and portable packaging (containers + ONNX + MLflow) so models move with minimal rewrite. Azure ML + AWS SageMaker have different UX but both support container inference, model registries, and CI/CD triggers; MLflow provides a neutral metadata/control plane that can federate across them. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html))

## Objective

Deliver production-ready AI models within 0–3 months that can:

-   Ingest real-world data
-   Train and improve with feedback
-   Operate in production securely
-   Be evaluated for continuous improvement

This is not a research team, it’s a delivery team that builds AI products for enterprise use at scale.

## Operating Principles

-   Build small, test fast, deploy often
-   Everything is versioned: code, data, models, decisions
-   Security, observability, and maintainability are not afterthoughts
-   Collaborate across roles, not in silos

## Roles

Lean delivery pod:

-   Data Engineer
-   Feature Engineer
-   Training Engineer
-   DevSecOps Engineer
-   Evaluation Engineer
-   Lead Engineer

### Data Engineer (DE)

**Focus:** Data extraction, normalization, pipelines, storage, lineage, privacy

-   Owns data ingestion from APIs, databases, files, etc.
-   Builds scalable, observable pipelines (ETL/ELT)
-   Handles cleaning, labeling, partitioning, and versioning
-   Ensures data lineage and auditability

**Common Platform & Tools:**

-   **Azure:** Data Factory, Synapse/Databricks, ADLS Gen2/Blob, dbt, Azure SQL/PostgreSQL Flex, Microsoft.Data.Analysis.
-   **AWS:** AWS Glue (Studio, Spark, Ray, DataBrew), AWS DMS, S3, Lake Formation
-   **Portable / OSS:** dbt Core, Apache Airflow, Delta Lake/Iceberg, DuckDB

**Key Outputs:**

-   Source connectors
-   Raw→curated jobs
-   Schema registry
-   Basic data quality rules

### Feature Engineer (FE)

**Focus:** Feature extraction, transformation, and engineering pipelines

-   Performs exploratory data analysis to identify key signals
-   Builds reproducible feature pipelines for all data types
-   Documents and versions feature logic
-   Implements drift and integrity checks for critical features

**Common Platform & Tools:**

-   **Azure:** Azure ML Designer/Notebooks, Azure Databricks, Feature Store (preview)
-   **AWS:** SageMaker Feature Store, Processing Jobs, Athena
-   **Portable / OSS:** Pandas, Scikit-learn Pipelines, Featuretools, Feast, Delta Lake

**Key Outputs:**

-   Feature pipelines
-   Versioned feature sets
-   Feature documentation and definitions
-   Drift detection checks

### Training Engineer (TE)

**Focus:** Model selection, training orchestration, and experiment tracking

-   Configures modeling approaches and training parameters
-   Builds training pipelines with reproducibility in mind
-   Runs hyperparameter tuning and performance benchmarking
-   Exports and packages models for deployment

**Common Platform & Tools:**

-   **Azure:** Azure ML pipelines, ML.NET, PyTorch, ONNX export
-   **AWS:** SageMaker Training Jobs, Autopilot, Hyperparameter tuning, Model Registry
-   **Portable / OSS:** MLflow, DVC, PyTorch Lightning, Optuna

**Key Outputs:**

-   Trained model artifacts
-   Experiment logs
-   Training pipeline code
-   Hyperparameter tuning reports

### DevSecOps Engineer (DO)

**Focus:** Build, package, deployment, monitoring, infrastructure, and security

-   Deploys models to APIs, containers, or serverless endpoints
-   Builds CI/CD pipelines for ML code and artifacts
-   Implements drift detection, canary releases, rollback strategies
-   Manages identity, access, and secrets

**Common Platform & Tools:**

-   **Azure:** DevOps Pipelines, AKS, Azure ML endpoints, Key Vault, App Gateway
-   **AWS:** SageMaker endpoints, CodePipeline/CodeBuild, KMS, Secrets Manager, API Gateway + Lambda
-   **Portable / OSS:** Kubernetes, Docker, Helm, KServe, Istio, Tekton, MLflow Registry, ONNX Runtime

**Key Outputs:**

-   CI/CD pipelines
-   Deployment manifests
-   Monitoring dashboards
-   Access controls and audit logs

### Evaluation Engineer (EvE)

**Focus:** Model testing, quality, feedback loop, offline/online metrics, explainability, drift, human-in-loop

-   Evaluates models using offline and online metrics
-   Builds tools and dashboards for human-in-loop review
-   Implements fairness, bias, and explainability frameworks
-   Integrates live feedback into continuous evaluation

**Common Platform & Tools:**

-   **Azure:** Semantic Kernel, Responsible AI dashboard, Azure ML monitoring, Power BI
-   **AWS:** SageMaker Model Monitor / Clarify, CloudWatch, Azure DevOps integration
-   **Portable / OSS:** MLflow metrics, Weights & Biases, OpenTelemetry, Grafana

**Key Outputs:**

-   Evaluation datasets and test harnesses
-   Quality dashboards
-   Bias/fairness/explainability reports
-   Model improvement recommendations

### Lead Engineer (LE)

**Focus:** Strategy, delivery orchestration, stakeholder alignment, and team performance

-   Owns backlog, sprint planning, and team rituals
-   Bridges product, engineering, and client stakeholders
-   Tracks delivery KPIs and ensures measurable value delivery
-   Coaches team members and removes delivery blockers

**Common Platform & Tools:**

-   **Azure:** Azure Boards, Azure Monitor
-   **AWS:** CloudWatch Dashboards, SageMaker Projects
-   **Portable / OSS:** GitHub Projects, Notion/Confluence, OpenTelemetry dashboards

**Key Outputs:**

-   Prioritized backlog
-   Sprint plans and retrospectives
-   Stakeholder reports
-   Team operating metrics

## Maturity Goals (0–3 Months)

| Month   | Focus               | Outcomes                                                              |
|---------|---------------------|-----------------------------------------------------------------------|
| **0–1** | Setup & Integration | Dev environments, data pipelines, infra, GitOps, experiments tracking |
| **1–2** | MVP Model Delivery  | Trained models, deployment pipeline, basic evaluation                 |
| **2–3** | Feedback Loops      | Logging, monitoring, retraining hooks, evaluation dashboards          |

## Dynamics

-   Lead owns backlog, priorities, and delivery flow
-   Daily standups + async updates via GitHub project Kanban board
-   Emphasis on end-to-end delivery of value, with each item ideally delivering data/model value or measurable outcomes
-   Use stories that deliver one independent incremental unit of model value (e.g., "Predict next refill date")

## Skill Matrix

Each row is a capability (skill / experience with columns showing depth of depth needed.

Legend: M = Must, P = Prefer, S = Stretch / Grow.

| Skill / Experience                       | DE | TE | DO | EvE | Why It Matters Wave A                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------|----|----|----|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Secure data ingest (SQL/API/CSV)         | M  | P  | P  | P   | No data, no model. Multicloud ingest required for enterprise clients. ([*aws.amazon.com*](https://aws.amazon.com/glue/engines/), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))                                                                                                                                     |
| Spark / distributed prep                 | P  | S  | S  | S   | Useful when \>1M rows; Glue & Databricks both Spark based. ([*aws.amazon.com*](https://aws.amazon.com/glue/engines/), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))                                                                                                                                                |
| ML training frameworks (PyTorch/XGBoost) | P  | M  | P  | P   | Cross‑cloud training portability; supported in Azure ML & SageMaker. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html))                                                                               |
| Semantic Kernel, ML.NET, .NET interop    | S  | P  | S  | S   | Useful for client‑side SDK integration in Microsoft estates. ([*dotnet.microsoft.com*](https://dotnet.microsoft.com/en-us/apps/ai/ml-dotnet))                                                                                                                                                                                                                                                                                |
| Containerization (Docker)                | P  | P  | M  | P   | Enables portable deploy across Azure ML, SageMaker, K8s. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain))                                                                |
| IaC (Terraform/Bicep/CloudFormation)     | P  | S  | M  | S   | Repeatable env creation; required in regulated clients. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))                                         |
| CI/CD pipelines                          | P  | P  | M  | P   | Automate build→deploy; Azure DevOps→SageMaker pattern. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))                                          |
| Model registry usage                     | P  | M  | P  | M   | Promote/test/rollback; MLflow + cloud registries. ([*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))                                                                                                                                   |
| Observability / OpenTelemetry            | S  | P  | M  | M   | Cross‑cloud metrics & traces unify ops; ADOT + CloudWatch. ([*aws.amazon.com*](https://aws.amazon.com/otel/), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html))                                                                                                                                                                                             |
| Responsible AI / bias checks             | S  | P  | P  | M   | Required in enterprise contracts; Azure Responsible AI tooling; SageMaker Clarify. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html)) |

### Hiring Interview Rubrics

Use the following scenario‑based prompts to screen candidates quickly:

**Data Engineer:** “You must land 3 data sources (SQL, CSV drop, REST API) from different customers into a single schema in \<4 weeks. Describe ingestion pattern, schema evolution, PII controls, and cost mgmt in Glue + Data Factory.” Look for serverless ETL familiarity, schema drift strategy, and encryption defaults. ([*aws.amazon.com*](https://aws.amazon.com/glue/engines/), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))

**Training Engineer:** “Given 1M rows tabular data, compare training on Azure ML vs SageMaker (instance choice, Spot/low priority usage, experiment tracking). When do you export to ONNX?” Candidate should discuss cost vs speed tradeoffs and registry lineage. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), [*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html))

**DevSecOps Engineer:** “We need a gated CI/CD that builds container + model artifact, scans, pushes to both Azure ML endpoint and SageMaker endpoint from one repo. Sketch pipeline.” Expect cloud credentials separation, IaC, and environment promotion. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))

**Evaluation Engineer:** “How do you wire drift & performance alerts cross‑cloud? Which metrics do you push to CloudWatch vs Azure Monitor vs vendor‑neutral OpenTelemetry collector?” Look for metric taxonomy and SLO mindset. ([*aws.amazon.com*](https://aws.amazon.com/otel/), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html))

**Team Fit:** “Tell us about a time you shipped a model to prod w/in 8 weeks, what broke in monitoring later and how’d you fix?” DevOps+MLOps integration experience is predictive of success. ([*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain))

## Team Ops

-   **Environment Review (weekly):** Confirm Azure & AWS env parity, tags, secrets rotation; prevents config drift. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))
-   **Model Artifact Promotion Checklist:** Must exist in MLflow + target cloud registry; container scan clean; metrics above threshold; signoff. ([*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com))
-   **Observability Drill:** Force a synthetic error; verify alarms in CloudWatch & Azure Monitor; update runbook. CloudWatch alarm recommendations show critical metrics to test. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html), [*aws.amazon.com*](https://aws.amazon.com/otel/))
-   **DevOps+MLOps Stand‑Down:** After first prod push, hold 1‑hr retro focused on supply‑chain integration; TechRadar reporting shows 85% of ML fails to prod due to silo gaps—address early. ([*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain))

## Capability to Cloud Technology Map

Options for technology that provide capabilities in cloud environments.

| Capability             | Azure                        | AWS                                   | Neutral / Bridge            | Notes                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------|------------------------------|---------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Ingest/ETL        | Data Factory / Databricks    | AWS Glue / DMS                        | Dagster / dbt               | Glue & Data Factory both schedule ETL; dbt for SQL‑transform parity. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/glue/engines/))                                                                                                                  |
| Data Lake Storage      | ADLS Gen2 / Blob             | Amazon S3                             | Snowflake / Delta / Iceberg | All encrypted @rest; versioning recommended. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com))                                                                                                |
| Training Orchestration | Azure ML                     | SageMaker Training                    | Kubeflow Pipelines          | Managed vs OSS tradeoffs; Spot vs Low‑Priority VMs. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html))                                                                            |
| Model Registry         | Azure ML Registry            | SageMaker Model Registry              | MLflow Registry             | MLflow federates across clouds; API centric. ([*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))                                                                                                                    |
| Deployment             | Managed Endpoint / AKS       | SageMaker Realtime / Serverless / MME | KServe / KFServing          | Use containers & ONNX for portability. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html))                                                                                                                                                     |
| CI/CD                  | Azure DevOps Pipelines       | CodePipeline / GitHub Actions         | GitHub Actions / Jenkins    | AWS prescriptive guidance shows Azure DevOps→SageMaker cross‑cloud pattern. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com)) |
| Secrets                | Key Vault                    | KMS + Secrets Manager                 | Vault                       | Align rotation policies; audit access. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))                                      |
| Observability          | Azure Monitor / App Insights | CloudWatch + ADOT                     | OpenTelemetry / Grafana     | Unified telemetry reduces silos. ([*aws.amazon.com*](https://aws.amazon.com/otel/), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html))                                                                                                                                                                                                   |

## Toolchain Map – CI/CD, Security, Observability (Wave A Lean)

**Git → Build → Train → Package → Deploy → Observe** across clouds.

**Source Control:** Monorepo in GitHub.

**CI Build Layer:** GitHub Actions triggers container build, unit tests, lint, security scans; AWS prescriptive pattern shows Actions/Pipelines pushing into SageMaker. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))

**Train Layer:** Parameterized training jobs in Azure ML or SageMaker; artifacts logged to MLflow Registry for portability. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), [*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html))

**Package & Registry:** Model packaged as Docker + model artifact (ONNX) and pushed to ACR/ECR; registered in both cloud registries (Azure ML, SageMaker Model Registry) with lineage tags. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))

**Deploy Layer:** Automated or manual gated push to: Azure ML managed endpoint *and/or* SageMaker Serverless/Multi‑Model endpoint; follow AWS HA best practices (multi‑AZ) once in prod. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html))

**Observability Layer:** OpenTelemetry collectors (AWS Distro or upstream) sidecar/daemonset export traces, metrics, logs to CloudWatch, Azure Monitor, and vendor tools; set CloudWatch recommended alarms for endpoint error rate/latency. ([*aws.amazon.com*](https://aws.amazon.com/otel/), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html))

**Security / Secrets:** Use Key Vault (Azure) + KMS/Secrets Manager (AWS) mounted via env injection at deploy; central rotation pipelines from CI. ([*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))

## Service Level Objectives

Capture these cross‑cloud metrics from day 1; route via OpenTelemetry where possible.

| Metric                  | Source                                 | Why                                | Alert Hint             |                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|----------------------------------------|------------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inference latency p95   | Endpoint metrics (SageMaker, Azure ML) | Detect cold starts & scaling needs | \>1s sustained (pilot) | ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com))                                                                 |
| Error rate (5xx)        | Endpoint logs→CloudWatch/Azure Monitor | Surf deploy & model load failures  | \>1% /5m               | ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html), [*aws.amazon.com*](https://aws.amazon.com/otel/))                                                                                                                                                                     |
| Data drift stat         | Model Monitor / custom job             | Trigger retrain                    | Z‑score \> threshold   | ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com)) |
| Cost per 1K predictions | Billing export tagged                  | FinOps early warning               | \>2× forecast          | ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html))                                                   |

CloudWatch best‑practice alarms guidance and AWS OpenTelemetry integration docs show how to wire metrics/alarms; Azure ML MLOps docs show model monitoring & metric capture hooks. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html), [*aws.amazon.com*](https://aws.amazon.com/otel/), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com))

## Sprint 1

**Columns:** To Do → In Progress → Done.

**Swimlanes:** Data, Modeling, Ops, Eval, Product.

**WIP Limits:** 2/story type per engineer; keep flow.

| Story                                                          | Role Lead | Acceptance Criteria                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Provision dev envs (Azure sub, AWS acct, IAM/AD sp)            | DevSecOps | Terraform plan applies; least‑priv roles; tagging enabled. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com)) |
| Stand up Git mono‑repo + branch strategy                       | DevSecOps | Main+dev branches; PR policy enforced; CI skeleton runs. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))                                                                                                                                                           |
| Data ingest POC from source → cloud lake                       | Data Eng  | 10K row sample landed nightly in S3 & ADLS; schema logged. ([*aws.amazon.com*](https://aws.amazon.com/glue/engines/), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))                                                                                                           |
| Data profiling notebook & quality metrics export               | Data Eng  | Null %, cardinality, type drift; report published. ([*aws.amazon.com*](https://aws.amazon.com/glue/engines/), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com))                                                                                                      |
| Baseline heuristic refill predictor                            | Model Eng | Runs on sample; produces refill date; logged to MLflow. ([*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com))                                                                                       |
| Container build pipeline (build+scan+push ACR/ECR)             | DevSecOps | Image built on commit; scan pass; tags w/ git SHA. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain))                                 |
| MLflow tracking server bootstrap                               | Model Eng | Track params/metrics; artifact logged; registry reachable. ([*mlflow.org*](https://mlflow.org/docs/latest/model-registry.html))                                                                                                                                                                                                                                                         |
| Observability bootstrap (ADOT Collector to CW + Azure Monitor) | Eval Eng  | Test metric appears in both stacks; alarm fires on test error. ([*aws.amazon.com*](https://aws.amazon.com/otel/), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html))                                                                                                                                                    |

Carryover to Sprint 2: feature engineering v1, serverless endpoint deploy, pilot KPI dashboard.

## Quick Reference Architecture

1.  Data sources land in S3 + ADLS via Glue & Data Factory jobs.
2.  Training jobs triggered by CI pipeline call into Azure ML *or* SageMaker; metrics logged to MLflow.
3.  Artifacts containerized; pushed to ECR & ACR; version recorded in MLflow registry.
4.  Deploy toggled per environment: Azure Managed Endpoint, SageMaker Serverless or Realtime; both behind API front end.
5.  OpenTelemetry collectors sidecar each serving pod → CloudWatch & Azure Monitor; alarms route to shared Ops channel.

This cross‑cloud reference path is documented in AWS prescriptive guidance for SageMaker+Azure DevOps, Azure MLOps docs for pipeline mgmt, and ADOT integration for telemetry fan‑out. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2&utm_source=chatgpt.com), [*aws.amazon.com*](https://aws.amazon.com/otel/))

## Hand‑Off Package Checklist

Before scaling automation:

-   Deployed at least once from CI.
-   MLflow registry canonical; cloud registries reference same artifact.
-   OpenTelemetry metrics flowing; baseline alarms configured.
-   Data quality rules codified in Glue/Data Factory.
-   Sprint metrics captured (lead time, change fail) to benchmark DevOps+MLOps integration; TechRadar highlights the value of shared supply‑chain metrics for scale. ([*techradar.com*](https://www.techradar.com/pro/breaking-silos-unifying-devops-and-mlops-into-a-unified-software-supply-chain), [*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html))

## Appendix

### Minimal IAM & RBAC Patterns

Use in Terraform modules.

-   **BuildRole**: read code repo, write ACR/ECR, start training jobs in either cloud via federated identity. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html), [*learn.microsoft.com*](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2&utm_source=chatgpt.com))
-   **TrainRole**: read training data bucket, write artifacts, limited network egress. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), [*aws.amazon.com*](https://aws.amazon.com/glue/engines/))
-   **DeployRole**: pull model artifact, create/update endpoint, write metrics. Follow AWS deploy best practice to multi‑AZ for resilience once prod. ([*docs.aws.amazon.com*](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html))
-   **ObserveRole**: write metrics/logs to CloudWatch & Azure Monitor exporters; required for ADOT collector. ([*aws.amazon.com*](https://aws.amazon.com/otel/))
