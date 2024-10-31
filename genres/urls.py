from django.urls import path
from genres.views import GenreListCreate, GenreRetrieveUpdateDestroy


urlpatterns = [
    path('genres/', GenreListCreate.as_view(), name='genre-list-create'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroy.as_view(), name='genre-detail-update-delete'),
]
