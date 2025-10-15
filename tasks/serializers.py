from rest_framework import serializers
from tasks.models import Cat, favoriteCat

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

class FavoriteCatSerializer(serializers.ModelSerializer):
    cat_detalles = serializers.StringRelatedField(source='cat', read_only=True)
    class Meta:
        model = favoriteCat
        fields = ['id', 'cat', 'cat_detalles']