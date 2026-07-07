# Enterprise Identity & Cloud Observability Platform

![Version](https://img.shields.io/badge/version-v3.0.0--enterprise-blue)
![Architecture](https://img.shields.io/badge/architecture-microservices-orange)
![Identity](https://img.shields.io/badge/identity-oauth2_oidc-success)
![Kubernetes](https://img.shields.io/badge/kubernetes-helm-informational)
![AI Ops](https://img.shields.io/badge/AI-LLM_RCA-purple)

A Fortune 500-grade, event-driven **Identity & Access Management (IAM)** and Cloud Infrastructure Observability platform. 

This platform is designed specifically to demonstrate deep expertise in the domains of Modern Identity (JumpCloud, Okta), Cloud Engineering, Security Engineering, Distributed Systems, and DevOps. It utilizes a microservices architecture communicating asynchronously over Apache Kafka and synchronously over gRPC and REST APIs.

---

## 📸 Platform Previews

Here is a look at the various operations dashboards and portals included in this platform:

### Network Operations Center (NOC) Dashboard
![NOC Dashboard UI](docs/frontend_ui.png)

### Server & Infrastructure Management
![Servers UI](docs/servers_ui.png)

### Active Incident Tracking
![Incidents UI](docs/incidents_ui.png)

### IT Ticketing & Support System
![Tickets UI](docs/tickets_ui.png)

---

## 🌟 Core Features & Modules

### 1. Modern Identity & Security
- **OAuth2 & OIDC**: Full authorization code flows, Access/Refresh tokens, and Token Revocation endpoints built in Go.
- **Device Management**: API endpoints for Device Registration, Trust Status, OS Health, and Policy Assignment.
- **Session Management**: Endpoints for Active Sessions, Terminate Session, and Concurrent Login Detection.
- **Dynamic Security**: AWS Secrets Manager integration for dynamic credential retrieval. AWS IAM Roles for Service Accounts (IRSA) via OIDC Federation.

### 2. Distributed Architecture
- **Event-Driven Microservices**: Powered by Apache Kafka (KRaft mode), ensuring highly scalable, asynchronous communication between nodes.
- **Micro-frontends & Dual UIs**: 
  - **Identity Portal (Vue 3)**: Administration for users, devices, policies, and audit logs.
  - **Operations Dashboard (React)**: SRE & NOC operations, metrics, and incident management.

### 3. AI & Deep Observability
- **AI-Assisted Operations (AIOps)**: A specialized Python microservice performing LLM-assisted Root Cause Analysis (RCA), Runbook Generation, and Natural Language Log Explanation.
- **The Three Pillars of Observability**: 
  - **Metrics**: Prometheus, Alertmanager & Grafana.
  - **Traces**: OpenTelemetry (OTel) distributed tracing via Jaeger.
  - **Logs**: Centralized, structured log aggregation via Grafana Loki & Promtail.

---

## 🏗️ Architecture Diagram

```mermaid
graph TD
    %% Frontends
    Client(["Web / Mobile Client"])
    NOC["React NOC Dashboard\n(Port 3000)"]
    Admin["Vue 3 Identity Portal\n(Port 3001)"]
    
    %% API Gateway
    Ingress{{"API Gateway / NGINX"}}
    
    %% Microservices
    API["Python Core API\nFastAPI / Port 8000"]
    Identity["Go Identity Engine\ngRPC / Port 50051"]
    AIOps["AI Ops API\nFastAPI / Port 8002"]
    
    %% Event Streaming
    Kafka{"Apache Kafka\n(KRaft Mode)"}
    
    %% Databases & Secrets
    DB[("PostgreSQL")]
    Redis[("Redis Cache")]
    AWS["AWS Secrets Manager"]
    
    %% Observability Stack
    Prometheus("Prometheus")
    Alertmanager("Alertmanager")
    Grafana("Grafana")
    Jaeger("Jaeger\nOTel Tracing")
    Loki("Grafana Loki\nLog Aggregation")
    
    %% Routing
    Client --> NOC
    Client --> Admin
    NOC --> Ingress
    Admin --> Ingress
    Ingress --> API
    Ingress --> Identity
    
    %% Microservice Comms
    API -- "gRPC Auth" --> Identity
    API -- "Fetch Creds" --> AWS
    API -- "Publish Events" --> Kafka
    Identity -- "Publish Audit Logs" --> Kafka
    Kafka -- "Consume Events" --> AIOps
    AIOps -- "Publish AI Insights" --> Kafka
    
    %% Data Persistence
    API --> DB
    API --> Redis
    Identity --> DB
    
    %% Telemetry
    API -. "OTLP Traces" .-> Jaeger
    Identity -. "OTLP Traces" .-> Jaeger
    API -. "/metrics" .-> Prometheus
    Prometheus --> Alertmanager
    Grafana -. "Queries Data" .-> Prometheus
    Grafana -. "Queries Logs" .-> Loki
    Grafana -. "Queries Traces" .-> Jaeger
```

---

## 📂 Repository Structure (Monorepo)

```text
observability-platform/
├── apps/
│   ├── dashboard-react/     # React NOC Operations Dashboard (Vite + Tailwind)
│   └── identity-vue/        # Vue 3 Identity Administration Portal (Vite + TS)
├── services/
│   ├── api-python/          # Core Infrastructure API (FastAPI, SQLAlchemy, Kafka, AWS Secrets)
│   ├── identity-go/         # Enterprise IAM Service (Golang, gRPC, OAuth2, Device Trust)
│   └── aiops-python/        # LLM Root Cause Analysis Service (FastAPI, Langchain, Kafka)
├── gateway/                 # API Gateway Configurations (NGINX/Envoy)
├── shared/                  
│   └── protobuf/            # Shared Protobufs (OAuth2, Sessions, Devices)
├── infra/
│   ├── helm/                # Kubernetes Helm Charts for dynamic deployment
│   └── monitoring/          # Grafana, Prometheus, Alertmanager, Loki configurations
├── tests/                   # Cypress E2E Automation tests
├── docker-compose.yml       # Local development stack (Kafka KRaft, Monitoring, DBs)
└── .github/workflows/       # CI/CD Pipelines (Testing, Docker Build, Helm Deploy)
```

---

## 🚀 Getting Started (Local Development)

### Prerequisites
Ensure you have the following installed on your machine before proceeding:
- **Docker Engine & Docker Compose V2** (Minimum 8GB RAM allocated to Docker)
- **Python 3.11+**
- **Go 1.23+**
- **Node.js 20+**

### 1. Spin up the Infrastructure
Bring up the entire microservice and observability stack locally via Docker Compose. This includes Kafka, PostgreSQL, Redis, and all observability tools.

```bash
docker-compose up -d
```

**Services Exposed Locally:**
- **NOC Dashboard (React)**: `http://localhost:3000`
- **Identity Portal (Vue 3)**: `http://localhost:3001`
- **Python Core API (FastAPI)**: `http://localhost:8000`
- **AI Ops API**: `http://localhost:8002`
- **Grafana**: `http://localhost:3003` *(Credentials: Admin / Admin)*
- **Jaeger UI**: `http://localhost:16686`
- **Prometheus**: `http://localhost:9090`

### 2. Microservice Development
To run a service locally outside of Docker (for step-through debugging):

**Go Identity Service (gRPC):**
```bash
cd services/identity-go
go run cmd/server/main.go
```

**Python Core API (FastAPI):**
```bash
cd services/api-python
python -m venv venv
source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. Frontend Development
**Run the React Dashboard:**
```bash
cd apps/dashboard-react
npm install
npm run dev
```

---

## 🧪 Testing & CI/CD

The platform enforces strict quality via GitHub Actions.

- **Enterprise CI Pipeline**: Runs on every push to `main` and `develop`. It includes:
  - Unit Tests for the Go Identity Service (`go test`)
  - Unit Tests for the Python Backend (`pytest` + `alembic` migrations testing)
  - Linting for both React and Vue frontends
- **Enterprise CD Pipeline**: Automatically builds and pushes Docker images to Amazon ECR, and handles continuous deployment using Helm on AWS EKS. (Currently disabled for local demo purposes).
