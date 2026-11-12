# In dit file wil ik de volledige opdracht in code laten zien. Deze code bestaat uit verschillende onderdelen code die zijn samengevoegd om er één mooi, werkend geheel van te maken.

import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)
response.raise_for_status()

naam_pokemon = response.json()["name"]
ability_not_hidden = response.json()["abilities"][0]["ability"]["name"]
ability_hidden = response.json()["abilities"][1]["ability"]["name"]

print("De naam van de Pokémon is: " + naam_pokemon)
print("Deze Pokémon heeft twee abilities. Die abilities zijn: " +
      ability_not_hidden + " en " + ability_hidden)
print("Maar één van die abilities is hidden. We kijken nu alleen naar de hidden ability.")

for abilities in response.json()["abilities"]:
    if abilities["is_hidden"]:
        print("De hidden ability is: " + ability_hidden)

verrijkte_gegevens = []

lengte_naam_pokemon = len(naam_pokemon)

print("De naam van de Pokémon is " + str(lengte_naam_pokemon) + " letters lang.")
