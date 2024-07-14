from django.contrib import admin
from todolist.models import TaskList #from current directory import models

# Register your models here.
admin.site.register(TaskList)
