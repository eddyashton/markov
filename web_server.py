#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import tempfile
import shutil

from _markov.io import save_model, load_model
from _markov.train import train_model
from _markov.generate import generate_value
import random

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/data-files")
def get_data_files():
    """Get list of available data files"""
    try:
        data_dir = "data"
        if not os.path.exists(data_dir):
            return jsonify({"error": "Data directory not found"}), 404

        files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/model-files")
def get_model_files():
    """Get list of available model files"""
    try:
        models_dir = "models"
        if not os.path.exists(models_dir):
            return jsonify({"files": []})

        files = [f for f in os.listdir(models_dir) if f.endswith(".json")]
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/train-and-generate", methods=["POST"])
def train_and_generate():
    """Train a model and generate values"""
    try:
        data = request.json
        input_file = data.get("input_file")
        n = data.get("n", 1)
        seeds = data.get("seeds", [])

        if not input_file:
            return jsonify({"error": "Input file is required"}), 400

        # Check if file exists
        file_path = f"data/{input_file}"
        if not os.path.exists(file_path):
            return jsonify({"error": f"File {input_file} not found"}), 404

        # Train the model
        model = train_model(file_path)

        # Generate values
        results = []

        # Generate random values if n is specified
        if n and n > 0:
            for i in range(n):
                seed = int(random.random() * 1000)
                value = generate_value(model, seed)
                results.append(
                    {"type": "random", "index": i + 1, "seed": seed, "value": value}
                )

        # Generate from specific seeds
        if seeds:
            for seed in seeds:
                # Pass seed directly - Python's random.seed() accepts strings
                value = generate_value(model, seed)
                results.append({"type": "seeded", "seed": seed, "value": value})

        return jsonify(
            {
                "success": True,
                "results": results,
                "model_trained": True,
                "model_data": model,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/train-only", methods=["POST"])
def train_only():
    """Train a model and save it to file"""
    try:
        data = request.json
        input_file = data.get("input_file")
        model_file = data.get("model_file")

        if not input_file:
            return jsonify({"error": "Input file is required"}), 400
        if not model_file:
            # Use default model file name if not provided
            model_file = "model.json"

        # Ensure model file has .json extension
        if not model_file.endswith(".json"):
            model_file += ".json"

        # Check if input file exists
        file_path = f"data/{input_file}"
        if not os.path.exists(file_path):
            return jsonify({"error": f"File {input_file} not found"}), 404

        # Train the model
        model = train_model(file_path)

        # Save the model
        model_path = f"models/{model_file}"
        save_model(model, model_path)

        return jsonify(
            {
                "success": True,
                "message": f"Model trained and saved to {model_file}",
                "model_file": model_file,
                "model_data": model,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/generate-only", methods=["POST"])
def generate_only():
    """Generate values from a saved model"""
    try:
        data = request.json
        model_file = data.get("model_file")
        n = data.get("n", 1)
        seeds = data.get("seeds", [])

        if not model_file:
            return jsonify({"error": "Model file is required"}), 400

        # Check if model file exists
        model_path = f"models/{model_file}"
        if not os.path.exists(model_path):
            return jsonify({"error": f"Model file {model_file} not found"}), 404

        # Load the model
        model = load_model(model_path)

        # Generate values
        results = []

        # Generate random values if n is specified
        if n and n > 0:
            for i in range(n):
                seed = int(random.random() * 1000)
                value = generate_value(model, seed)
                results.append(
                    {"type": "random", "index": i + 1, "seed": seed, "value": value}
                )

        # Generate from specific seeds
        if seeds:
            for seed in seeds:
                # Pass seed directly - Python's random.seed() accepts strings
                value = generate_value(model, seed)
                results.append({"type": "seeded", "seed": seed, "value": value})

        return jsonify(
            {"success": True, "results": results, "model_loaded": model_file}
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/data/<filename>")
def serve_data_file(filename):
    """Serve data files"""
    return send_from_directory("data", filename)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
