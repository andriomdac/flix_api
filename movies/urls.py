from django.urls import path
from movies.views import MovieListCreate, MovieRetrieveUpdateDelete, MovieStats


urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('movies/<int:pk>', MovieRetrieveUpdateDelete.as_view(), name='movie-detail-update-delete'),
    path('movies/stats/', MovieStats.as_view(), name='movie-statistics'),
]
