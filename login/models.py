from django.db import models

class User(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    watching_movie = models.TextField(null=True, blank=True)
    watched_movie = models.TextField(null=True, blank=True)

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField()
    poster = models.CharField(max_length=150)