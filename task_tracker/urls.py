from django.urls import path
from . import views
from .views import (TaskDetailView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    BoardCreateView,
                    BoardUpdateView,
                    BoardDeleteView,
                    EpicDetailView,
                    EpicCreateView,
                    EpicUpdateView,
                    EpicDeleteView,
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
    path('epics/<int:pk>', EpicDetailView.as_view(), name='epic_details'),
    path('epics/create', EpicCreateView.as_view(), name='epic_create'),
    path('epics/update/<int:pk>', EpicUpdateView.as_view(), name='epic_update'),
    path('epics/delete/<int:pk>', EpicDeleteView.as_view(), name='epic_delete'),
]
