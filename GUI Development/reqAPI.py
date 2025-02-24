# How to connect API using python 
import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}" 
    response=requests.get(url)
    if response.status_code==200:
        pokemon_data=response.json() 
        return pokemon_data

    else:
        print(f"Fail to retrieve the data {response.status_code}")



pokemon_name=input("Enter the name of pokemon\n").lower()  # noqa

pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info:
    print("\nPokémon Information:")
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Base Experience: {pokemon_info['base_experience']}")
    print(f"Types: {', '.join(t['type']['name'] for t in pokemon_info['types'])}")
else:
    print("Pokémon not found. Please check the name and try again.")