from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

from .serializers import TaskSerializer
import todo_app
from .models import Task
from .log_utils import log_event


User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, status='new', user=request.user)
        return redirect('index')

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo_app/index.html', {'tasks': tasks})

def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    statuses = ['new', 'in_progress', 'completed']
    try:
        current_index = statuses.index(task.status)
        next_index = (current_index + 1) % len(statuses)
        task.status = statuses[next_index]
    except ValueError:
        task.status = ['new']
    task.save()
    log_event('update_logger', f'Статус задачи: {task.status}')
    return redirect('index')

def delete(request: HttpRequest, task_id: int):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        log_event('delete_logger', f'Удаление задачи: {task.title}')
        task.delete()
        messages.success(request, 'Задача успешно удалена')
    return redirect('index')

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)