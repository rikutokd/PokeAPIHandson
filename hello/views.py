from django.http import HttpResponse
from django.shortcuts import render
import requests

def showIndex(request):
    data = {
        'image_url' : image_url,
        'id' : id,
        'name' : name,
        'types' : type,
    }
    return render(request, 'index.html', data)

url = "https://pokeapi.co/api/v2/pokemon/1000"

response = requests.get(url)
pokemonData = response.json()

image_url = pokemonData['sprites']['other']['official-artwork']['front_default']
id = pokemonData['id']
name = pokemonData['name']

type = []
count = 0

for types in pokemonData['types']:
    type.insert(count, types['type']['name'])
    count+=1

print(id)
print(name)
print(type)