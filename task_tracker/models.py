from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Task(models.Model):
    TO_DO = "TODO"
    IN_PROGRESS = "IP"
    DONE = "DONE"

    TASK_STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length = 4,
        choices = TASK_STATUS_CHOICES,
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='author')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assignee')
    story_points = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('task_details', args=[str(self.id)])
