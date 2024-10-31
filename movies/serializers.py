from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = '__all__'


    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError('O ano não pode ser inferior a 1888')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo não pode exceder 500 caracteres')
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


    def get_rate(self, obj):
        reviews = Review.objects.filter(movie=obj.id).aggregate(stars_rate=Avg('stars'))
        if reviews['stars_rate']:
            return round(reviews['stars_rate'], 1)
        return None
