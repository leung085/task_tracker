from django.urls import path
from . import views
from .views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', views.home, name='task_tracker-home'),
    path('about', views.about, name='task_tracker-about'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_details'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
]
