from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import TaskDetailView, TaskListCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:task_id>', views.update, name='update'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)