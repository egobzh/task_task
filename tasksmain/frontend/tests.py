# Django
from django.test import TestCase
from django.test import Client
# Python
from http import HTTPStatus
# Models
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.c = Client()
    def test_is_ok_index(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    def test_is_ok_task_add(self):
        headers = {'task': 'тест запси!'}
        response = self.c.post('/task_add', {'task': 'тест запси!'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
    def test_is_ok_task_complete(self):
        response = self.c.post('/tasks_commit/1')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    def test_is_ok_task_uncomplete(self):
        response = self.c.post('/tasks_commit/1')
        self.assertEqual(response.status_code, HTTPStatus.OK)

