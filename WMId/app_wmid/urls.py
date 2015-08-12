from django.conf.urls import url

from . import views

urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),
    # ex: /app_wmid/track/5/
    url(r'^track/(?P<track_id>[0-9]+)/$', views.track, name='track'),
    # ex: /app_wmid/album/5/
    url(r'^album/(?P<album_id>[0-9]+)/$', views.album, name='album'),
    # ex: /app_wmid/artist/5/
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
    # ex: /app_wmid/search/query/
    url(r'^search/(?P<search_query>\w+)/$', views.search, name='search'), 
    #url(r'^search/?q=(?P<search_query>\w+)$', views.search, name='search'), 
]