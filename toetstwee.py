# Stap 1. Zet een Python programma op dat gegevens ophaalt bij een aangewezen publieke REST-API.

# import requests zorgt ervoor dat je aan de slag kunt gaan met het opvragen van gegevens, bijvoorbeeld bij een REST-API.
# Om het in VSCode te laten werken moet je eerst in de terminal met pip de requests installeren.
import requests

# Vervolgens geven we aan van welke website (URL) het programma de gegevens moet ophalen.
url = "https://pokeapi.co/api/v2/pokemon/ditto"

# Hierbij geven we een naam aan de response die we krijgen van de website, die we in verdere code weer kunnen gebruiken.
response = requests.get(url)

# Hierbij wordt er een naam gegeven aan de informatie die we van de website krijgen. We vragen de naam van een pokémon op, dus noemen de informatie "naam_pokemon".
naam_pokemon = response.json()["name"]

# Dit is de laatste stap van het programma (voor nu). Hiermee zeggen we tegen het programma: laat zien wat de naam van de pokémon is die we hebben gekregen van de website.
print("De naam van de Pokémon is: " + naam_pokemon)
