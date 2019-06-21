from rest_framework import serializers
from .models import Songz



class SongzSerializer(serializers.HyperlinkedModelSerializer): # ModelSerializer, HyperlinkedModelserializer
    class Meta:
        model = Songz
        fields = ('title', 'artist')
