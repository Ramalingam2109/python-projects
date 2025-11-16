# Python Projects Collection 🐍

A comprehensive collection of Python projects showcasing various programming concepts, algorithms, GUI applications, web development, and API integrations. This repository contains beginner to intermediate-level projects perfect for learning and portfolio building.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [Command-Line Applications](#command-line-applications)
  - [GUI Applications](#gui-applications)
  - [Web Applications](#web-applications)
  - [Algorithms](#algorithms)
  - [API Integrations](#api-integrations)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains a diverse set of Python projects covering:
- **Game Development**: Interactive console games
- **GUI Applications**: Desktop applications using PyQt5
- **Web Development**: Django-based web applications
- **Data Structures & Algorithms**: Search and sort implementations
- **API Integration**: RESTful API clients
- **Utilities**: QR code generation, finance tracking

## 🚀 Projects

### Command-Line Applications

#### 🎲 Dice Rolling Simulator
**Location**: `dice-rolling-simulator/`

A fun command-line tool that simulates rolling dice with beautiful ASCII art representation. Roll multiple dice and see the results displayed horizontally.

**Features**:
- ASCII art dice visualization
- Support for multiple dice
- Total calculation
- Input validation

**Usage**:
```bash
cd dice-rolling-simulator
python dice_rolling_asciii.py
```

**See**: [dice-rolling-simulator/README.md](dice-rolling-simulator/README.md) for detailed documentation.

---

#### 🎮 Hangman Game
**Location**: `hangman-game/`

A classic word guessing game where players try to guess a word letter by letter. Features score tracking and multiple rounds.

**Features**:
- Random word selection
- 6 attempts per game
- Score tracking
- Multiple game rounds
- User-friendly interface

**Usage**:
```bash
cd hangman-game
python hangman.py
```

**See**: [hangman-game/README.md](hangman-game/README.md) for detailed documentation.

---

#### 📱 QR Code Generator
**Location**: `qr-code-generator/`

Generate QR codes from text or URLs. Perfect for creating QR codes for websites, contact information, or any text data.

**Features**:
- Generate QR codes from text/URLs
- Custom file naming
- Automatic PNG format
- Error handling

**Dependencies**:
```bash
pip install -r requirements.txt
```

**Usage**:
```bash
cd qr-code-generator
python qr_code_generator.py
```

**See**: [qr-code-generator/README.md](qr-code-generator/README.md) for detailed documentation.

---

#### 💰 Personal Finance Tracker
**Location**: `PERSONAL FINANCE TRACKER/`

A comprehensive command-line application to track income and expenses with CSV storage and data visualization.

**Features**:
- Add income/expense transactions
- Date-based filtering
- Financial summaries (total income, expenses, net savings)
- Data visualization with matplotlib
- CSV data persistence

**Dependencies**:
```bash
pip install -r requirements.txt
```

**Usage**:
```bash
cd "PERSONAL FINANCE TRACKER"
python main.py
```

**See**: [PERSONAL FINANCE TRACKER/README.md](PERSONAL%20FINANCE%20TRACKER/README.md) for detailed documentation.

---

### GUI Applications

#### 🌤️ Weather App
**Location**: `Weather_app/`

A beautiful PyQt5 desktop application to fetch and display weather information for any city using the OpenWeatherMap API.

**Features**:
- Modern, responsive UI
- Real-time weather data
- Temperature in Celsius and Fahrenheit
- Weather condition emojis
- Comprehensive error handling
- City and country display

**Dependencies**:
```bash
pip install -r requirements.txt
```

**Usage**:
```bash
cd Weather_app
python weather_app.py
```

**Note**: You'll need an API key from [OpenWeatherMap](https://openweathermap.org/api). Replace the API key in `weather_app.py`.

**See**: [Weather_app/README.md](Weather_app/README.md) for detailed documentation.

---

#### 🖥️ Qt Module Applications
**Location**: `qt_module/`

A collection of PyQt5-based desktop applications including a digital clock and stopwatch.

**Applications**:
- **Digital Clock** (`digital_clock/`): Real-time clock with minimalist design
- **Stopwatch** (`Stop_Watch/`): Precision stopwatch with millisecond accuracy

**Dependencies**:
```bash
pip install -r requirements.txt
```

**Usage**:
```bash
# Digital Clock
cd qt_module/digital_clock
python Digitlal_clock.py

# Stopwatch
cd qt_module/Stop_Watch
python stop-watch.py
```

**See**: [qt_module/README.md](qt_module/README.md) for detailed documentation.

---

### Web Applications

#### ✅ Django To-Do List
**Location**: `ToDolist-Django/`

A full-featured web-based To-Do List application built with Django featuring user authentication, task management, and a modern Bootstrap UI.

**Features**:
- User registration and authentication
- Create, view, update, and delete tasks
- Task status tracking (In Progress/Completed)
- User-specific task isolation
- Secure password handling
- Responsive Bootstrap design

**Dependencies**:
```bash
pip install Django
```

**Setup**:
```bash
cd ToDolist-Django
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Optional
python manage.py runserver
```

**Access**: Open `http://127.0.0.1:8000/` in your browser

**See**: [ToDolist-Django/README.md](ToDolist-Django/README.md) for detailed documentation.

---

### Algorithms

#### 🔍 Searching Algorithms
**Location**: `searching/`

Implementation of fundamental searching algorithms with examples and explanations.

**Algorithms**:
- **Linear Search** (`linearSearch.py`): O(n) - Works on any array
- **Binary Search** (`binarySearch.py`): O(log n) - Requires sorted array

**Features**:
- Clean, well-documented code
- Multiple examples
- Time complexity information
- Educational comments

**Usage**:
```bash
cd searching
python linearSearch.py
python binarySearch.py
```

**See**: [searching/README.md](searching/README.md) for detailed documentation.

---

#### 📊 Sorting Algorithms
**Location**: `sorting/`

Implementation of classic sorting algorithms with performance analysis.

**Algorithms**:
- **Bubble Sort** (`bubble_sort.py`): O(n²) - Simple but inefficient
- **Selection Sort** (`selection_sort.py`): O(n²) - In-place sorting

**Features**:
- Time and space complexity documentation
- Example usage
- Educational value

**Usage**:
```bash
cd sorting
python bubble_sort.py
python selection_sort.py
```

**See**: [sorting/README.md](sorting/README.md) for detailed documentation.

---

### API Integrations

#### 🎮 Pokemon API Client
**Location**: `api/`

A simple client to fetch and display Pokemon information from the PokeAPI. Learn about RESTful API consumption with Python.

**Features**:
- Fetch Pokemon data by name
- Display stats, types, abilities
- Error handling
- User-friendly output

**Dependencies**:
```bash
pip install -r requirements.txt
```

**Usage**:
```bash
cd api
python pokemon_api.py
```

**See**: [api/README.md](api/README.md) for detailed documentation.

---

## 📁 Project Structure

```
py/
├── dice-rolling-simulator/      # Dice rolling game
│   ├── dice_rolling_asciii.py
│   ├── requirements.txt        # No dependencies
│   └── README.md
├── hangman-game/                # Hangman game
│   ├── hangman.py
│   ├── requirements.txt        # No dependencies
│   └── README.md
├── qr-code-generator/           # QR code generator
│   ├── qr_code_generator.py
│   ├── requirements.txt        # qrcode[pil]
│   └── README.md
├── api/                          # API clients
│   ├── pokemon_api.py
│   ├── requirements.txt        # requests
│   └── README.md
├── PERSONAL FINANCE TRACKER/     # Finance tracker
│   ├── main.py
│   ├── data_entry.py
│   ├── requirements.txt        # pandas, matplotlib
│   └── README.md
├── Weather_app/                 # Weather desktop app
│   ├── weather_app.py
│   ├── requirements.txt        # PyQt5, requests
│   └── README.md
├── qt_module/                    # Qt applications
│   ├── digital_clock/
│   ├── Stop_Watch/
│   ├── requirements.txt        # PyQt5
│   └── README.md
├── searching/                    # Search algorithms
│   ├── linearSearch.py
│   ├── binarySearch.py
│   ├── requirements.txt        # No dependencies
│   └── README.md
├── sorting/                       # Sort algorithms
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── requirements.txt        # No dependencies
│   └── README.md
├── ToDolist-Django/              # Django web app
│   ├── manage.py
│   ├── todoapp/
│   ├── requirements.txt        # Django
│   └── README.md
└── README.md                      # This file
```

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**:
```bash
git clone <repository-url>
cd py
```

2. **Create a virtual environment** (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:

**Each project has its own `requirements.txt` file** for easy dependency management. Navigate to the project folder and install:

```bash
# API projects
cd api
pip install -r requirements.txt

# Weather App
cd Weather_app
pip install -r requirements.txt

# Qt applications
cd qt_module
pip install -r requirements.txt

# Django To-Do List
cd ToDolist-Django
pip install -r requirements.txt

# QR Code Generator
cd qr-code-generator
pip install -r requirements.txt

# Personal Finance Tracker
cd "PERSONAL FINANCE TRACKER"
pip install -r requirements.txt
```

**Note**: Projects without external dependencies (dice-rolling-simulator, hangman-game, searching, sorting) have `requirements.txt` files that indicate no dependencies are needed.

**Or install all common dependencies at once**:
```bash
pip install requests PyQt5 qrcode[pil] pandas matplotlib Django
```

---

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **PyQt5**: GUI framework for desktop applications
- **Django**: Web framework for the To-Do List application
- **Pandas**: Data manipulation for finance tracker
- **Matplotlib**: Data visualization
- **Requests**: HTTP library for API calls
- **QRCode**: QR code generation library
- **SQLite**: Database for Django application

---

## 📝 Usage

Each project is self-contained and can be run independently. Navigate to the project directory and run the main Python file:

```bash
cd <project-folder>
python <project_file>.py
```

For Django projects:
```bash
cd ToDolist-Django
python manage.py runserver
```

**Note**: 
- Each project folder contains its own `README.md` with detailed usage instructions, examples, and customization options
- **All projects have `requirements.txt` files** for easy dependency management - simply run `pip install -r requirements.txt` in each project folder

---

## 🎓 Learning Resources

These projects are excellent for learning:
- **Python Basics**: Variables, functions, loops, conditionals
- **Object-Oriented Programming**: Classes and objects
- **GUI Development**: PyQt5 widgets and layouts
- **Web Development**: Django framework, templates, models
- **API Integration**: HTTP requests, JSON parsing
- **Data Structures**: Lists, dictionaries, sets
- **Algorithms**: Search and sort implementations
- **File Handling**: CSV reading/writing
- **Error Handling**: Try-except blocks, validation

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation
- Add more projects

---

## 📄 License

This project is open source and available for educational purposes. Feel free to use, modify, and distribute as needed.

---

## 👤 Author

Python Projects Collection

---

## 🌟 Features Summary

| Project | Location | Type | Difficulty | Dependencies |
|---------|----------|------|------------|--------------|
| Dice Rolling | `dice-rolling-simulator/` | CLI | Beginner | None |
| Hangman | `hangman-game/` | CLI | Beginner | None |
| QR Code Generator | `qr-code-generator/` | CLI | Beginner | qrcode |
| Finance Tracker | `PERSONAL FINANCE TRACKER/` | CLI | Intermediate | pandas, matplotlib |
| Weather App | `Weather_app/` | GUI | Intermediate | PyQt5, requests |
| Qt Applications | `qt_module/` | GUI | Beginner | PyQt5 |
| Django To-Do | `ToDolist-Django/` | Web | Intermediate | Django |
| Search Algorithms | `searching/` | Algorithm | Beginner | None |
| Sort Algorithms | `sorting/` | Algorithm | Beginner | None |
| Pokemon API | `api/` | API | Beginner | requests |

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the project-specific README files
2. Review the code comments
3. Open an issue on GitHub

---

**Happy Coding! 🚀**
