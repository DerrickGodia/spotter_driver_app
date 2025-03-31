from rest_framework import serializers

from .models import Driver, Journey, Trailer, Trip, Truck


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "_all_"
