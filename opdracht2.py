# In dit file wil ik afzonderlijke code laten zien, specifiek over het stuk: Gegevens filteren op een meegegeven criterium.

import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)

naam_pokemon = response.json()["name"]
ability_not_hidden = response.json()["abilities"][0]["ability"]["name"]
ability_hidden = response.json()["abilities"][1]["ability"]["name"]

print("De naam van de Pokémon is: " + naam_pokemon)
print("Deze Pokémon heeft twee abilities. Die abilities zijn: " +
      ability_not_hidden + " en " + ability_hidden)
print("Maar één van die abilities is hidden. We kijken nu alleen naar de hidden ability.")

for ability in response.json()["abilities"]:
    if ability["is_hidden"]:
        print("De hidden ability is: " + ability_hidden)
