from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Anime


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    return render(request, 'index.html', {'host' : host, 'path' : path, 'user_agent' : user_agent})
def about(request, name, age):
    return HttpResponse(f"""
                        <h2>About</h2>
                        <p>Name: {name}</p>
                        <p>Age: {age}</p>
                         """)
def contact(request):
    return HttpResponse("Contacts!")

def anime(request):
    anime_list = Anime.objects.all()
    if anime_list == []:
        return render(request, 'anime.html', {'anime' : anime_list})
    else:
        return HttpResponseNotFound("Not Found, Anime list is empty")

def anime_get(request, id):
    return HttpResponse(f"<h1>This is anime {id}</h1>")

