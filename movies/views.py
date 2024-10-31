from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from rest_framework.views import APIView, Response, status
from genres.models import Genre
from reviews.models import Review
from django.db.models import Avg


class MovieListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStats(APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = {}
        total_reviews = Review.objects.all().count()
        average_stars = Review.objects.all().aggregate(avg_stars=Avg('stars'))['avg_stars']

        for genre in Genre.objects.all():
            movies_by_genre[genre.name] = Movie.objects.filter(genre=genre.id).count()

        return Response(
            data={
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "average_stars": round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
