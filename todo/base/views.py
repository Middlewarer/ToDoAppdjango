from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

from extra_views import FormSetView, ModelFormSetView
from .forms import TaskFormSet, TaskForm

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

def uncomplete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = False
    task.save()
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

class TaskList(LoginRequiredMixin, FormSetView):
    form_class = TaskForm
    template_name = 'base/index.html'
    extra = 1  # Одна дополнительная форма для создания задачи

    def get_queryset(self):
        return Task.objects.none()  # Пустой QuerySet для создания новых задач

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Task.objects.filter(user=self.request.user)
        context['stasks'] = user_tasks.filter(complete=False)  # Невыполненные задачи
        context['ntasks'] = user_tasks.filter(complete=True)   # Выполненные задачи
        context['formset'] = self.get_formset() 
        context['count'] = context['stasks'].count() # Создание пустого formset
        return context

    def formset_valid(self, formset):  # Получаем данные формы из POST

        if formset.is_valid():  # Проверяем, валидны ли формы
            for form in formset:
                if form.is_valid():  # Дополнительная проверка на валидность формы
                    task = form.save(commit=False)
                    task.user = self.request.user  # Присваиваем текущего пользователя
                    task.save()  # Сохраняем задачу
            return super().formset_valid(formset)  # Обработка успешной валидации

        return self.formset_invalid(formset)




class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'


    
    

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
