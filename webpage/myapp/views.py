from django.shortcuts import render
import requests
import json

def index(request):
    context = {}
    context['some_string'] = "this is some string that I'm passing to the view"

    response = requests.get('http://127.0.0.1:9090/musics')
    musics = json.loads(response.text)

    return render(request, 'myapp/templates/musics.html', {"musics": musics})