from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'base/login.html'  # Путь к вашему HTML-шаблону входа
    redirect_authenticated_user = True  # Перенаправляет авторизованных пользователей
    success_url = reverse_lazy('base:task_list')  # URL, на который перенаправляется пользователь после входа

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base:task_list')  # Перенаправляет авторизованных пользователей
        return super().get(*args, **kwargs)
    

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print(f"Task before update: {task.complete}")  # Отладочная печать
    task.complete = True
    task.save()
    print(f"Task after update: {task.complete}")  # Проверка обновления
    return redirect('base:task_list')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('base:task_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)  # Log in the user after registration
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base:task_list')  # Redirect if user is already logged in
        return super().get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Фильтруем только задачи, которые принадлежат текущему пользователю и не выполнены
        context['stasks'] = context['tasks'].filter(user=self.request.user, complete=False)
        context['ntasks'] = context['tasks'].filter(user=self.request.user, complete=True)
        context['count'] = context['tasks'].count()

        # Поиск по заголовку задачи
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input

        return context

    



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:task_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.completed = False
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print('not saving the form')
        print(form.errors)
        return super(TaskCreate, self).form_invalid(form)
    
    
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:task_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:task_list')


class DefaultPage(TemplateView):
    template_name = 'base/page_default.html'
