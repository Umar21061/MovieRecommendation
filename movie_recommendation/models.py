# movie_recommendation/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    tag = models.TextField()

    def __str__(self):
        return self.title
