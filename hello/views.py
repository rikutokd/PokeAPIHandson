from django.http import HttpResponse
from django.shortcuts import render
import requests

def showIndex(request):
    def receiveDataFromAPI(startIndex, endIndex):
        htmlOutput = []
        for num in range(startIndex, endIndex+1):
            url = "https://pokeapi.co/api/v2/pokemon/" + str(num)
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
            
            oneCard = makeHTML(image_url, id, name, type)
            htmlOutput.insert(num-1, oneCard) 
        
        return htmlOutput

    def makeHTML(image_url, id, name, type):
        typePart = ""
        typePart += setColor(type[0])
        if len(type) == 2:
            typePart += setColor(type[1])
        elif len(type) == 1:
            typePart += '<li class="list-group-item" style="opacity:0">' + 'hoge' + '</li>'

        result = ""

        result += '<div class="card" style="width: 10rem; float: left;">'
        result += '<img class="bd-placeholder-img card-img-top" width="100%" height="150" src="' + image_url + '" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Image cap"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"/><text x="50%" y="50%" fill="#dee2e6" dy=".3em"></text></img>'
        result += '<ul class="list-group list-group-flush">'
        result += '<li class="list-group-item">' + str(id) + '</li>'
        result += '<li class="list-group-item">' + name + '</li>'
        result += typePart
        result += '</ul>'
        result += '</div>'

        return result
    
    startIndex = 1
    endIndex = 20
    htmlOutput = receiveDataFromAPI(startIndex, endIndex)

    htmlOutput = '\n'.join(htmlOutput)

    data = {
        'htmlOutput' : htmlOutput
    }
    return render(request, 'index.html', data)

def setColor(type):
    result = ""
    if type == "grass":
        result += '<li class="list-group-item" style="background-color:#198754; color:white">' + type + '</li>'
    elif type == "poison":
        result += '<li class="list-group-item" style="background-color:#6f42c1; color:white">' + type + '</li>'
    elif type == "fire":
        result += '<li class="list-group-item" style="background-color:#fd7e14; color:white">' + type + '</li>'
    elif type == "flying":
        result += '<li class="list-group-item" style="background-color:#0dcaf0; color:white">' + type + '</li>'
    elif type == "water":
        result += '<li class="list-group-item" style="background-color:#0d6efd; color:white">' + type + '</li>'
    elif type == "bug":
        result += '<li class="list-group-item" style="background-color:#99cc66; color:white">' + type + '</li>'
    elif type == "normal":
        result += '<li class="list-group-item" style="background-color:#adb5bd; color:white">' + type + '</li>'

    return result