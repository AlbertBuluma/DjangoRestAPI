from django.urls import reverse
from . models import Songz
from rest_framework.views import status
from rest_framework.test import APIClient, APITestCase
from . serializers import SongzSerializer
# Create your tests here.


class BaseViewTest(APITestCase):

    client = APIClient

    @staticmethod
    def createsong(title='', artist=''):
        if title!='' and artist!='':
            Songz.objects.create(title=title, artist=artist)

    def setUp(self):
        self.createsong('Speeding', 'Omarion')
        self.createsong('Duro', 'Tekno')
        self.createsong('Malaika', 'Vinka')
        self.createsong('Taken', 'Trey Songz')


class GetAllSongzTest(BaseViewTest):

    def test_get_all_songz(self):
        response = self.client.get(reverse('songz-all'))
        expected = Songz.objects.all()
        serialized = SongzSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)