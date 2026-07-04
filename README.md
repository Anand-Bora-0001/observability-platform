# Enterprise Identity & Cloud Observability Platform

![Version](https://img.shields.io/badge/version-v2.0.0--enterprise-blue)
![Architecture](https://img.shields.io/badge/architecture-microservices-orange)
![Kubernetes](https://img.shields.io/badge/kubernetes-helm-informational)
![AI Ops](https://img.shields.io/badge/AI-LLM_RCA-purple)

A Fortune 500-grade, event-driven Cloud Infrastructure Observability and Identity Management platform. 

This platform demonstrates modern Full Stack Engineering, Cloud Engineering, Identity & Access Management (IAM), Observability, Security Engineering, Distributed Systems, and DevOps.

## 🌟 Core Features

- **Event-Driven Microservices**: Powered by Apache Kafka, ensuring highly scalable, asynchronous communication between nodes.
- **Enterprise IAM**: A dedicated Golang gRPC Identity service managing stateless JWT authentication and granular Role-Based Access Control (RBAC).
- **AI-Assisted Operations (AIOps)**: A specialized Python microservice performing LLM-assisted Root Cause Analysis (RCA) and Retrieval-Augmented Generation (RAG) on infrastructure alerts.
- **The Three Pillars of Observability**: 
  - **Metrics**: Prometheus & Grafana with Blackbox Exporters.
  - **Traces**: OpenTelemetry (OTel) distributed tracing via Jaeger.
  - **Logs**: Centralized, structured log aggregation via Grafana Loki & Promtail.
- **Dynamic Security**: HashiCorp Vault integration for dynamic database credential retrieval. AWS IAM Roles for Service Accounts (IRSA) configurations via Terraform.
- **Dual Frontends**: 
  - A React-based SRE & NOC Operations Dashboard.
  - A Vue 3-based Identity & Security Administration Portal.
- **Cloud Native DevOps**: Fully parameterized Kubernetes Helm charts and automated GitHub Actions CI/CD pipelines.

---

## 🏗️ Architecture Diagram

```mermaid
graph TD
    %% Frontends
    Client([Web Client])
    NOC[React NOC Dashboard\n(Port 3000)]
    Admin[Vue 3 Admin Portal\n(Port 3001)]
    
    %% API Gateway / Ingress
    Ingress{{NGINX / K8s Ingress}}
    
    %% Microservices
    Backend[Python Core API\nFastAPI / Port 8000]
    Identity[Go Identity API\ngRPC / Port 50051]
    AIOps[AI Ops API\nFastAPI / Port 8002]
    
    %% Event Streaming
    Kafka{Apache Kafka\nMessage Bus}
    Zookeeper[(Zookeeper)]
    
    %% Databases & Secrets
    DB[(PostgreSQL)]
    Redis[(Redis Cache)]
    Vault{HashiCorp Vault\nSecrets Engine}
    
    %% Observability Stack
    Prometheus(Prometheus)
    Grafana(Grafana)
    Jaeger(Jaeger\nOTel Tracing)
    Loki(Grafana Loki\nLog Aggregation)
    Promtail(Promtail)
    Blackbox(Blackbox Exporter)
    
    %% Routing
    Client --> NOC
    Client --> Admin
    NOC --> Ingress
    Admin --> Ingress
    Ingress --> Backend
    
    %% Microservice Comms
    Backend -- "gRPC Auth" --> Identity
    Backend -- "Fetch DB Creds" --> Vault
    Backend -- "Publish ALERT_TRIGGERED" --> Kafka
    Kafka -- "Consume Events" --> AIOps
    AIOps -- "Publish RCA_COMPLETED" --> Kafka
    
    %% Data Persistence
    Backend --> DB
    Backend --> Redis
    Identity --> DB
    Kafka --- Zookeeper
    
    %% Telemetry
    Backend -. "OTLP Traces" .-> Jaeger
    Identity -. "OTLP Traces" .-> Jaeger
    Backend -. "/metrics" .-> Prometheus
    Promtail -. "Tails Container Logs" .-> Loki
    Grafana -. "Queries Data" .-> Prometheus
    Grafana -. "Queries Logs" .-> Loki
    Grafana -. "Queries Traces" .-> Jaeger
    Prometheus -. "Probes Targets" .-> Blackbox
```

---

## 📂 Repository Structure (Monorepo)

```text
observability-platform/
├── apps/
│   ├── dashboard-react/     # React NOC Operations Dashboard (Vite + Tailwind)
│   └── admin-vue/           # Vue 3 Identity Administration Portal (Vite + TS)
├── services/
│   ├── backend-python/      # Core Infrastructure API (FastAPI, SQLAlchemy, Kafka, Vault)
│   ├── identity-go/         # Enterprise IAM Service (Golang, gRPC, JWT)
│   └── ai-ops-python/       # LLM Root Cause Analysis Service (FastAPI, Langchain, Kafka)
├── infrastructure/
│   ├── aws/                 # Terraform configurations (EKS IRSA)
│   ├── helm/                # Kubernetes Helm Charts for dynamic deployment
│   └── monitoring/          # Grafana, Prometheus, Loki, Blackbox configurations
├── shared/                  # Shared Protobufs (gRPC definitions)
├── tests/                   # Cypress E2E Automation tests
├── docker-compose.yml       # Local development stack (12+ Containers)
└── .github/workflows/       # CI/CD Pipelines (Testing, Docker Build, Helm Deploy)
```

---

## 🚀 Getting Started (Local Development)

### Prerequisites
- Docker Engine & Docker Compose V2
- Python 3.11+
- Go 1.23+
- Node.js 20+
- Minimum 8GB RAM available for Docker (required for Kafka & Vault).

### 1. Spin up the Infrastructure
Bring up the entire microservice and observability stack via Docker Compose:

```bash
docker-compose up -d
```

**Services Exposed:**
- **NOC Dashboard**: `http://localhost:3000`
- **Admin Portal**: `http://localhost:3001`
- **Python Core API**: `http://localhost:8000`
- **AI Ops API**: `http://localhost:8002`
- **Grafana**: `http://localhost:3003` (Admin / Admin)
- **Jaeger UI**: `http://localhost:16686`
- **Prometheus**: `http://localhost:9090`
- **HashiCorp Vault**: `http://localhost:8200`

### 2. Microservice Development
To run a service locally outside of Docker (for debugging):

**Python Core API**:
```bash
cd services/backend-python
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Go Identity Service**:
```bash
cd services/identity-go
go run cmd/server/main.go
```

**Vue Admin Portal**:
```bash
cd apps/admin-vue
npm install
npm run dev
```

---

## 🛡️ Enterprise Security Posture

- **Stateless Authentication**: Utilizes asymmetric JWT signing validated over secure internal gRPC channels.
- **Dynamic Secrets**: HashiCorp Vault is integrated via the `hvac` Python client to ensure that the core backend dynamically retrieves database credentials, eliminating static secrets in source code or `EnvVars`.
- **Cloud Native IRSA**: Terraform definitions are provided (`infrastructure/aws/iam/eks_irsa.tf`) to map Kubernetes Service Accounts to AWS IAM Roles via OpenID Connect (OIDC), ensuring absolute least-privilege access to cloud resources.

---

## 🤖 AI-Assisted Operations (AIOps)

The platform features a decoupled event-driven AI engine.
1. When an infrastructure alert fires, the Core API publishes an `ALERT_TRIGGERED` event to **Apache Kafka**.
2. The `ai-ops-python` consumer asynchronously reads the event.
3. The AI engine performs simulated **Retrieval-Augmented Generation (RAG)** by pulling similar past incidents.
4. An LLM calculates a **Root Cause Hypothesis** and a list of **Recommended Actions**, publishing the resolution back to the event bus (`RCA_COMPLETED`).
