# In dit file wil ik de volledige opdracht in code laten zien. Deze code bestaat uit verschillende onderdelen code die zijn samengevoegd om er één mooi, werkend geheel van te maken.

import csv
import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url, timeout=10)
response.raise_for_status()

naam_pokemon = response.json()["name"]
ability_not_hidden = response.json()["abilities"][0]["ability"]["name"]
ability_hidden = response.json()["abilities"][1]["ability"]["name"]

if response.status_code == 200:
    print("De aanvraag is gelukt!")

else:
    print("Er is iets misgegaan!")
    print("Statuscode:", response.status_code)

# except requests.exceptions.Timeout:
#     print("De website deed er te lang over. Probeer het later opnieuw.")
# except requests.exceptions.RequestException as e:
#     print("Er is een fout opgetreden bij het ophalen van de gegevens:")

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

verrijkte_gegevens.append({
    "name": naam_pokemon,
    "ability_not_hidden": ability_not_hidden,
    "ability_hidden": ability_hidden,
    "length_name": lengte_naam_pokemon
})

kolommen = ["name", "ability_not_hidden", "ability_hidden", "length_name"]

with open("gebruikers.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=kolommen)
    writer.writeheader()
    writer.writerows(verrijkte_gegevens)

print("CSV-bestand succesvol aangemaakt met de verrijkte gegevens.")

with open("gebruikers.json", "w", newline="", encoding="utf-8") as jsonfile:
    json.dump(verrijkte_gegevens, jsonfile, indent=4, ensure_ascii=False)

print("JSON-bestand succesvol aangemaakt!")
