# Infrastructure Provisioning Agent

[![CI](https://github.com/kogunlowo123/infrastructure-provisioning-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/infrastructure-provisioning-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Self-service infrastructure provisioning agent that translates service requests into cloud resources using IaC templates, enforces guardrails, tracks provisioning state, and manages resource lifecycle with automated decommissioning.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `provision_resource` | Provision a cloud resource from a catalog template |
| `validate_request` | Validate provisioning request against guardrails and quotas |
| `estimate_cost` | Estimate monthly cost before provisioning |
| `track_provisioning` | Track status of an in-progress provisioning |
| `decommission_resource` | Safely decommission and clean up a resource |
| `list_catalog` | List available self-service resource templates |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/provision` | Provision a new resource |
| `GET` | `/api/v1/provision/{request_id}/status` | Check provisioning status |
| `POST` | `/api/v1/validate` | Validate provisioning request |
| `POST` | `/api/v1/estimate` | Estimate resource cost |
| `GET` | `/api/v1/catalog` | List resource catalog |
| `POST` | `/api/v1/decommission` | Decommission resource |

## Features

- Self Service Provisioning
- Guardrail Enforcement
- Lifecycle Management
- Cost Estimation
- Approval Workflows

## Integrations

- Terraform Cli
- Aws Provider
- Azure Provider
- Gcp Provider
- Servicenow

## Architecture

```
infrastructure-provisioning-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── infrastructure_provisioning_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Terraform + Pulumi + CloudFormation**

---

Built as part of the Enterprise AI Agent Platform.
