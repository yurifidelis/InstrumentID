from django.test import TestCase

from .models import Track, Album, Artist

def create_track(album, file, title, position, duration):
    # Cria uma faixa com os atributos passados
    return Track.objects.create(album=album, file=file, title=title, position=position, duration=duration)

def create_album(artist, title, year):
    # Cria uma faixa com os atributos passados
    return Album.objects.create(artist=artist, title=title, year=year)

def create_artist(name):
    # Cria uma faixa com os atributos passados
    return Artist.objects.create(name=name)

# TODO: Testes para
# Faixa não pode ser adicionada sem que haja um album na base de dados
# Albums sem faixas podem ser excluidos de qualquer listagem