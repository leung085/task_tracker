from django.contrib import admin
from .models import Task, Board, Epic

admin.site.register(Task)
admin.site.register(Board)
admin.site.register(Epic)
