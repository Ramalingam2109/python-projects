import sys, os
try:
    import requests
except:
    os.system('python -m pip install requests')
try: 
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
    from PyQt5.QtCore import Qt  # Import Qt for alignment constants
except:
    os.system('python -m pip install PyQt5')
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
    from PyQt5.QtCore import Qt  # Import Qt for alignment constants
    
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
        api_key = 'e3476649856a7567b6f87637e8caff41'
        city =  self.city_input.text()
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # to get request code which gets passed using the request module . 
            data =response.json()
            if data["cod"] == 200:
                self.display_weather(data)
            else:
                print(data)
        except requests.exceptions.HTTPError:   #exception type -1 
            match response.status_code:
                case 400:
                    self.display_error("Bad Request: \n Plz check ur input")
                case 401:
                    self.display_error("Unauthorized or Invalud API Key ")
                case 403:
                    self.display_error("Forbidden error: \naccess is denied")
                case 404:
                    self.display_error("Not found: \nLocation not found ")
                case 500:
                    self.display_error("Server Error:\n Please try again Later    ")
                case 502:
                    self.display_error("Bad Gateway:\n Invalid response from server ")
                case 503:
                    self.display_error("Service Unavailable:\n Server is down  ")
                case 504:
                    self.display_error("GateWay timeout \n No ")
                case _:
                    self.display_error("HTTP error occured")
                    
        except requests.exceptions.ConnectionError: # exception type  - 2 
            self.display_error("Connection Error: \n Check your internet connection")
            
        except requests.exceptions.Timeout: # exception type  - 3
            self.display_error(f"Timeout Error: \n The request timed out ")
            
        except requests.exceptions.TooManyRedirects:# exception type  - 4
            self.display_error(f"Too many redirects: Check the URL")
        
        except requests.exceptions.RequestException as req_error:  # exception type  - 5
            print(f"Request error {req_error}")
        
        
        
    def display_error(self,message):
        self.temprature_label.setStyleSheet("font-size :30px;")
        self.temprature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()    
    
    def display_weather(self,data):
        self.temprature_label.setStyleSheet("font-size :75px;")
        temprature_k = data["main"]["temp"]
        temprature_c = temprature_k -273
        temprature_f = (temprature_k *9/5) -459.67
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.temprature_label.setText(f"{temprature_f:.0f}°F")
        self.description_label.setText(f"{weather_description}")
        self.emoji_label
    
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
        
        
        
        
if __name__ =="__main__":
    app =  QApplication(sys.argv)
    Weather_app =WeatherApp()
    Weather_app.show()
    sys.exit(app.exec_())
    