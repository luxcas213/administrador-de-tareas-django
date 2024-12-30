from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required 
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse, JsonResponse
# Create your views here.
@login_required
def tasks(request):
    a=Task.objects.filter(user=request.user)
    return render(request, 'tasks.html',{"tasks":a})

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{"form":TaskForm()})
    
    
    if request.method == 'POST':
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html',{"form":TaskForm(),"error":"Bad data passed in. Try again."})
            

@login_required
def taskdetail(request,task_id):
    task = get_object_or_404(Task,pk=task_id)
    return render(request, 'taskdetail.html',{"task":task})

@login_required
def complete_task(request,task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task,pk=task_id)
        if task.completed == False:
            task.completed = True
        else:
            task.completed = False    
        task.save()
        return redirect('tasks')
    else:
        return redirect('tasks')
    
@login_required
def delete_task(request,task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task,pk=task_id)
        task.delete()
        return redirect('tasks')
    else:
        return redirect('tasks')

@login_required
def update_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'update_task.html',{"task":task,"form":form})
    else:
        try:
            form = TaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'update_task.html',{"task":task,"form":form,"error":"Bad data passed in. Try again."})