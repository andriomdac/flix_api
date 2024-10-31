from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'genre', 'release_date', 'resume',)
