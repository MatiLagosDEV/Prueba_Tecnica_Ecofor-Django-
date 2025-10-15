from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CatSerializer, FavoriteCatSerializer
from .models import Cat, favoriteCat
# Create your views here.

class CatView(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

class FavoriteCatView(viewsets.ModelViewSet):
    serializer_class = FavoriteCatSerializer
    queryset = favoriteCat.objects.all()

@api_view(['GET'])
def search_cats(request):
    name = request.GET.get('name', '')
    origin = request.GET.get('origin', '')
    temperamento = request.GET.get('temperamento', '')

    cats = Cat.objects.all()
    
    if name:
        cats = cats.filter(name__icontains=name)
    if origin:
        cats = cats.filter(origin__icontains=origin)
    if temperamento:
        cats = cats.filter(temperamento__icontains=temperamento)

    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)
