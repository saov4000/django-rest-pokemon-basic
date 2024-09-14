from rest_framework import serializers

class PokemonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    height = serializers.IntegerField()
    weight = serializers.IntegerField()