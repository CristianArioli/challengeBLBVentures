from rest_framework import viewsets
from musics.api import serializers
from musics import models

class MusicsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MusicsSerializer
    queryset = models.Musics.objects.all()