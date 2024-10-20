from django.forms import ModelForm
from .models import Task
from django import forms
from django.forms import modelformset_factory

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', )

TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=1)