from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT, name='movie')
    comment = models.CharField(max_length=1000, blank=True, null=True)
    stars = models.IntegerField(validators=[
        MinValueValidator(0, message='O valor não pode ser inferior a 0'),
        MaxValueValidator(5, message='O valor não pode ser superior a 5'),
    ])

    def __str__(self):
        return self.movie.title
