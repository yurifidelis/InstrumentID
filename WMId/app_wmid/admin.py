from django.contrib import admin

from .models import User, Artist, Album, UserLibrary, Track, InstrumentClass, Instrument

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(UserLibrary)
admin.site.register(Track)
admin.site.register(InstrumentClass)
admin.site.register(Instrument)