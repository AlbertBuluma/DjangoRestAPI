from . models import Songz
from . serializers import SongzSerializer
from rest_framework import generics, viewsets
# Create your views here.

class ListSongzView(generics.ListAPIView):
# class ListSongzView(viewsets.ModelViewSet):
    queryset = Songz.objects.all()
    serializer_class = SongzSerializer
