from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(to=Genre, on_delete=models.PROTECT, related_name='genre')
    release_date = models.DateField()
    actors = models.ManyToManyField(to=Actor, related_name='actors')
    resume = models.TextField(default='', max_length=500)

    def __str__(self):
        return self.title
