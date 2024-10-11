from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.views import LoginView



class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:task_list')


class TaskList(ListView):
    model = Task
    template_name = 'base/index.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'base/task_detail.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_urll = reverse_lazy('base:task_list')

    def get_success_url(self):
        return self.success_urll
    
    def form_valid(self, form):
        # Create a new object only when the form is valid
        form.save()
        return super().form_valid(form)
    

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:task_list')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:task_list')
