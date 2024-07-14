from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.form import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required 
# Create your views here.


@login_required 
def todolist(request):#todolist is name of function that is being called in todolist ka urls.py
     if request.method == "POST":
          form= Taskform(request.POST or None)
          if form.is_valid():
               instance = form.save(commit=False)
               instance.manage = request.user
               form.save()
          messages.success(request,"New Task Added!")
          return redirect('todolist')
     else:
          all_tasks= TaskList.objects.filter(manage=request.user)
          paginator1 = Paginator(all_tasks, 5)
          page = request.GET.get('pg')
          all_tasks= paginator1.get_page(page)
          
          return render(request, 'todolist.html', {'all_tasks': all_tasks})
     
@login_required 
def delete_task(request,task_id):
     task = TaskList.objects.get(pk=task_id) #task is selected and stored in this variable 
     if task.manage == request.user:
          task.delete()
     else:
           messages.error(request,"ACCESS DENIEDD BOIIII")
     
     return redirect('todolist')

@login_required 
def edit_task(request,task_id):
     if request.method == "POST": #whenever post request we are saving some kind of data
          task = TaskList.objects.get(pk=task_id)
          form = Taskform(request.POST or None, instance= task)
          if form.is_valid():
               form.save()
          
          messages.success(request,"Task Edited!")
          return redirect('todolist')
     else:
          task_obj = TaskList.objects.get(pk=task_id)
          return render(request, 'edit.html', {'task_obj': task_obj}) #working with just one obj thus no need for loop 
     
@login_required 
def complete_task(request,task_id):
     task = TaskList.objects.get(pk=task_id) #task is selected and stored in this variable 
     if task.manage == request.user:
          
          task.done = True
          task.save() 
     else:
           messages.error(request,"ACCESS DENIEDD BOIIII")

     return redirect('todolist')
@login_required 
def pending_task(request,task_id):
     task = TaskList.objects.get(pk=task_id) #task is selected and stored in this variable 
     task.done = False #whenever get request we are loading some kind of data
     task.save() 
     return redirect('todolist')

    
def contact(request):
     context= {'contact_text': "Welcome to Contact Page",   
     }
     return render(request, 'contact.html', context)
def about(request):
     context= {'about_text': "Welcome to About Page",   
     }
     return render(request, 'about.html', context)
    

def index(request):
     context= {'index_text': "Welcome to Index Page",   
     }
     return render(request, 'index.html', context)