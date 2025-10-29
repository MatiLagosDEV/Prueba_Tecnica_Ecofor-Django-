from django.urls import path, include
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'FavoriteCats', views.FavoriteCatView, 'FavoriteCats')
urlpatterns = [
    path('api/thecatapi.com/v1/', include(router.urls)),
    path('api/thecatapi.com/v1/breeds/', views.get_breeds, name='get-breeds'),
    path('api/thecatapi.com/v1/favorite/', views.add_favorite_by_id, name='add-favorite')
]