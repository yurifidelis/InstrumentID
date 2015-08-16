from django.db import models
import datetime                 # Para salvar data de criacao de usuario
import os

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    created_time = models.DateTimeField(editable=False)
    modified_time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' Atualiza timestamps ao salvar user '''
        if not self.id:
            self.created_time = datetime.datetime.today()
        self.modified_time = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)
    
    def __str__(self):           # __unicode__ on Python 2
        return self.username
    
class Artist(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):           # __unicode__ on Python 2
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    coverURL = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):           # __unicode__ on Python 2
        return self.title

class UserLibrary(models.Model):
    user = models.ForeignKey(User)
    album = models.ForeignKey(Album)

class Track(models.Model):
    album = models.ForeignKey(Album)
    file = models.FileField(upload_to='uploads',null=True)
    title = models.CharField(max_length=255)
    position = models.IntegerField()
    duration = models.DurationField()
    
    def __str__(self):           # __unicode__ on Python 2
        return self.title
    
    def filename(self):
        return os.path.basename(self.file.name)
    
class InstrumentClass(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):           # __unicode__ on Python 2
        return self.name

class Instrument(models.Model):
    instrument_class = models.ForeignKey(InstrumentClass)
    track = models.ForeignKey(Track)
    start_time = models.FloatField()
    end_time = models.FloatField()
    
    def __str__(self):           # __unicode__ on Python 2
        return self.id + '\tclass: ' + self.instrument_class