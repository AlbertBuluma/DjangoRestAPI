from django.urls import path, include
from . views import ListSongzView
# from . views import 


urlpatterns = [
    path('', ListSongzView.as_view(), name='songz-all'),
]