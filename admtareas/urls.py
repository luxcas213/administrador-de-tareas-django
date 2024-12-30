from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.taskdetail, name='create_task'),
    path('tasks/complete/<int:task_id>', views.complete_task, name='complete_task'),
    path('tasks/delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('tasks/update/<int:task_id>', views.update_task, name='update_task'),
]