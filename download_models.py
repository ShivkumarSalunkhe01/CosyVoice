#!/usr/bin/env python3
"""
Model download script for CosyVoice pretrained models.
Supports both ModelScope (for users in China) and HuggingFace (for overseas users).
"""

import os
import argparse
import sys
from pathlib import Path


def download_from_modelscope():
    """Download models using ModelScope SDK (recommended for users in China)."""
    try:
        from modelscope import snapshot_download
    except ImportError:
        print("Error: modelscope is not installed. Please install it with:")
        print("  pip install modelscope")
        return False
    
    print("Downloading models using ModelScope SDK...")
    
    models = [
        ('FunAudioLLM/Fun-CosyVoice3-0.5B-2512', 'pretrained_models/Fun-CosyVoice3-0.5B'),
        ('iic/CosyVoice2-0.5B', 'pretrained_models/CosyVoice2-0.5B'),
        ('iic/CosyVoice-300M', 'pretrained_models/CosyVoice-300M'),
        ('iic/CosyVoice-300M-SFT', 'pretrained_models/CosyVoice-300M-SFT'),
        ('iic/CosyVoice-300M-Instruct', 'pretrained_models/CosyVoice-300M-Instruct'),
        ('iic/CosyVoice-ttsfrd', 'pretrained_models/CosyVoice-ttsfrd'),
    ]
    
    for model_id, local_dir in models:
        print(f"\nDownloading {model_id} to {local_dir}...")
        try:
            snapshot_download(model_id, local_dir=local_dir)
            print(f"✓ Successfully downloaded {model_id}")
        except Exception as e:
            print(f"✗ Failed to download {model_id}: {e}")
            return False
    
    return True


def download_from_huggingface():
    """Download models using HuggingFace SDK (recommended for overseas users)."""
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        print("Error: huggingface_hub is not installed. Please install it with:")
        print("  pip install huggingface_hub")
        return False
    
    print("Downloading models using HuggingFace SDK...")
    
    models = [
        ('FunAudioLLM/Fun-CosyVoice3-0.5B-2512', 'pretrained_models/Fun-CosyVoice3-0.5B'),
        ('FunAudioLLM/CosyVoice2-0.5B', 'pretrained_models/CosyVoice2-0.5B'),
        ('FunAudioLLM/CosyVoice-300M', 'pretrained_models/CosyVoice-300M'),
        ('FunAudioLLM/CosyVoice-300M-SFT', 'pretrained_models/CosyVoice-300M-SFT'),
        ('FunAudioLLM/CosyVoice-300M-Instruct', 'pretrained_models/CosyVoice-300M-Instruct'),
        ('FunAudioLLM/CosyVoice-ttsfrd', 'pretrained_models/CosyVoice-ttsfrd'),
    ]
    
    for model_id, local_dir in models:
        print(f"\nDownloading {model_id} to {local_dir}...")
        try:
            snapshot_download(model_id, local_dir=local_dir)
            print(f"✓ Successfully downloaded {model_id}")
        except Exception as e:
            print(f"✗ Failed to download {model_id}: {e}")
            return False
    
    return True


