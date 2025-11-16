# 🌤️ Weather App

A beautiful PyQt5 desktop application to fetch and display weather information for any city using the OpenWeatherMap API. Features a modern, responsive UI with real-time weather data.

## Features

- 🎨 Modern, responsive PyQt5 interface
- 🌍 Search weather for any city worldwide
- 🌡️ Temperature display in Celsius and Fahrenheit
- 😊 Weather condition emojis
- 📍 City and country display
- 🛡️ Comprehensive error handling
- ⚡ Real-time weather updates
- 🎯 User-friendly design

## Requirements

- Python 3.6 or higher
- `PyQt5` - GUI framework
- `requests` - HTTP library
- OpenWeatherMap API key (free)

## Installation

### 1. Install Dependencies

**Option 1: Using requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Manual installation**
```bash
pip install PyQt5 requests
```

### 2. Get API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Replace the API key in `weather_app.py`:

```python
api_key = 'YOUR_API_KEY_HERE'  # Line 150
```

## Usage

```bash
python weather_app.py
```

### How to Use

1. Launch the application
2. Enter a city name in the input field
3. Click "Get Weather" button
4. View weather information displayed

## Features in Detail

### Weather Information Displayed

- **Temperature**: In both Celsius and Fahrenheit
- **Weather Description**: Current conditions (e.g., "Clear Sky", "Light Rain")
- **Location**: City name and country code
- **Visual Indicator**: Emoji representing weather condition

### Weather Emojis

The app displays appropriate emojis based on weather conditions:
- ☀️ Clear sky
- ⛅ Few clouds
- ☁️ Overcast
- 🌧️ Rain
- ⛈️ Thunderstorm
- ❄️ Snow
- 🌫️ Mist/Fog
- 🌪️ Extreme weather

## Project Structure

```
Weather_app/
├── weather_app.py    # Main application file
├── requirements.txt  # Dependencies
└── README.md        # This file
```

## Code Structure

### WeatherApp Class

- `__init__()`: Initializes UI components
- `initUI()`: Sets up the user interface and styling
- `get_details()`: Fetches weather data from API
- `display_weather()`: Displays weather information
- `display_error()`: Shows error messages
- `get_weather_emoji()`: Returns emoji based on weather ID

## API Information

### OpenWeatherMap API

- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **Parameters**: 
  - `q`: City name
  - `appid`: Your API key
- **Response**: JSON with weather data

### Free Tier Limits

- 60 calls/minute
- 1,000,000 calls/month
- Perfect for personal use

## Error Handling

The application handles various errors:

- **400 Bad Request**: Invalid input
- **401 Unauthorized**: Invalid API key
- **404 Not Found**: City not found
- **500 Server Error**: API server issues
- **Connection Error**: No internet connection
- **Timeout**: Request timeout

## Customization

### Change Temperature Unit

Modify the display in `display_weather()`:

```python
# Show only Celsius
self.temprature_label.setText(f"{temperature_c:.1f}°C")

# Show only Fahrenheit
self.temprature_label.setText(f"{temperature_f:.0f}°F")
```

### Modify UI Colors

Edit the stylesheet in `initUI()`:

```python
self.setStyleSheet('''
    QWidget {
        background-color: #your-color;
    }
    ...
''')
```

### Add More Weather Details

Extend `display_weather()` to show:
- Humidity
- Wind speed
- Pressure
- Visibility
- Sunrise/Sunset times

## Troubleshooting

### Common Issues

1. **"Invalid API Key" Error**
   - Verify your API key is correct
   - Check if API key is activated

2. **"City Not Found" Error**
   - Check city name spelling
   - Try using city,country format (e.g., "London,UK")

3. **Application Won't Start**
   - Ensure PyQt5 is installed: `pip install PyQt5`
   - Check Python version (3.6+)

4. **No Weather Data**
   - Check internet connection
   - Verify API key has remaining calls

## Screenshots

The app features:
- Clean, modern interface
- Large, readable temperature display
- Intuitive input field
- Prominent "Get Weather" button
- Color-coded weather emojis

## Future Enhancements

Potential features:
- 5-day weather forecast
- Hourly weather updates
- Weather alerts
- Multiple city favorites
- Weather history
- Dark mode
- Location-based weather (GPS)

## License

This project is open source and available for educational purposes.

---

**Stay informed about the weather! 🌤️**

