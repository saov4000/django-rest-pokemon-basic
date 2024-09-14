from django.urls import path
from .views import PokemonAPIView

urlpatterns = [
    path('pokemon/<str:name>/', PokemonAPIView.as_view(), name='pokemon-detail'),
]