import requests
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AddForm

# Token used on operations which require auth
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

# PetStore API end point
PETSTORE_END_POINT = 'https://aduck.rnl.tecnico.ulisboa.pt/deipet/pets'

# Index page view
def index(request):
    return render(request, 'index.html', {})

# Pet list page view
def pets(request):
    # Get limit & offset
    if 'limit' in request.GET:
        limit = int(request.GET['limit'])
    else:
        limit = 10

    if 'offset' in request.GET:
        offset = int(request.GET['offset'])
    else:
        offset = 0

    # Request pet list
    response = requests.get(PETSTORE_END_POINT, params={
        "limit": limit,
        "offset": offset
    })

    # Render page
    pets = response.json()
    return render(request, 'pets.html', {
        "limit": limit,     # Current pet list limit
        "offset": offset,   # Current pet list offset
        # New offset if the previous button is pressed
        "prevOffset": max(0, offset - limit),
        # New offset if the next button is pressed
        "nextOffset": pets[-1]["id"] + 1 if len(pets) == limit else offset,
        "pets": pets,       # Pet list
        "nbar": "list"      # Set page as active on the navbar
    })

# Pet page view
def pet(request, id):
    # Request pet from ID
    response = requests.get('%s/%d' % (PETSTORE_END_POINT, id))
    pet = response.json()
    
    # Render page
    # If the API exposes new pet properties, they can be accessed through the
    # template 'pet.html'
    return render(request, 'pet.html', {
        "pet": pet,         # Pet to show
        "nbar": "pet"       # Set page as active on the navbar
    })

# Pet addition form page view
def add(request):
    # If the form was submitted
    if request.method == 'POST':
        # Populate form instance with data from the request
        form = AddForm(request.POST)
        if form.is_valid():
            # Parse name and URLs
            name = form.cleaned_data['name']
            urls = [s.strip() for s in form.cleaned_data['urls'].split(',')]
            
            # Send pet addition request to the PetStore API
            response = requests.post(PETSTORE_END_POINT, json={
                "imageUrls": urls,
                "name": name
            }, headers={'Authorization': 'Bearer %s' % AUTH_TOKEN})

            # Handle response
            if response.status_code == 201:
                # Redirect to pet page if it was added successfully
                return HttpResponseRedirect('/pets/%d' % response.json()['id'])
            else:
                # Show error on the form
                if response.status_code == 400:
                    error = "invalid pet"
                elif response.status_code == 401:
                    error = "accept token missing or invalid"
                else:
                    error = "error code " + str(response.status_code)
                return render(request, 'add.html', {
                    "form": form,       # Restore form used
                    "nbar": "add",      # Set page as active on the navbar
                    "error": error      # Error message
                })

    # Render pet addition form page
    return render(request, 'add.html', {
        "form": AddForm(),  # New form
        "nbar": "add",      # Set page as active on the navbar
        "error": ""         # No error message
    })