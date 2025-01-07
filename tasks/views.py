from datetime import date
from django.shortcuts import render,redirect

from .models import task
from .forms import TaskForm
from django.core.paginator import Paginator

def listTask(request):
    search_query = request.GET.get('search', '')  # Get the search query from the GET request
    
    if search_query:
        tasks = task.objects.filter(title__icontains=search_query)  # Filter tasks by title containing the search query
    else:
        tasks = task.objects.all()  # If no search query, show all tasks
    
    # Apply pagination: 10 tasks per page
    paginator = Paginator(tasks, 9)  # Show 10 tasks per page
    
    # Get the current page number from the GET request
    page_number = request.GET.get('page')
    
    # Get the tasks for the current page
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj, 'search_query': search_query})
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            due_date = form.cleaned_data['dueDate']
            if due_date<date.today():
                form.add_error('dueDate', 'تاريخ الاستحقاق يجب أن يكون في المستقبل')
                return render(request, 'add_task.html', {'form': form})
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
def update_task(request,id):
    single_task=task.objects.get(id=id)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=single_task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_task')
    form=TaskForm(instance=single_task)
    return render(request,'update_task.html',{'form':form})

