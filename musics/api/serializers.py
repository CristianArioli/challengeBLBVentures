from rest_framework import serializers
from musics import models
 
class MusicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Musics
        fields = '__all__'