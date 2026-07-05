#!/bin/bash
set -euo pipefail
echo "Setting up Infrastructure Provisioning Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
