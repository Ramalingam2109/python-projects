"""
Digital Clock
A PyQt5-based digital clock application with a sleek black background and green text.
"""

import sys
import os

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
    from PyQt5.QtCore import QTime, QTimer, Qt
except ImportError:
    print("Installing PyQt5 library...")
    os.system(f'{sys.executable} -m pip install PyQt5')
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
    from PyQt5.QtCore import QTime, QTimer, Qt


class DigitalClock(QWidget):
    """Digital clock widget that displays current time."""
    
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 400, 150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 80px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            color: #00ff00;
            padding: 20px;
        """)
        
        self.setStyleSheet("background-color: #000000;")
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        self.update_time()

    def update_time(self):
        """Update the displayed time."""
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())