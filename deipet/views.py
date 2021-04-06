import requests
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def pets(request):
    response = requests.get('https://aduck.rnl.tecnico.ulisboa.pt/deipet/pets')
    pets = response.json()
    return render(request, 'pets.html', {"pets": pets})

def pet(request, id):
    response = requests.get('https://aduck.rnl.tecnico.ulisboa.pt/deipet/pets/%d' % id)
    pet = response.json()
    return render(request, 'pet.html', {"pet": pet})