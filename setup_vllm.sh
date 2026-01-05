#!/bin/bash
# Setup script for vLLM support with CosyVoice
# This script creates a new conda environment for vLLM to avoid conflicts

set -e

echo "=========================================="
echo "CosyVoice vLLM Setup Script"
echo "=========================================="
echo ""

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "Error: conda is not installed or not in PATH"
    echo "Please install conda first: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Check if base cosyvoice environment exists
if ! conda env list | grep -q "cosyvoice "; then
    echo "Warning: 'cosyvoice' environment not found."
    echo "Please create it first by running:"
    echo "  conda create -n cosyvoice -y python=3.10"
    echo "  conda activate cosyvoice"
    echo "  pip install -r requirements.txt"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

ENV_NAME="cosyvoice_vllm"
VLLM_VERSION="${1:-0.11.0}"  # Default to 0.11.0, can pass 0.9.0 as argument

echo "Creating conda environment: $ENV_NAME"
echo "Cloning from: cosyvoice"
echo "vLLM version: $VLLM_VERSION"
echo ""

# Clone the environment
conda create -n "$ENV_NAME" --clone cosyvoice -y

echo ""
echo "Activating environment: $ENV_NAME"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

echo ""
echo "Installing vLLM and dependencies..."

if [ "$VLLM_VERSION" == "0.9.0" ]; then
    echo "Installing vLLM 0.9.0 (legacy)..."
    pip install vllm==0.9.0 transformers==4.51.3 numpy==1.26.4 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
else
    echo "Installing vLLM $VLLM_VERSION (V1 engine)..."
    pip install "vllm==${VLLM_VERSION}" transformers==4.57.1 numpy==1.26.4 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
fi

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To activate the environment, run:"
echo "  conda activate $ENV_NAME"
echo ""
echo "To test vLLM with CosyVoice, run:"
echo "  python vllm_example.py"
echo ""
echo "Note: vLLM requires specific hardware (GPU with CUDA support)."
echo "If your hardware doesn't support vLLM, you can continue using"
echo "the regular 'cosyvoice' environment without vLLM."

