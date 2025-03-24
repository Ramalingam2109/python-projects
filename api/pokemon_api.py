
# connecting with api's

import os
try:
    import requests
except:
    os.system('python -m pip install requests')
    import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemom_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        print("data received")
        return pokemon_data
    else:
        print(f"failed to retreive data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemom_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"].capitalize()}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")
    print(f"{pokemon_info["weight"]}")