from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='task_tracker-home'),
    path('about', views.about, name='task_tracker-about'),
]
