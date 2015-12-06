from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Track, Album, Artist

def index(request):
    # Teste: ultimas faixas adicionadas na home
    latest_tracks_list = Track.objects.order_by('title')[:5]
    latest_albums_list = Album.objects.order_by('title')[:5]
    context = { 'latest_tracks_list': latest_tracks_list,
                'latest_albums_list': latest_albums_list}
    return render(request, 'app_wmid/index.html', context)
    
def track(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'app_wmid/detail.html', {'track':track})
    
def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album_track_list = Track.objects.filter(album__exact = album).order_by('position').values()
    
    context = { 'album': album,
                'album_track_list': album_track_list}
    
    return render(request, 'app_wmid/detail.html', context)
    
def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist_albums_list = Album.objects.filter(artist__exact = artist).values()
    
    context = { 'artist': artist,
                'artist_albums_list': artist_albums_list}
    
    return render(request, 'app_wmid/detail.html', context)
    
def search(request, search_query):
    return render(request, 'app_wmid/search.html', {'search_query':search_query})
    
def edit_track(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'app_wmid/edit.html', {'track':track})
    
def save_track(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    if request.method == 'POST':
        track_album = request.POST['track_album']
        track_position = request.POST['track_position']
        track_duration = request.POST['track_duration']
        
        # if Album.objects.filter(title__exact = track_album).exists():
        #     track.album = Album.objects.get(title = track_album)
        # else:
        #     new_album =
            