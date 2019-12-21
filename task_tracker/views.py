from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# ??? Check if ListView can create something like Kanban/Scrum board
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import F
from .models import Task, Board, Epic

def home(request):
    todos = Task.objects.filter(status='TODO').order_by(F('epic__pk').desc(nulls_last=True))
    ip = Task.objects.filter(status='IP').order_by(F('epic__pk').desc(nulls_last=True))
    done = Task.objects.filter(status='DONE').order_by(F('epic__pk').desc(nulls_last=True))

    context = {
        'todos': todos,
        'ip': ip,
        'done': done,
    }
    return render(request, 'task_tracker/home.html', context)

def about(request):
    return render(request, 'task_tracker/about.html')

class EpicDetailView(DetailView):
    model = Epic

class EpicCreateView(LoginRequiredMixin, CreateView):
    model = Epic
    template_name = 'task_tracker/create_update_form.html'
    fields = ['name', 'description', 'board']

    def get_context_data(self, **kwargs):
        context = super(EpicCreateView, self).get_context_data(**kwargs)
        context.update({'name': 'Epic'})
        return context


class EpicUpdateView(LoginRequiredMixin, UpdateView):
    model = Epic
    template_name = 'task_tracker/create_update_form.html'
    fields = ['name', 'description', 'board']

    def get_context_data(self, **kwargs):
        context = super(EpicUpdateView, self).get_context_data(**kwargs)
        context.update({'name': 'Epic'})
        return context

class EpicDeleteView(LoginRequiredMixin, DeleteView):
    model = Epic
    success_url = reverse_lazy('task_tracker-home')

class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_tracker/create_update_form.html'
    fields = ['name', 'description', 'status', 'author', 'assignee', 'story_points', 'board', 'epic']

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({'name': 'Task'})
        return context

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_tracker/create_update_form.html'
    fields = ['name', 'description', 'status', 'author', 'assignee', 'story_points', 'board', 'epic']

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context.update({'name': 'Task'})
        return context

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_tracker-home')



def board(request, **kwargs):
    board = Board.objects.filter(pk=kwargs.get('pk'))
    board_exists = board.count()
    if not board_exists:
        raise Exception("Board doesn't exist.")

    if request.user.profile.organization != board.first().organization:
        raise Exception("Not allowed to view board.")

    todos = Task.objects.filter(status='TODO', board=kwargs.get('pk')).order_by(F('epic__pk').desc(nulls_last=True))
    ip = Task.objects.filter(status='IP', board=kwargs.get('pk')).order_by(F('epic__pk').desc(nulls_last=True))
    done = Task.objects.filter(status='DONE', board=kwargs.get('pk')).order_by(F('epic__pk').desc(nulls_last=True))
    name = Board.objects.filter(pk=kwargs.get('pk')).first().name

    context = {
        'todos': todos,
        'ip': ip,
        'done': done,
        'board_name': name,
    }
    return render(request, 'task_tracker/home.html', context)



class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = 'task_tracker/create_update_form.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(BoardCreateView, self).get_context_data(**kwargs)
        context.update({'name': 'Board'})
        return context

    def form_valid(self, form):
        form.instance.organization = self.request.user.profile.organization
        return super().form_valid(form)


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    template_name = 'task_tracker/create_update_form.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(BoardUpdateView, self).get_context_data(**kwargs)
        context.update({'name': 'Board'})
        return context

class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('task_tracker-home')
