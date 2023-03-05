from django.http import HttpResponse
from django.shortcuts import render
import requests

def showIndex(request):
    def makeHTML(image_url, id, name, type):
        result = ""

        result += '<div class="card" style="width: 18rem;">'
        result += '<img class="bd-placeholder-img card-img-top" width="100%" height="280" src="' + image_url + '" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Image cap"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"/><text x="50%" y="50%" fill="#dee2e6" dy=".3em"></text></img>'
        result += '<ul class="list-group list-group-flush">'
        result += '<li class="list-group-item">' + str(id) + '</li>'
        result += '<li class="list-group-item">' + name + '</li>'
        result += '<li class="list-group-item">' + str(type ) + '</li>'
        result += '</ul>'
        result += '</div>'

        return result
    
    htmlOutput = makeHTML(image_url, id, name, type)
    data = {
        'htmlOutput' : htmlOutput
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