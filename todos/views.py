from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task

from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'todos'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'todos-get'
    template_name = 'todos/details.html'

class TaskCreate(CreateView):
    model = Task
    context_object_name = 'todos-create'
    template_name = 'todos/create.html'
    fields = '__all__'
    success_url = reverse_lazy('todos')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todos')

