"""Test configuration for Infrastructure Provisioning Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "infrastructure-provisioning-agent", "category": "DevOps & Platform Engineering"}
