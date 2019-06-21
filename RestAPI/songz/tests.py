from django.urls import reverse
from . models import Songz
from rest_framework.views import status
from rest_framework.test import APIClient, APITestCase
from . serializers import SongzSerializer
# Create your tests here.


class BaseViewTest(APITestCase):

    client = APIClient

    @staticmethod
    def createsong(title='', song=''):
        if title!='' and song!='':
            Songz.objects.create(title=title, song=song)

    def setUp(self):
        self.createsong('Speeding', 'Omarion')
        self.createsong('Duro', 'Tekno')
        self.createsong('Malaika', 'Vinka')
        self.createsong('Taken', 'Trey Songz')


class GetAllSongzTest(BaseViewTest):

    def test_get_all_songz(self):
        response = self.client.get(
            reverse('songz-all', kwargs={'version':'v1'}))

        expected = Songz.objects.all()
        serialized = SongzSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status, status.HTTP_200_OK)