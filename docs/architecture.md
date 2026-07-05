# Infrastructure Provisioning Agent Architecture

Self-service infrastructure provisioning agent that translates service requests into cloud resources using IaC templates, enforces guardrails, tracks provisioning state, and manages resource lifecycle with automated decommissioning.

## Domain Tools

- **provision_resource**: Provision a cloud resource from a catalog template
- **validate_request**: Validate provisioning request against guardrails and quotas
- **estimate_cost**: Estimate monthly cost before provisioning
- **track_provisioning**: Track status of an in-progress provisioning
- **decommission_resource**: Safely decommission and clean up a resource
- **list_catalog**: List available self-service resource templates