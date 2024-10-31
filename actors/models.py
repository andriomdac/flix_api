from django.db import models


NATIONALITY = [
    {"BR", "BRAZIL"},
    {"USA", "UNITED STATES"}
]


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(choices=NATIONALITY, blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name
