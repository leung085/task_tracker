from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# ??? Check if ListView can create something like Kanban/Scrum board
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, Board

def home(request):
    todos = Task.objects.filter(status='TODO')
    ip = Task.objects.filter(status='IP')
    done = Task.objects.filter(status='DONE')

    context = {
        'todos': todos,
        'ip': ip,
        'done': done,
    }
    return render(request, 'task_tracker/home.html', context)

def about(request):
    return render(request, 'task_tracker/about.html')

class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'author', 'assignee', 'story_points', 'board']


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'author', 'assignee', 'story_points', 'board']


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_tracker-home')



def board(request, **kwargs):
    board_exists = Board.objects.filter(pk=kwargs.get('pk')).count()
    print(board_exists)
    if not board_exists:
        raise Exception("Board doesn't exist.")
    todos = Task.objects.filter(status='TODO', board=kwargs.get('pk'))
    ip = Task.objects.filter(status='IP', board=kwargs.get('pk'))
    done = Task.objects.filter(status='DONE', board=kwargs.get('pk'))

    context = {
        'todos': todos,
        'ip': ip,
        'done': done,
    }
    return render(request, 'task_tracker/home.html', context)



class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['name', 'description']


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    fields = ['name', 'description']


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('task_tracker-home')
