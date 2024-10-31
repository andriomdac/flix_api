from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('comment', )
    list_display = ('movie', 'comment', 'stars',)
