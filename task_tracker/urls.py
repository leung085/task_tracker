from django.urls import path
from . import views
from .views import (TaskDetailView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    BoardCreateView,
                    BoardUpdateView,
                    BoardDeleteView,
                    )

urlpatterns = [
    path('', views.home, name='task_tracker-home'),
    path('about', views.about, name='task_tracker-about'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_details'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('boards/<int:pk>', views.board, name='board_details'),
    path('boards/create', BoardCreateView.as_view(), name='board_create'),
    path('boards/update/<int:pk>', BoardUpdateView.as_view(), name='board_update'),
    path('boards/delete/<int:pk>', BoardDeleteView.as_view(), name='board_delete'),
]
