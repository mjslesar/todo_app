from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from todo_app.models import Task

User = get_user_model()

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.task = Task.objects.create(title='Test Task', user=self.user)

    def test_get_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_task_detail(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)