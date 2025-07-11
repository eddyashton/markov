# Markov Chain Web Frontend

A web-based interface for the Markov chain generator that provides an intuitive way to train models and generate values.

## Features

- **🎨 Modern Web Interface**: Clean, responsive design with intuitive controls
- **📊 Three Operation Modes**: 
  - Train & Generate: Train a model and immediately generate values
  - Train Only: Train a model and save it to a file
  - Generate Only: Load a saved model and generate values
- **📁 File Management**: Automatic discovery of data files and saved models
- **🔢 Flexible Generation**: Support for both random and seeded generation
- **📱 Responsive Design**: Works on desktop and mobile devices

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Web Server**:
   ```bash
   python web_server.py
   ```

3. **Open Browser**: Navigate to `http://localhost:5000`

## Usage

### Train & Generate Mode
- Select an input data file from the dropdown
- Set the number of random generations (optional)
- Enter deterministic seeds for reproducible results (optional)
- Click "Train & Generate" to train the model and generate values

### Train Only Mode
- Select an input data file from the dropdown
- Enter a name for the output model file
- Click "Train Model" to train and save the model

### Generate Only Mode
- Select a previously saved model file
- Set the number of random generations (optional)
- Enter deterministic seeds for reproducible results (optional)
- Click "Generate Values" to generate from the saved model

## API Endpoints

The web server provides the following REST API endpoints:

- `GET /api/data-files` - Returns list of available data files
- `GET /api/model-files` - Returns list of saved model files
- `POST /api/train-and-generate` - Train and generate values
- `POST /api/train-only` - Train and save model
- `POST /api/generate-only` - Generate from saved model

## File Structure

```
markov/
├── web_server.py          # Flask web server
├── templates/
│   └── index.html        # Main web interface
├── data/                 # Input data files (.txt)
├── models/               # Saved model files (.json)
├── requirements.txt      # Python dependencies
└── _markov/             # Core markov modules
    ├── train.py
    ├── generate.py
    └── io.py
```

## Input Format

- **Data Files**: Plain text files with one entry per line
- **Seeds**: Can be entered one per line or comma-separated
- **Model Files**: JSON files automatically saved/loaded

## CLI Equivalent

This web interface provides the same functionality as the command-line tool:

```bash
# Train & Generate
python markov.py train_and_generate data/names.txt -n 5 seed1 seed2

# Train Only  
python markov.py train data/names.txt models/names.json

# Generate Only
python markov.py generate models/names.json -n 3 seed1 seed2
```

## Development

The web frontend is built with:
- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Styling**: Modern CSS with gradients and transitions
- **API**: RESTful JSON endpoints

## Configuration

- **Port**: Server runs on port 5000 by default
- **File Limits**: 16MB maximum file upload size
- **Directories**: 
  - `data/` for input files
  - `models/` for saved models
  - `templates/` for HTML templates

## Tips

- Use the Train & Generate mode for quick experiments
- Save models with Train Only mode for reuse
- Use specific seeds for reproducible results
- The interface automatically refreshes file lists when new files are added
- Results show both the generated values and their corresponding seeds

Enjoy using the Markov Chain Web Frontend! 🚀
