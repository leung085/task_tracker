from django.shortcuts import render

todos = [
    {'name': 'Task 1 Name', 'description': 'Task 1 Description', 'status': 'TODO'},
    {'name': 'Task 2 Name', 'description': 'Task 2 Description', 'status': 'TODO'},
]
ip = [
    {'name': 'Task 3 Name', 'description': 'Task 3 Description', 'status': 'IP'},
]
done = [
    {'name': 'Task 4 Name', 'description': 'Task 4 Description', 'status': 'DONE'},
]

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
