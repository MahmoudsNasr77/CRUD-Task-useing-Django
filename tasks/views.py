from django.shortcuts import render,redirect

from .models import task
from .forms import TaskForm

def listTask(request):
    tasks=task.objects.all()
    return render(request,'home.html',{'tasks':tasks})
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_task') 
    form=TaskForm()        
    return render(request,'add_task.html',{'form':form})
def update_task_status(request,id):
    single_task=task.objects.get(id=id)
    if request.method=='POST':
        is_completed='is_completed' in request.POST
        single_task.isCompleted=is_completed
        single_task.save()
        return redirect('tasks:list_task')
    return redirect('tasks:list_task')
def delete_task(request,id):
    single_task=task.objects.get(id=id)
    single_task.delete()
    return redirect('tasks:list_task')

