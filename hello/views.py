from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime


def index(request):
    return render(request, 'index.html')
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
    return render(request, 'anime.html', {'anime' : anime_list})

