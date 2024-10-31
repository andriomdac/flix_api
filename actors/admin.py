from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    search_fields = ("name", "nationality",)
