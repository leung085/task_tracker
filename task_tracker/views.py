from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'task_tracker/home.html')
