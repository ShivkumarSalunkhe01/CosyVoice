#!/usr/bin/env python3
"""
Quick start script for CosyVoice.
This script helps you get started with CosyVoice by running examples and tests.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path


def check_model_exists(model_dir):
    """Check if a model directory exists."""
    path = Path(model_dir)
    if not path.exists():
        return False
    # Check if it has some expected files (config.json, model files, etc.)
    if (path / 'config.json').exists() or (path / 'model_config.json').exists():
        return True
    # Check for any .bin or .safetensors files
    if list(path.glob('*.bin')) or list(path.glob('*.safetensors')):
        return True
    return False


def run_basic_example():
    """Run the basic example.py"""
    print("\n" + "="*60)
    print("Running Basic Usage Example")
    print("="*60)
    
    if not Path('example.py').exists():
        print("Error: example.py not found in current directory")
        return False
    
    # Check if recommended model exists
    recommended_model = 'pretrained_models/Fun-CosyVoice3-0.5B'
    if not check_model_exists(recommended_model):
        print(f"Warning: Recommended model '{recommended_model}' not found.")
        print("Please download models first:")
        print("  python download_models.py --source huggingface")
        return False
    
    print("\nRunning example.py...")
    print("This will demonstrate CosyVoice3 usage (recommended).")
    print("\nNote: Generated audio files will be saved in the current directory.")
    print("Press Ctrl+C to stop at any time.\n")
    
    try:
        subprocess.run([sys.executable, 'example.py'], check=True)
        print("\n✓ Example completed successfully!")
        print("Check the generated .wav files in the current directory.")
        return True
    except KeyboardInterrupt:
        print("\n\nExample interrupted by user.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Example failed with error: {e}")
        return False


def run_web_demo(model_dir=None, port=50000):
    """Run the web demo"""
    print("\n" + "="*60)
    print("Starting Web Demo")
    print("="*60)
    
    if not Path('webui.py').exists():
        print("Error: webui.py not found in current directory")
        return False
    
    if model_dir is None:
        # Try to find a suitable model
        models_to_try = [
            'pretrained_models/Fun-CosyVoice3-0.5B',
            'pretrained_models/CosyVoice2-0.5B',
            'pretrained_models/CosyVoice-300M-SFT',
            'pretrained_models/CosyVoice-300M',
            'pretrained_models/CosyVoice-300M-Instruct',
        ]
        
        model_dir = None
        for model in models_to_try:
            if check_model_exists(model):
                model_dir = model
                print(f"Found model: {model_dir}")
                break
        
        if model_dir is None:
            print("Error: No suitable model found.")
            print("Please download models first:")
            print("  python download_models.py --source huggingface")
            return False
    else:
        if not check_model_exists(model_dir):
            print(f"Error: Model directory '{model_dir}' not found or invalid.")
            return False
    
    print(f"\nStarting web demo with model: {model_dir}")
    print(f"Server will be available at: http://localhost:{port}")
    print("Press Ctrl+C to stop the server.\n")
    
    try:
        subprocess.run([
            sys.executable, 'webui.py',
            '--port', str(port),
            '--model_dir', model_dir
        ], check=True)
        return True
    except KeyboardInterrupt:
        print("\n\nWeb demo stopped by user.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Web demo failed with error: {e}")
        return False


def check_models():
    """Check which models are available"""
    print("\n" + "="*60)
    print("Checking Available Models")
    print("="*60)
    
    models = [
        ('Fun-CosyVoice3-0.5B', 'pretrained_models/Fun-CosyVoice3-0.5B'),
        ('CosyVoice2-0.5B', 'pretrained_models/CosyVoice2-0.5B'),
        ('CosyVoice-300M', 'pretrained_models/CosyVoice-300M'),
        ('CosyVoice-300M-SFT', 'pretrained_models/CosyVoice-300M-SFT'),
        ('CosyVoice-300M-Instruct', 'pretrained_models/CosyVoice-300M-Instruct'),
        ('CosyVoice-ttsfrd', 'pretrained_models/CosyVoice-ttsfrd'),
    ]
    
    print("\nModel Status:")
    print("-" * 60)
    available = []
    missing = []
    
    for name, path in models:
        if check_model_exists(path):
            print(f"✓ {name:30} [Available]")
            available.append(name)
        else:
            print(f"✗ {name:30} [Missing]")
            missing.append(name)
    
    print("-" * 60)
    print(f"\nAvailable: {len(available)}/{len(models)}")
    
    if missing:
        print("\nMissing models. Download them with:")
        print("  python download_models.py --source huggingface")
    
    return len(available) > 0


def main():
    parser = argparse.ArgumentParser(
        description='Quick start script for CosyVoice',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check which models are available
  python quick_start.py --check-models

  # Run basic example
  python quick_start.py --example

  # Start web demo with default model
  python quick_start.py --web-demo

  # Start web demo with specific model
  python quick_start.py --web-demo --model pretrained_models/CosyVoice-300M-SFT

  # Start web demo on custom port
  python quick_start.py --web-demo --port 8080
        """
    )
    
    parser.add_argument(
        '--check-models',
        action='store_true',
        help='Check which models are available'
    )
    
    parser.add_argument(
        '--example',
        action='store_true',
        help='Run the basic example.py'
    )
    
    parser.add_argument(
        '--web-demo',
        action='store_true',
        help='Start the web demo'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default=None,
        help='Model directory to use (for web demo)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=50000,
        help='Port for web demo (default: 50000)'
    )
    
    args = parser.parse_args()
    
    # If no arguments, show menu
    if not any([args.check_models, args.example, args.web_demo]):
        print("\n" + "="*60)
        print("CosyVoice Quick Start")
        print("="*60)
        print("\nAvailable options:")
        print("  1. Check available models")
        print("  2. Run basic example")
        print("  3. Start web demo")
        print("\nUsage examples:")
        print("  python quick_start.py --check-models")
        print("  python quick_start.py --example")
        print("  python quick_start.py --web-demo")
        print("\nFor more options, run: python quick_start.py --help")
        return
    
    # Check models first if requested or if needed for other operations
    if args.check_models or args.example or args.web_demo:
        if not check_models():
            print("\nNo models available. Please download models first.")
            return
    
    # Run requested operations
    success = True
    
    if args.example:
        success = run_basic_example() and success
    
    if args.web_demo:
        success = run_web_demo(args.model, args.port) and success
    
    if success:
        print("\n" + "="*60)
        print("All operations completed successfully!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("Some operations failed. Please check the errors above.")
        print("="*60)
        sys.exit(1)


if __name__ == '__main__':
    main()

