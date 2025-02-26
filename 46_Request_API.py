# How to connect to an API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    
    response = requests.get(url)    
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
        
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info =  get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['id']}")
    print(f"Weight: {pokemon_info['height']}")
    