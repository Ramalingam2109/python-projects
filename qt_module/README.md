# 🖥️ Qt Module Applications

A collection of PyQt5-based desktop applications including a digital clock and stopwatch. These applications demonstrate GUI development with Python and Qt framework.

## Applications Included

### 1. ⏰ Digital Clock
**Location**: `digital_clock/Digitlal_clock.py`

A sleek digital clock application with a black background and green text, perfect for desktop display.

**Features**:
- Real-time clock updates
- 12/24-hour format support (12-hour with AM/PM)
- Minimalist design
- Auto-updates every second
- Customizable styling

### 2. ⏱️ Stopwatch
**Location**: `Stop_Watch/stop-watch.py`

A precision stopwatch application with start, stop, and reset functionality. Displays time in HH:MM:SS.mm format.

**Features**:
- Start/Stop/Reset controls
- Millisecond precision (10ms intervals)
- Clean, modern interface
- Real-time updates
- Button state management

## Requirements

- Python 3.6 or higher
- `PyQt5` - GUI framework

## Installation

### Install Dependencies

**Option 1: Using requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Manual installation**
```bash
pip install PyQt5
```

The applications will automatically attempt to install PyQt5 if it's not found.

## Usage

### Digital Clock

```bash
cd digital_clock
python Digitlal_clock.py
```

**Features**:
- Displays current time in HH:MM:SS AM/PM format
- Updates every second
- Black background with green text
- Resizable window

### Stopwatch

```bash
cd Stop_Watch
python stop-watch.py
```

**How to Use**:
1. Click **Start** to begin timing
2. Click **Stop** to pause
3. Click **Reset** to reset to 00:00:00.00
4. Time displays in HH:MM:SS.mm format

## Project Structure

```
qt_module/
├── digital_clock/
│   ├── Digitlal_clock.py
│   ├── image.png
│   └── readme.md
├── Stop_Watch/
│   ├── stop-watch.py
│   ├── image.png
│   └── readme.md
├── requirements.txt
└── README.md
```

## Code Structure

### Digital Clock

**DigitalClock Class**:
- `__init__()`: Initializes timer and UI
- `initUI()`: Sets up the interface and styling
- `update_time()`: Updates displayed time every second

**Key Components**:
- `QTimer`: Updates clock every 1000ms (1 second)
- `QLabel`: Displays the time
- `QTime.currentTime()`: Gets current system time

### Stopwatch

**StopWatch Class**:
- `__init__()`: Initializes timer and UI components
- `initUI()`: Sets up buttons and layout
- `start()`: Starts the stopwatch
- `stop()`: Stops the stopwatch
- `reset()`: Resets to zero
- `format_time()`: Formats time display
- `update_display()`: Updates display every 10ms

**Key Components**:
- `QTimer`: Updates every 10ms for precision
- `QTime`: Tracks elapsed time
- `QPushButton`: Start, Stop, Reset buttons
- `QLabel`: Displays formatted time

## Customization

### Digital Clock Customization

**Change Time Format**:
```python
# 24-hour format
current_time = QTime.currentTime().toString("hh:mm:ss")

# 12-hour format (current)
current_time = QTime.currentTime().toString("hh:mm:ss AP")
```

**Change Colors**:
```python
self.time_label.setStyleSheet("""
    font-size: 80px;
    color: #00ff00;  # Change to your preferred color
""")
self.setStyleSheet("background-color: #000000;")  # Background color
```

**Change Font Size**:
```python
font-size: 80px;  # Adjust as needed
```

### Stopwatch Customization

**Change Update Interval**:
```python
self.timer.start(10)  # 10ms = 0.01 seconds
# Change to 100 for 0.1 second precision
```

**Change Time Format**:
```python
# Current: HH:MM:SS.mm
return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

# Alternative: MM:SS.mm (for shorter times)
return f"{minutes:02}:{seconds:02}.{milliseconds:02}"
```

**Modify Button Styles**:
```python
self.setStyleSheet("""
    QPushButton {
        font-size: 30px;  # Adjust size
        background-color: #your-color;  # Change color
    }
""")
```

## PyQt5 Basics

### Key Concepts

1. **QApplication**: Main application object
2. **QWidget**: Base class for all UI elements
3. **QLayout**: Arranges widgets (QVBoxLayout, QHBoxLayout)
4. **QTimer**: Handles timed events
5. **Signals and Slots**: Event handling mechanism

### Example: Creating a Simple Window

```python
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("My App")
window.show()
sys.exit(app.exec_())
```

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'PyQt5'"**
   ```bash
   pip install PyQt5
   ```

2. **Application Won't Close**
   - Use `sys.exit(app.exec_())` to properly exit
   - Press Ctrl+C in terminal if needed

3. **Window Not Showing**
   - Ensure `window.show()` is called
   - Check if QApplication is created before widgets

4. **Timer Not Working**
   - Ensure `timer.start()` is called
   - Check timeout connection: `timer.timeout.connect(function)`

## Learning Resources

### PyQt5 Documentation
- [Official PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Qt for Python](https://doc.qt.io/qtforpython/)

### Tutorials
- PyQt5 tutorial series
- Qt Designer for visual UI design
- Signals and slots mechanism

## Future Enhancements

Potential improvements:
- **Digital Clock**:
  - Multiple time zones
  - Alarm functionality
  - Custom themes
  - System tray integration

- **Stopwatch**:
  - Lap time functionality
  - Multiple timers
  - History/logging
  - Export times

## License

This project is open source and available for educational purposes.

---

**Build beautiful desktop applications! 🖥️**

