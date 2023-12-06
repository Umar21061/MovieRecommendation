# movie_recommendation/forms.py
from django import forms

class MovieForm(forms.Form):
    movie_title = forms.CharField(label='Enter a movie title:')
