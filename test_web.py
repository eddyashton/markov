#!/usr/bin/env python3

# Simple test to verify the web server components work
import sys
import os

print("Testing web server components...")

try:
    # Test Flask import
    from flask import Flask

    print("✓ Flask imported successfully")

    # Test markov imports
    from _markov.io import save_model, load_model
    from _markov.train import train_model
    from _markov.generate import generate_value

    print("✓ Markov modules imported successfully")

    # Test data directory
    if os.path.exists("data"):
        data_files = [f for f in os.listdir("data") if f.endswith(".txt")]
        print(f"✓ Data directory found with {len(data_files)} .txt files: {data_files}")
    else:
        print("✗ Data directory not found")

    # Test models directory
    if os.path.exists("models"):
        model_files = [f for f in os.listdir("models") if f.endswith(".json")]
        print(
            f"✓ Models directory found with {len(model_files)} .json files: {model_files}"
        )
    else:
        print("✓ Models directory not found (will be created as needed)")

    # Test templates directory
    if os.path.exists("templates/index.html"):
        print("✓ Templates directory and index.html found")
    else:
        print("✗ Templates directory or index.html not found")

    print("\nAll components ready! You can start the web server with:")
    print("  python web_server.py")
    print("Then open: http://localhost:5000")

except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
