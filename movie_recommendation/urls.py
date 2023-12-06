# movie_recommendation/urls.py
from django.urls import path
from .views import movie_recommendation

urlpatterns = [
    path('', movie_recommendation, name='movie_recommendation'),
]
