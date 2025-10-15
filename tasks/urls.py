from django.urls import path, include
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'cats', views.CatView, 'cats')
router.register(r'favoriteCats', views.FavoriteCatView, 'favoriteCats')
urlpatterns = [
    path('api/thecatapi.com/v1/', include(router.urls)),
    path('api/thecatapi.com/v1/search-cats/', views.search_cats, name='search-cats'),
]