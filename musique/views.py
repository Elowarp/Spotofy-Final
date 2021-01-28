from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import django.core.exceptions as exceptions
from .forms import SongsForm
from .models import Songs
# Create your views here.

def index(request):
    songs = Songs.objects.all()
    print(len(songs))
    return render(request, 'index.html', {"songs": songs})

def musique(request):
    if request.method == "GET":
        idParam = request.GET.get('id', '')
        if idParam != '':
            try:
                song = Songs.objects.get(id=idParam)
            except exceptions.ObjectDoesNotExist:
                return render(request, "404.html")
            else:
                return render(request, 'musique.html', {"musicInfo": song})

        else:
            return render(request, "404.html")
    else:
        return render(request, "404.html")

def uploadSongs(request):
    form = SongsForm()
    if request.method == "POST":
        form = SongsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'uploadSong.html', {'form': form})
    else:
        return render(request, 'uploadSong.html', {'form': form})

def search(request):
    if request.method == "GET":
        query = request.GET.get("q", '')
        if query == '':
            return HttpResponseRedirect("/")
        else:
            songs = Songs.objects.filter(name__icontains = query)
            if not songs:
                return render(request, '404.html')
            return render(request, 'index.html', {"songs": songs})
