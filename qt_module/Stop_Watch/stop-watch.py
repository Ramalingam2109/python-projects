# stop watch program using pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class Stop_watch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        # Create the main vertical layout
        vbox = QVBoxLayout()

        # Add the time label (centered)
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label)

        # Create a horizontal layout for buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # Add the button layout (hbox) to the main vertical layout (vbox)
        vbox.addLayout(hbox)

        # Set the main layout for the widget
        self.setLayout(vbox)

        # Apply stylesheet
        self.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                font-weight: bold;
                padding: 10px;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
                padding: 20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)
        self.stop_button.setEnabled(True)

    def stop(self):
        self.timer.stop()
        self.stop_button.setDisabled(True)

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()  # Corrected method name
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"  # Corrected formatting

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stop_watch()
    stopwatch.show()
    sys.exit(app.exec_())
