from django import forms
from django.forms import widgets

from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'Task_Assign_Date': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }
