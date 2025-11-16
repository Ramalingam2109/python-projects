"""
Weather App
A PyQt5-based desktop application to fetch and display weather information for any city.
"""

import sys
import os

try:
    import requests
except ImportError:
    print("Installing requests library...")
    os.system(f'{sys.executable} -m pip install requests')
    import requests

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
    from PyQt5.QtCore import Qt
except ImportError:
    print("Installing PyQt5 library...")
    os.system(f'{sys.executable} -m pip install PyQt5')
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
    from PyQt5.QtCore import Qt
    
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the City :",self)
        self.city_input = QLineEdit("",self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temprature_label =QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label =QLabel( self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        
        # creating widgets for each text or property 
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temprature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        self.setLayout(vbox)
        
        # setting layout and alignment for each column using Qt module 
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        # self.get_weather_button.setAlignment(Qt.AlignCenter)
        self.temprature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        
        # creating a id (CSS Property for passing informaration on Click )
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        # styling using css 
        
        self.setStyleSheet('''
            /* Base Styling */
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            /* City Label */
            QLabel#city_label {
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
            
            /* City Input Field */
            QLineEdit#city_input {
                font-size: 24px;
                padding: 12px;
                border: 2px solid #3498db;
                border-radius: 8px;
                background-color: white;
                color: #34495e;
            }
            
            /* Button */
            QPushButton#get_weather_button {
                font-size: 20px;
                font-weight: bold;
                padding: 15px;
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                border: none;
            }
            
            QPushButton#get_weather_button:hover {
                background-color: #2980b9;
            }
            
            QPushButton#get_weather_button:pressed {
                background-color: #1a5276;
            }
            
            /* Temperature Display */
            QLabel#temperature_label {
                font-size: 72px;
                font-weight: bold;
                color: #e74c3c;
                qproperty-alignment: 'AlignCenter';
            }
            
            /* Emoji Display */
            QLabel#emoji_label {
                font-size: 64px;
                qproperty-alignment: 'AlignCenter';
                padding: 20px;
            }
            
            /* Weather Description */
            QLabel#description_label {
                font-size: 24px;
                color: #7f8c8d;
                qproperty-alignment: 'AlignCenter';
            }
            
            /* Error Messages */
            QLabel.error {
                font-size: 18px;
                color: #e74c3c;
                background-color: #fadbd8;
                padding: 10px;
                border-radius: 5px;
            }
        ''')
        self.get_weather_button.clicked.connect(self.get_details)
        
    def get_details(self):
        """Fetch weather details for the entered city."""
        # Note: Replace with your own API key from openweathermap.org
        api_key = 'e3476649856a7567b6f87637e8caff41'
        city = self.city_input.text().strip()
        
        if not city:
            self.display_error("Please enter a city name")
            return
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get("cod") == 200:
                self.display_weather(data)
            else:
                self.display_error(f"Error: {data.get('message', 'Unknown error')}")
                
        except requests.exceptions.HTTPError as e:
            status_code = response.status_code
            error_messages = {
                400: "Bad Request:\nPlease check your input",
                401: "Unauthorized:\nInvalid API Key",
                403: "Forbidden:\nAccess is denied",
                404: "Not Found:\nLocation not found",
                500: "Server Error:\nPlease try again later",
                502: "Bad Gateway:\nInvalid response from server",
                503: "Service Unavailable:\nServer is down",
                504: "Gateway Timeout:\nRequest timed out"
            }
            self.display_error(error_messages.get(status_code, f"HTTP Error {status_code}"))
                    
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
            
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
            
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL")
        
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{str(req_error)}")
        
        
        
    def display_error(self,message):
        self.temprature_label.setStyleSheet("font-size :30px;")
        self.temprature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()    
    
    def display_weather(self, data):
        """Display weather information in the UI."""
        self.temprature_label.setStyleSheet("font-size: 75px; color: #e74c3c;")
        
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        
        weather_description = data["weather"][0]["description"].title()
        weather_id = data["weather"][0]["id"]
        city_name = data["name"]
        country = data["sys"].get("country", "")
        
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.temprature_label.setText(f"{temperature_c:.1f}°C / {temperature_f:.0f}°F")
        self.description_label.setText(f"{city_name}, {country}\n{weather_description}")
    
    @staticmethod
    def get_weather_emoji(weather_id):
        
        match weather_id:
            case _ if 200 <= weather_id <= 232:  # Thunderstorm
                return "⛈️"
            case _ if 300 <= weather_id <= 321:  # Drizzle
                return "🌧️"
            case _ if 500 <= weather_id <= 531:  # Rain
                return "🌧️" if weather_id < 520 else "⛈️"
            case _ if 600 <= weather_id <= 622:  # Snow
                return "❄️" if weather_id < 615 else "🌨️"
            case _ if 701 <= weather_id <= 721:  # Atmosphere (Mist/Fog/Haze)
                return "🌫️"
            case 711:  # Smoke
                return "💨"
            case 731 | 761:  # Dust/Sand
                return "🌪️"
            case 762:  # Ash
                return "🌋"
            case 771:  # Squalls
                return "🌬️"
            case 781:  # Tornado
                return "🌪️"
            case 800:  # Clear
                return "☀️"
            case _ if 801 <= weather_id <= 804:  # Clouds
                return "⛅" if weather_id == 801 else "☁️"
            case _:
                return "❓"  # Unknown weather condition
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    