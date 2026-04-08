FinPilot AI

Production-Grade AI Wealth Management Platform with Advisory Assistant
FinPilot AI is an enterprise-grade, cloud-native AI Wealth Management platform designed to simulate a real-world fintech system. The platform demonstrates advanced DevOps practices, scalable microservices architecture, AI integration, GitOps delivery, and production-level observability.
---
Key Highlights
Production-grade microservices architecture
AWS EKS-based scalable deployment
Terraform-managed infrastructure (IaC)
GitHub Actions CI pipelines
ArgoCD GitOps continuous delivery
Redis for caching and session management
MySQL for transactional data storage
Datadog for monitoring, logging, and APM
AI-powered recommendation engine
Conversational advisory assistant (FinPilot Advisor)
---
Architecture Overview
The platform follows a layered microservices architecture:
User → Frontend → ALB → API Services → Business Services → Redis / MySQL / AI Engine
Core Components
Frontend (React + NGINX)
Backend Microservices (Python)
AI Services (Recommendation, Risk, Forecasting)
Advisory Assistant (Chat-based AI interface)
Redis (Caching, Sessions, Rate Limiting)
MySQL (Transactional Database)
Kubernetes (EKS)
CI/CD (GitHub Actions + ArgoCD)
Observability (Datadog)
---
Microservices
auth-service
user-service
portfolio-service
transaction-service
recommendation-service
market-data-service
notification-service
advisory-assistant-service
---
Advisory Assistant (FinPilot Advisor)
The Advisory Assistant provides a conversational interface for users to:
Understand portfolio performance
Get investment recommendations
Analyze risk profiles
Plan financial goals
Receive simplified market insights
Design Principles
Data-driven responses (no hallucination)
Controlled advisory layer (no direct execution)
Redis-based session memory
MySQL audit logging
Observability via Datadog
---
Technology Stack
Cloud & Infrastructure
AWS (EKS, ECR, VPC, RDS, S3, IAM)
DevOps
Git
GitHub Actions
Terraform
ArgoCD
Containers & Orchestration
Docker
Kubernetes
Backend & AI
Python (FastAPI)
AI/ML logic (rule-based + lightweight models)
Data Layer
MySQL
Redis
Observability
Datadog (APM, Logs, Metrics)
---
CI/CD Workflow
Code pushed to GitHub
GitHub Actions pipeline runs:
Linting
Testing
Security scanning
Docker build
Image pushed to ECR
GitOps repo updated
ArgoCD sync triggers deployment to EKS
---
Infrastructure Design
Terraform modules:
VPC
EKS Cluster
IAM Roles
ECR Repositories
RDS MySQL
S3 Buckets
Secrets Management
State management:
S3 backend
DynamoDB locking
---
Kubernetes Design
Namespaces (dev, stage, prod)
Deployments and Services
ALB Ingress
ConfigMaps and Secrets
Horizontal Pod Autoscaler (HPA)
Pod Disruption Budgets (PDB)
Resource limits and requests
---
Observability
Datadog is used for:
Infrastructure monitoring
Kubernetes metrics
Application performance (APM)
Log aggregation
Distributed tracing
Alerting
---
Security
IAM least privilege
IRSA for pod access
Secrets Manager integration
Kubernetes RBAC
Network policies
Secure CI/CD pipelines
---
Folder Structure
```
finpilot-ai-app/
finpilot-ai-infra/
finpilot-ai-gitops/
```
---
Implementation Phases
Architecture design
Infrastructure provisioning (Terraform)
Core service development
AI service integration
Chatbot implementation
Dockerization and Helm charts
CI/CD setup
GitOps deployment
Observability integration
Security hardening
---
Resume Summary
Designed and implemented a production-grade AI Wealth Management platform using AWS EKS, Terraform, Docker, Kubernetes, Redis, MySQL, GitHub Actions, ArgoCD, and Datadog. Built scalable microservices, AI-driven recommendation systems, GitOps-based CI/CD pipelines, and a conversational advisory assistant.
---
Conclusion
FinPilot AI demonstrates real-world DevOps engineering capabilities, combining cloud-native design, automation, observability, and AI integration in a fintech-grade architecture.
This project is ideal for showcasing:
DevOps expertise
Cloud architecture skills
Kubernetes production experience
CI/CD and GitOps knowledge
AI-enabled platform design