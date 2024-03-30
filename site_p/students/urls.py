from django.urls import path
from  . import views

urlpatterns = [
    path('', views.students_home, name='students_home'),
    path('tasks', views.tasks_home, name='tasks_home'),
    path('create', views.create, name='create'),
    path('list_students', views.list_students, name='list_students'),
    path('create_task', views.create_task, name='create_task'),

    path('add_task_to_student/<int:student_id>/', views.add_task_to_student, name='add_task_to_student'),


]