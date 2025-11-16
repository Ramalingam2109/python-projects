"""
Pokemon API Client
A simple client to fetch and display Pokemon information from the PokeAPI.
"""

import os
import sys

try:
    import requests
except ImportError:
    print("Installing requests library...")
    os.system(f'{sys.executable} -m pip install requests')
    import requests

BASE_URL = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    """
    Fetch Pokemon information from the PokeAPI.
    
    Args:
        name: Pokemon name (case-insensitive)
    
    Returns:
        dict: Pokemon data if successful, None otherwise
    """
    url = f"{BASE_URL}pokemon/{name.lower()}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        pokemon_data = response.json()
        return pokemon_data
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"❌ Pokemon '{name}' not found.")
        else:
            print(f"❌ HTTP Error {response.status_code}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return None


def display_pokemon_info(pokemon_data):
    """Display formatted Pokemon information."""
    if not pokemon_data:
        return
    
    print("\n" + "=" * 50)
    print(f"Pokemon: {pokemon_data['name'].capitalize()}")
    print("=" * 50)
    print(f"ID: {pokemon_data['id']}")
    print(f"Height: {pokemon_data['height'] / 10:.1f} m")
    print(f"Weight: {pokemon_data['weight'] / 10:.1f} kg")
    
    # Display types
    types = [t['type']['name'] for t in pokemon_data['types']]
    print(f"Type(s): {', '.join(types).title()}")
    
    # Display abilities
    abilities = [a['ability']['name'] for a in pokemon_data['abilities']]
    print(f"Abilities: {', '.join(abilities).title()}")
    
    # Display base stats
    print("\nBase Stats:")
    for stat in pokemon_data['stats']:
        stat_name = stat['stat']['name'].replace('-', ' ').title()
        print(f"  {stat_name}: {stat['base_stat']}")


def main():
    """Main function to run the Pokemon API client."""
    print("=" * 50)
    print("Pokemon API Client")
    print("=" * 50)
    
    pokemon_name = input("\nEnter Pokemon name (or press Enter for Pikachu): ").strip()
    if not pokemon_name:
        pokemon_name = "pikachu"
    
    pokemon_info = get_pokemon_info(pokemon_name)
    
    if pokemon_info:
        display_pokemon_info(pokemon_info)
    else:
        print("Failed to retrieve Pokemon information.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")