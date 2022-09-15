from asyncio import Task
from dataclasses import field, fields
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descrition', 'important']