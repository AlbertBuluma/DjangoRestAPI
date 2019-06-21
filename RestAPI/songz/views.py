from . models import Songz
from . serializers import SongzSerializer
from rest_framework import generics
# Create your views here.

class ListSongzView(generics.ListAPIView):
    queryset = Songz.objects.all()
    serializer_class = SongzSerializer
