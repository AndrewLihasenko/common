from http import HTTPStatus

import requests
from django.http import JsonResponse
from django.test import TestCase, Client
from django.urls import reverse


USER_URL = 'https://api.github.com/users/'


class ViewTests(TestCase):
    client = Client()

    def test_health_check_view(self):
        response = self.client.get(reverse('health_check'))
        assert response.status_code == HTTPStatus.OK

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == HTTPStatus.OK

    def test_question_view(self):
        response = self.client.get(reverse('github'))
        assert response.status_code == HTTPStatus.OK


class ReturnDataTests(TestCase):

    def test_question_return_data(self):
        response = requests.get(f'{USER_URL}user')
        data = response.json()
        assert data is not None

    def test_question_valid_data(self):
        response = requests.get(f'{USER_URL}user')
        try:
            data = response.json()
            JsonResponse(data, safe=False)
        except TypeError:
            print("This data is can’t be parsed")


