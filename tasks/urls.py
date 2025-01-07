app_name='tasks'
from django.urls import path
from .views import listTask,add_task,update_task_status,delete_task,update_task
urlpatterns = [
    path('',listTask,name='list_task'),
    path('add_task',add_task,name='add_task'),
    path('update_task_status/<int:id>/', update_task_status, name='update_task_status'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('update_task/<int:id>/', update_task, name='update_task'),
]
