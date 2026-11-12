# In dit file wil ik afzonderlijke code laten zien, specifiek over het stuk: Gegevens ophalen bij een aangewezen publieke REST-API.

import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)
naam_pokemon = response.json()["name"]

print("De naam van de Pokémon is: " + naam_pokemon)
