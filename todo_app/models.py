from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Task(models.Model):
    TASK_STATUS = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='new')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.TextField(max_length=100, blank=True)


