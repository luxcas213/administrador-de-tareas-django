from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from .forms import TaskForm
from .models import Task
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
            render(request, 'create_task.html',{"form":TaskForm(),"error":"Bad data passed in. Try again."})
            

@login_required
def taskdetail(request,task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'taskdetail.html',{"task":task})