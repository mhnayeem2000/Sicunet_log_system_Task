from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import AccessLog
# Create your tests here.


class AccessLogAPITests(APITestCase):

    def setUp(self):
        self.log = AccessLog.objects.create(
            card_id="12345",
            door_name="Main Entrance",
            access_granted=True
        )
        self.list_url = reverse('accesslog-list')
        self.detail_url = reverse('accesslog-detail', args=[self.log.id])


    def test_post_log(self):
        data = {
            "card_id": "67890",
            "door_name": "Side Entrance",
            "access_granted": False
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AccessLog.objects.count(), 2)
        self.assertEqual(AccessLog.objects.get(id=response.data['id']).card_id, "67890")


    def test_get_logs(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_log(self):
        data = {
            "card_id": "12345",
            "door_name": "Main Entrance",
            "access_granted": False
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.log.refresh_from_db()
        self.assertFalse(self.log.access_granted)    