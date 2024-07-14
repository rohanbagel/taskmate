from django import forms 
from todolist.models import TaskList

class Taskform(forms.ModelForm):
    class Meta:
        model= TaskList
        fields= ['task', 'done']
