import requests, json
from django.shortcuts import render
from django.http import request
from django.template.defaulttags import register

# Create your views here.
def index(request):
    if request.method == "POST":
        urlPokemon = "https://pokeapi.co/api/v2/pokemon/"+request.POST.get("pokemonId")
    else:
        urlPokemon = "https://pokeapi.co/api/v2/pokemon/1"
    urlTypes = "https://binario-djangob.s3-sa-east-1.amazonaws.com/PokemonTypes.json"
    pokemonRequest = requests.get(urlPokemon)
    typesRequest = requests.get(urlTypes)
    data = {"pokemon": pokemonRequest.json(), "types": typesRequest.json()}
    return render(request, "index.html", data)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def previousPokemon(id):
    return id - 1 if id > 1 else 1

@register.filter
def nextPokemon(id):
    return id + 1 if id < 898 else 898