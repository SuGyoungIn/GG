
from ..models import Genre
from rest_framework import serializers

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'