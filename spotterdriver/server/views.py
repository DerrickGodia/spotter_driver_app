from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Server
from .serilaizer import ServerSerializer


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        trip = request.query_params.get("trip")

        if trip:
            self.queryset.filter(trip=trip)

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
