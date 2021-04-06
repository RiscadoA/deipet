import requests
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def petlist(request):
    response = requests.get('https://aduck.rnl.tecnico.ulisboa.pt/deipet/pets')
    pets = response.json()
    return render(request, 'petlist.html', {"pets": pets})
