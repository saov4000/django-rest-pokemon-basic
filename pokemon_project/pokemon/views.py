from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PokemonAPIView(APIView):
    def get(self, request, name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            pokemon_data = {
                'name': data['name'],
                'height': data['height'],
                'weight': data['weight'],
                'abilities': [ability['ability']['name'] for ability in data['abilities']],
            }
            return Response(pokemon_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Pokémon not found."}, status=status.HTTP_404_NOT_FOUND)
