# Data Source Quiz

An interactive web-based quiz that tests your ability to identify which data file an entry comes from.

## About

This quiz dynamically discovers and presents you with random entries from text files in the `data/` directory. By default, it includes:
- `emperors.txt` - Historical emperor names
- `names.txt` - Contemporary names
- `poems.txt` - First lines of poems
- `shakespeare.txt` - Lines from Shakespeare's works
- `towns.txt` - British town and place names
- **And any other .txt files** - The quiz automatically discovers new data files

Your task is to correctly identify which file each entry originated from.

## Features

- 🎯 **Interactive Quiz**: Click to select your answer
- 📊 **Real-time Statistics**: Track your overall accuracy and progress
- 📈 **Per-File Statistics**: See detailed stats for each data source (even files with no answers yet)
- 🎛️ **Data Source Filtering**: Select which data sources to include in your quiz
- 🔄 **Dynamic File Discovery**: Automatically detects new or removed data files
- 🎨 **Modern UI**: Clean, responsive design with dense statistics display
- 🔄 **Endless Questions**: Keep playing to improve your score
- 📈 **Progress Tracking**: Visual accuracy indicators for overall and per-file performance

## How to Play

1. **Start the Server**: Run `python server.py` in your terminal
2. **Open Browser**: Navigate to `http://localhost:8000`
3. **Select Data Sources**: Use the checkboxes to choose which data files to include in your quiz
4. **Read the Entry**: Each question shows a random entry from one of the active data sources
5. **Make Your Guess**: Click on the button corresponding to the data source you think it came from
6. **See Results**: Get immediate feedback on whether you were correct
7. **Track Progress**: Monitor your per-file statistics in the dense grid display
8. **Continue Playing**: Click "Next Question" to continue improving your score

## Key Features Explained

### Data Source Filtering
- **Selective Testing**: Choose which data sources to include in your quiz
- **Dynamic Options**: Only selected sources appear as answer choices
- **Flexible Learning**: Focus on specific data types or test all sources

### Per-File Statistics
- **Comprehensive Tracking**: See statistics for every data file, even unused ones
- **Dense Display**: Compact grid showing correct/total answers and accuracy percentages
- **Visual Progress**: Color-coded accuracy bars for each file
- **Real-time Updates**: Statistics update immediately after each answer

### Dynamic File Discovery
- **Auto-Detection**: Quiz automatically finds all `.txt` files in the `data/` directory
- **No Configuration**: Simply add new files to the data directory and they'll appear
- **Fallback Support**: Uses hardcoded files if dynamic discovery fails

## Running the Quiz

### Option 1: Using Python Server (Recommended)
```bash
python server.py
```
Then open `http://localhost:8000` in your browser.

The Python server provides:
- Static file serving for the quiz interface
- `/api/data-files` endpoint for dynamic file discovery
- CORS support for local development
- Automatic data directory access

### Option 2: Using Any HTTP Server
You can use any local HTTP server, but you'll lose dynamic file discovery:
```bash
# Using Python's built-in server
python -m http.server 8000

# Using Node.js http-server (if installed)
npx http-server

# Using PHP's built-in server
php -S localhost:8000
```

## Data Sources

The quiz dynamically discovers all `.txt` files in the `data/` directory. Default files include:
- `emperors.txt` - 166 Roman emperor names
- `names.txt` - 2,454 modern names
- `poems.txt` - Poetry and verse entries
- `shakespeare.txt` - 25,722 lines from Shakespeare's works
- `towns.txt` - 37,174 British town and place names

**Adding New Data Sources:**
1. Create a new `.txt` file in the `data/` directory
2. Add one entry per line
3. Restart the server (if using the Python server)
4. The new file will automatically appear in the quiz filter options

## Technical Details

- **Frontend**: Pure HTML, CSS, and JavaScript
- **Backend**: Simple Python HTTP server with API endpoints
- **Data Loading**: Asynchronous fetch of text files with dynamic discovery
- **Responsive Design**: Works on desktop and mobile devices
- **Statistics**: Real-time tracking with persistent per-file metrics
- **UI**: Dense, grid-based statistics display with visual progress indicators

## API Endpoints

- `GET /api/data-files` - Returns JSON list of available data files
- `GET /data/<filename>` - Serves individual data files
- `GET /` - Serves the main quiz interface

## Tips for Success

- **emperors.txt**: Look for classical Roman names like "Constantinus", "Alexius", "Basil"
- **names.txt**: Modern names are typically shorter and more familiar
- **poems.txt**: Look for poetic language, verse structure, and literary themes
- **shakespeare.txt**: Look for archaic language, quotes, and poetic phrasing
- **towns.txt**: British place names often have distinctive patterns and endings
- **Use Filters**: Start with fewer sources to learn patterns, then add more for challenge
- **Monitor Stats**: Use the per-file statistics to identify your weak areas

Good luck with the quiz! 🎉
