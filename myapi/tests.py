from django.test import TestCase
from rest_framework.test import RequestsClient


class APITestCase(TestCase):

    def test_response(self):
        client = RequestsClient()
        response = client.get('http://localhost/')
        assert response.status_code == 200
