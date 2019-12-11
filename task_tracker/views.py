from django.shortcuts import render
from .models import Task

todos = Task.objects.filter(status='TODO')
ip = Task.objects.filter(status='IP')
done = Task.objects.filter(status='DONE')

# Create your views here.
def home(request):
    context = {
        'todos': todos,
        'ip': ip,
        'done': done,
    }
    return render(request, 'task_tracker/home.html', context)

def about(request):
    return render(request, 'task_tracker/about.html')
