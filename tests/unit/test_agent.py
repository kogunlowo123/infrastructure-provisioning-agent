"""Infrastructure Provisioning Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_provision_resource():
    """Test Provision a cloud resource from a catalog template."""
    tools = AgentTools()
    result = await tools.provision_resource(resource_type="test", parameters="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_request():
    """Test Validate provisioning request against guardrails and quotas."""
    tools = AgentTools()
    result = await tools.validate_request(request="test", policy_set="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_estimate_cost():
    """Test Estimate monthly cost before provisioning."""
    tools = AgentTools()
    result = await tools.estimate_cost(resource_spec="test", region="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_provisioning():
    """Test Track status of an in-progress provisioning."""
    tools = AgentTools()
    result = await tools.track_provisioning(request_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.infrastructure_provisioning_agent_agent import InfrastructureProvisioningAgentAgent
    agent = InfrastructureProvisioningAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
