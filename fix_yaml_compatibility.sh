#!/bin/bash
# Fix script for ruamel.yaml compatibility issue with HyperPyYAML
# This downgrades ruamel.yaml to a compatible version

echo "=========================================="
echo "Fixing ruamel.yaml compatibility issue"
echo "=========================================="
echo ""
echo "This will install ruamel.yaml < 0.18.0 which is compatible"
echo "with HyperPyYAML 1.2.2"
echo ""

pip install "ruamel.yaml<0.18.0"

echo ""
echo "=========================================="
echo "Fix completed!"
echo "=========================================="
echo ""
echo "You can now try running the example again:"
echo "  python quick_start.py --example"

