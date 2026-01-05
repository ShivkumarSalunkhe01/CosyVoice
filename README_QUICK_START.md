# CosyVoice Quick Start Guide

This guide will help you get started with CosyVoice quickly.

## Step 1: Download Models

First, download the pretrained models:

```bash
# For users in China (using ModelScope)
python download_models.py --source modelscope

# For overseas users (using HuggingFace)
python download_models.py --source huggingface
```

We strongly recommend downloading **Fun-CosyVoice3-0.5B** for the best performance.

## Step 2: Check Installation

Verify that models are downloaded correctly:

```bash
python quick_start.py --check-models
```

## Step 3: Run Examples

### Basic Usage

Run the basic example to see CosyVoice in action:

```bash
python quick_start.py --example
```

Or run directly:

```bash
python example.py
```

This will demonstrate:
- CosyVoice3 zero-shot voice cloning
- Fine-grained control (breath markers)
- Instruct mode (dialect and speed control)

### Web Demo

Start an interactive web interface:

```bash
# Use default model (auto-detects best available)
python quick_start.py --web-demo

# Or specify a model explicitly
python quick_start.py --web-demo --model pretrained_models/CosyVoice-300M-SFT

# Or use a custom port
python quick_start.py --web-demo --port 8080
```

Or run directly:

```bash
# Using CosyVoice-300M (default)
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M

# Using CosyVoice-300M-SFT for SFT inference
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M-SFT

# Using CosyVoice-300M-Instruct for instruct inference
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M-Instruct

# Using Fun-CosyVoice3-0.5B (recommended)
python3 webui.py --port 50000 --model_dir pretrained_models/Fun-CosyVoice3-0.5B
```

Then open your browser and navigate to `http://localhost:50000`

## Step 4: vLLM Setup (Optional)

vLLM provides faster inference for CosyVoice2/3. To set up vLLM:

```bash
# For vLLM 0.11.0+ (V1 engine) - recommended
bash setup_vllm.sh

# For vLLM 0.9.0 (legacy)
bash setup_vllm.sh 0.9.0
```

This will create a new conda environment `cosyvoice_vllm` to avoid conflicts.

**Important Notes:**
- vLLM requires GPU with CUDA support
- Creates a separate environment to avoid dependency conflicts
- Older vLLM versions (<0.9.0) are not supported
- Versions between 0.9.0 and 0.11.0 are not tested

After setup, activate the environment and test:

```bash
conda activate cosyvoice_vllm
python vllm_example.py
```

## Available Models

| Model | Description | Recommended For |
|-------|-------------|-----------------|
| Fun-CosyVoice3-0.5B | Latest model, best performance | Production use |
| CosyVoice2-0.5B | Version 2.0, streaming support | Streaming applications |
| CosyVoice-300M | Base model | General purpose |
| CosyVoice-300M-SFT | Fine-tuned with speaker data | Pre-trained speaker voices |
| CosyVoice-300M-Instruct | Instruction-tuned | Natural language control |

## Troubleshooting

### Models not found
- Make sure you've run `download_models.py` first
- Check that models are in `pretrained_models/` directory
- Verify download completed successfully

### Import errors
- Ensure you've installed all requirements: `pip install -r requirements.txt`
- Make sure you're in the correct conda environment
- Check that `third_party/Matcha-TTS` submodule is initialized

### vLLM issues
- vLLM requires specific hardware (GPU with CUDA)
- Use the regular `cosyvoice` environment if vLLM doesn't work
- Make sure you're using a supported vLLM version (0.9.0 or 0.11.0+)

### Web demo not starting
- Check if the port is already in use
- Try a different port: `--port 8080`
- Verify the model directory exists and is valid

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [example.py](example.py) for code examples
- Visit the [demo website](https://funaudiollm.github.io/cosyvoice3/) for more examples
- Explore advanced usage in `examples/` directory

## Getting Help

- GitHub Issues: https://github.com/FunAudioLLM/CosyVoice/issues
- Check the FAQ: [FAQ.md](FAQ.md)

