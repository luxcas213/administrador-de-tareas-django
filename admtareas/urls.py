from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='task_create'),
    path('tasks/<int:task_id>', views.taskdetail, name='task_detail'),
    path('tasks/complete/<int:task_id>', views.complete_task, name='task_complete'),
    path('tasks/delete/<int:task_id>', views.delete_task, name='task_delete'),
    path('tasks/update/<int:task_id>', views.update_task, name='task_update'),
]