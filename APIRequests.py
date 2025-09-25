import requests

baseUrl = "https://pokeapi.co/api/v2/"

def getPokemonInfo(name):
    fullUrl = baseUrl + "pokemon/" + name
    response = requests.get(fullUrl)
    
    if response.status_code == 200:
        pokemonInfo = response.json()
        return pokemonInfo
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemonInfo = getPokemonInfo("pikachu")

print(f"Name: {pokemonInfo["name"].capitalize()}")
print(f"Id: {pokemonInfo["id"]}")
print(f"Height: {pokemonInfo["height"]}")
print(f"Weight: {pokemonInfo["weight"]}")
