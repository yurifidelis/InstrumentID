from django import forms

class TrackForm(forms.Form):
    title = forms.CharField(max_length=255)
    album = forms.CharField(max_length=100)
    position = forms.CharField(max_length=1)