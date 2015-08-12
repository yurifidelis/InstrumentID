from django.shortcuts import render
from django.http import HttpResponse
from .models import Track, Album, Artist #teste

def index(request):
    # Teste: ultimas faixas adicionadas na home
    latest_tracks_list = Track.objects.order_by('title')[:5]
    latest_albums_list = Album.objects.order_by('title')[:5]
    
    output = '<h1>Latest tracks:</h2>'
    output += '<br />'.join([t.title for t in latest_tracks_list])
    
    output += '<h1>Latest albums:</h2>'
    output += '<br />'.join([a.title for a in latest_albums_list])
    
    return HttpResponse(output)
    
def track(request, track_id):
    response = "Details for track %s."
    return HttpResponse(response % track_id)
    
def album(request, album_id):
    response = ("Details for album %s")
    return HttpResponse(response % album_id)
    
def artist(request, artist_id):
    response = ("Details for artist %s")
    return HttpResponse(response % artist_id)
    
def search(request, search_query):
    response = ("Details for search query %s")
    return HttpResponse(response % search_query)
    
