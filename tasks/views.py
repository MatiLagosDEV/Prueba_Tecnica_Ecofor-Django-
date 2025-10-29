from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FavoriteCatSerializer
from .models import FavoriteCat
import requests
# Create your views here.



class FavoriteCatView(viewsets.ModelViewSet):
    serializer_class = FavoriteCatSerializer
    queryset = FavoriteCat.objects.all()


@api_view(['GET'])
def get_breeds(request):
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code == 200:
        breeds = response.json()
        filtered = [
            {
                "id": breed.get("id"),
                "name": breed.get("name"),
                "origen": breed.get("origin"),
                "temperamento": breed.get("temperament"),
                "descripcion": breed.get("description"),
                "url": f"https://cdn2.thecatapi.com/images/{breed.get('reference_image_id')}.jpg" if breed.get('reference_image_id') else None
            }
            for breed in breeds[:10]
        ]
        return Response(filtered)
    else:
        return Response({"error": "No se pudieron recuperar las razas"}, status=response.status_code)
    
@api_view(['POST'])
def add_favorite_by_id(request):
    breed_id = request.data.get('id')
    if not breed_id:
        return Response({"error": "Falta el id de la raza"}, status=400)
    url = f"https://api.thecatapi.com/v1/breeds/{breed_id}"
    r = requests.get(url)
    if r.status_code != 200:
        return Response({"error": "No se encontró la raza"}, status=404)
    b = r.json()
    fav, _ = FavoriteCat.objects.get_or_create(
        breed_id=b.get("id"),
        defaults={
            "name": b.get("name"),
            "origen": b.get("origin"),
            "temperamento": b.get("temperament"),
            "descripcion": b.get("description"),
            "url": f"https://cdn2.thecatapi.com/images/{b.get('reference_image_id')}.jpg" if b.get('reference_image_id') else None
        }
    )
    return Response(FavoriteCatSerializer(fav).data)


