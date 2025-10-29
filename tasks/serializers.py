from rest_framework import serializers
from tasks.models import FavoriteCat

class FavoriteCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCat
        fields = '__all__'