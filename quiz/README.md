# Data Source Quiz

An interactive web-based quiz that tests your ability to identify which data file an entry comes from.

## About

This quiz presents you with random entries from four different data sources:
- **Roman Emperors** - Historical emperor names from `emperors.txt`
- **Modern Names** - Contemporary names from `names.txt`
- **Shakespeare Quotes** - Lines from Shakespeare's works from `shakespeare.txt`
- **Town Names** - British town and place names from `towns.txt`

Your task is to correctly identify which file each entry originated from.

## Features

- 🎯 **Interactive Quiz**: Click to select your answer
- 📊 **Real-time Statistics**: Track your accuracy and progress
- 🎨 **Modern UI**: Clean, responsive design
- 🔄 **Endless Questions**: Keep playing to improve your score
- 📈 **Progress Tracking**: Visual accuracy indicator

## How to Play

1. **Start the Server**: Run `python server.py` in your terminal
2. **Open Browser**: Navigate to `http://localhost:8000`
3. **Read the Entry**: Each question shows a random entry from one of the data files
4. **Make Your Guess**: Click on the button corresponding to the data source you think it came from
5. **See Results**: Get immediate feedback on whether you were correct
6. **Continue Playing**: Click "Next Question" to continue improving your score

## Running the Quiz

### Option 1: Using Python Server (Recommended)
```bash
python server.py
```
Then open `http://localhost:8000` in your browser.

### Option 2: Using Any HTTP Server
You can use any local HTTP server. For example:
```bash
# Using Python's built-in server
python -m http.server 8000

# Using Node.js http-server (if installed)
npx http-server

# Using PHP's built-in server
php -S localhost:8000
```

## Data Sources

The quiz uses four text files from the `data/` directory:
- `emperors.txt` - 166 Roman emperor names
- `names.txt` - 2,454 modern names
- `shakespeare.txt` - 25,722 lines from Shakespeare's works
- `towns.txt` - 37,174 British town and place names

## Technical Details

- **Frontend**: Pure HTML, CSS, and JavaScript
- **Backend**: Simple Python HTTP server for local development
- **Data Loading**: Asynchronous fetch of text files
- **Responsive Design**: Works on desktop and mobile devices

## Tips for Success

- **Emperors**: Look for classical Roman names like "Constantinus", "Alexius", "Basil"
- **Names**: Modern names are typically shorter and more familiar
- **Shakespeare**: Look for archaic language, quotes, and poetic phrasing
- **Towns**: British place names often have distinctive patterns and endings

Good luck with the quiz! 🎉
