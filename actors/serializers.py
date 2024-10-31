from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birth_date(self, value):
        if value.year < 1800:
            raise serializers.ValidationError('Ano de nascimento não pode ser inferior a 1800')
        return value