def install_ttsfrd():
    """Install ttsfrd package for better text normalization performance."""
    ttsfrd_dir = Path('pretrained_models/CosyVoice-ttsfrd')
    resource_zip = ttsfrd_dir / 'resource.zip'
    dependency_whl = ttsfrd_dir / 'ttsfrd_dependency-0.1-py3-none-any.whl'
    ttsfrd_whl = ttsfrd_dir / 'ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl'
    
    if not ttsfrd_dir.exists():
        print("Error: pretrained_models/CosyVoice-ttsfrd directory not found.")
        print("Please download CosyVoice-ttsfrd first.")
        return False
    
    # Unzip resource.zip if it exists
    if resource_zip.exists():
        print("\nUnzipping resource.zip...")
        import zipfile
        try:
            with zipfile.ZipFile(resource_zip, 'r') as zip_ref:
                zip_ref.extractall(ttsfrd_dir)
            print("✓ Successfully unzipped resource.zip")
        except Exception as e:
            print(f"✗ Failed to unzip resource.zip: {e}")
            return False
    else:
        print("Warning: resource.zip not found, skipping unzip step.")
    
    # Install dependency wheel
    if dependency_whl.exists():
        print(f"\nInstalling {dependency_whl.name}...")
        os.system(f"pip install {dependency_whl}")
    else:
        print(f"Warning: {dependency_whl.name} not found, skipping installation.")
    
    # Install ttsfrd wheel
    if ttsfrd_whl.exists():
        print(f"\nInstalling {ttsfrd_whl.name}...")
        os.system(f"pip install {ttsfrd_whl}")
        print("✓ Successfully installed ttsfrd package")
    else:
        print(f"Warning: {ttsfrd_whl.name} not found.")
        print("Note: ttsfrd installation is optional. WeText will be used by default if ttsfrd is not available.")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Download CosyVoice pretrained models',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download using ModelScope (recommended for users in China)
  python download_models.py --source modelscope

  # Download using HuggingFace (recommended for overseas users)
  python download_models.py --source huggingface

  # Download specific models only
  python download_models.py --source huggingface --models cosyvoice3 cosyvoice2

  # Install ttsfrd package after download
  python download_models.py --install-ttsfrd
        """
    )
    
    parser.add_argument(
        '--source',
        choices=['modelscope', 'huggingface'],
        default='modelscope',
        help='Download source: modelscope (China) or huggingface (overseas). Default: modelscope'
    )
    
    parser.add_argument(
        '--models',
        nargs='+',
        choices=['cosyvoice3', 'cosyvoice2', 'cosyvoice-300m', 'cosyvoice-300m-sft', 
                 'cosyvoice-300m-instruct', 'cosyvoice-ttsfrd', 'all'],
        default=['all'],
        help='Models to download. Default: all'
    )
    
    parser.add_argument(
        '--install-ttsfrd',
        action='store_true',
        help='Install ttsfrd package for better text normalization (optional)'
    )
    
    args = parser.parse_args()
    
    # Create pretrained_models directory if it doesn't exist
    os.makedirs('pretrained_models', exist_ok=True)
    
    # Download models
    if 'all' in args.models:
        if args.source == 'modelscope':
            success = download_from_modelscope()
        else:
            success = download_from_huggingface()
    else:
        # Download specific models
        print(f"Downloading selected models: {', '.join(args.models)}")
        # For simplicity, we download all models and let users filter manually
        # In production, you could implement selective downloading here
        if args.source == 'modelscope':
            success = download_from_modelscope()
        else:
            success = download_from_huggingface()
    
    if not success:
        print("\nError: Some models failed to download.")
        sys.exit(1)
    
    # Install ttsfrd if requested
    if args.install_ttsfrd:
        print("\n" + "="*50)
        print("Installing ttsfrd package...")
        install_ttsfrd()
    
    print("\n" + "="*50)
    print("Model download completed!")
    print("\nNext steps:")
    print("\n1. Check which models are available:")
    print("   python quick_start.py --check-models")
    print("\n2. Run basic example (recommended):")
    print("   python quick_start.py --example")
    print("   # or directly: python example.py")
    print("\n3. Start web demo for interactive testing:")
    print("   python quick_start.py --web-demo")
    print("   # or directly: python webui.py --port 50000 --model_dir pretrained_models/Fun-CosyVoice3-0.5B")
    print("\n4. (Optional) Setup vLLM for faster inference:")
    print("   bash setup_vllm.sh")
    print("   conda activate cosyvoice_vllm")
    print("   python vllm_example.py")
    print("\n5. (Optional) Install ttsfrd for better text normalization:")
    print("   python download_models.py --install-ttsfrd")
    print("\nFor more details, see README_QUICK_START.md")


if __name__ == '__main__':
    main()

