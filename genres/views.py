from genres.models import Genre
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class GenreListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
