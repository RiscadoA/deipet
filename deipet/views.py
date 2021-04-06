import requests
from django.shortcuts import render


PETSTORE_PETS_END_POINT = 'https://aduck.rnl.tecnico.ulisboa.pt/deipet/pets'

def index(request):
    return render(request, 'index.html', {})

def pets(request):
    
    if 'limit' in request.GET:
        limit = int(request.GET['limit'])
    else:
        limit = 10

    if 'offset' in request.GET:
        offset = int(request.GET['offset'])
    else:
        offset = 0

    response = requests.get(PETSTORE_PETS_END_POINT, params={
        "limit": limit,
        "offset": offset
    })

    pets = response.json()
    return render(request, 'pets.html', {
        "limit": limit,
        "offset": offset,
        "prevOffset": max(0, offset - limit),
        "nextOffset": pets[-1]["id"] if len(pets) == limit else offset,
        "first": offset + 1,
        "last": min(len(pets), limit) + offset,
        "pets": pets
    })

def pet(request, id):
    response = requests.get('%s/%d' % (PETSTORE_PETS_END_POINT, id))
    pet = response.json()
    return render(request, 'pet.html', {"pet": pet})