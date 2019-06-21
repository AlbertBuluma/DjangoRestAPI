from django.urls import path, include
from . views import ListSongzView
# from . views import 


urlpatterns = [
    path('songz/', ListSongzView.as_view(), name='songz-all'),
]