# 🎮 Pokemon API Client

A simple Python client to fetch and display Pokemon information from the PokeAPI. Learn about RESTful API consumption with Python while exploring Pokemon data.

## Features

- 🔍 Search Pokemon by name (case-insensitive)
- 📊 Display comprehensive Pokemon information
- 🎨 Formatted output with stats, types, and abilities
- 🛡️ Comprehensive error handling
- 🌐 HTTP request management
- ⚡ Automatic dependency installation

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

### Install Dependencies

**Option 1: Using requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Manual installation**
```bash
pip install requests
```

The program will automatically attempt to install `requests` if it's not found.

## Usage

```bash
python pokemon_api.py
```

### Example Usage

```
==================================================
Pokemon API Client
==================================================

Enter Pokemon name (or press Enter for Pikachu): charizard

==================================================
Pokemon: Charizard
==================================================
ID: 6
Height: 1.7 m
Weight: 90.5 kg
Type(s): Fire, Flying
Abilities: Blaze, Solar Power

Base Stats:
  Hp: 78
  Attack: 84
  Defense: 78
  Special Attack: 109
  Special Defense: 85
  Speed: 100
```

## API Information

This project uses the [PokeAPI](https://pokeapi.co/) - a free, open-source RESTful API that provides Pokemon data.

- **Base URL**: `https://pokeapi.co/api/v2/`
- **Endpoint**: `/pokemon/{name}`
- **Rate Limiting**: No authentication required, but be respectful with requests

## Available Information

For each Pokemon, you can access:
- **Basic Info**: Name, ID, Height, Weight
- **Types**: Elemental types (Fire, Water, Grass, etc.)
- **Abilities**: Special abilities
- **Base Stats**: HP, Attack, Defense, Special Attack, Special Defense, Speed
- **Moves**: Available moves (can be added to the code)
- **Sprites**: Images (can be added to the code)

## Code Structure

- `BASE_URL`: PokeAPI base URL
- `get_pokemon_info(name)`: Fetches Pokemon data from API
- `display_pokemon_info(pokemon_data)`: Formats and displays information
- `main()`: Main program loop

## Error Handling

The program handles:
- **404 Errors**: Pokemon not found
- **Network Errors**: Connection issues
- **Timeout Errors**: Request timeouts
- **Invalid API Responses**: Malformed data
- **Keyboard Interrupts**: Ctrl+C

## Customization

You can extend the program to display:
- Pokemon sprites/images
- Move lists
- Evolution chains
- Location data
- Game appearances

### Example: Adding Sprite Display

```python
sprite_url = pokemon_data['sprites']['front_default']
print(f"Sprite: {sprite_url}")
```

## API Response Structure

The API returns JSON with the following structure:
```json
{
  "id": 6,
  "name": "charizard",
  "height": 17,
  "weight": 905,
  "types": [...],
  "abilities": [...],
  "stats": [...],
  "sprites": {...}
}
```

## Learning Points

This project demonstrates:
- Making HTTP GET requests
- JSON data parsing
- Error handling for API calls
- User input validation
- Data formatting and display

## Rate Limiting

While PokeAPI doesn't require authentication, please:
- Don't make excessive requests
- Cache results when possible
- Respect the API's terms of service

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install requests with `pip install requests`
2. **Connection Error**: Check your internet connection
3. **404 Error**: Verify the Pokemon name is spelled correctly
4. **Timeout**: The API might be slow; the program has a 10-second timeout

## License

This project is open source and available for educational purposes.

The PokeAPI is provided by [PokeAPI](https://pokeapi.co/) and is free to use.

---

**Catch 'em all! 🎮**

