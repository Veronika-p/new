from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Tasks, Statistic
from .forms import ArticlesForm, TaskForm
from django.views import View
from .forms import ArticlesLoginForm
from students.models import Articles
from django.http import Http404
from .forms import AddTaskForm
import random
import string
from django.contrib.auth import logout
from django.shortcuts import redirect

class ArticlesLogOutView2(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class ArticlesLoginView(View):
    template_name = 'users/login.html'
    def get(self, request, *args, **kwargs):
        form = ArticlesLoginForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = ArticlesLoginForm(request.POST)
        if form.is_valid():
            login_value = form.cleaned_data['login']
            password_value = form.cleaned_data['password']
            try:
                user = get_object_or_404(Articles, login1=login_value, password1=password_value)
                request.session['user'] = user.id

                return  redirect('profile')
            except Http404:
                pass
                #request.session['user'] = False


        return render(request, self.template_name, {'form': form})

class ArticlesstatisticsView(View):
    template_name = 'users/statistics.html'

    def get(self, request, *args, **kwargs):
        statistics = Statistic.objects.all()
        return render(request, self.template_name, {'statistics': statistics})

def students_home(request):
    students = Articles.objects.order_by('name_student')
    return render(request, 'students/students_home.html', {'students': students})
def tasks_home(request):
    tasks = Tasks.objects.order_by('number_tasks')
    stud = len(tasks)
    return render(request, 'students/task_home.html', {'tasks': tasks, 'stud': stud})
def create(request):
    if request.user.is_authenticated and request.user.is_staff:
        error = ''
        if request.method == 'POST':
            form = ArticlesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('students_home')
            else:
                error = 'Форма неверна'

        form = ArticlesForm()
        login = gen_rand_login(8)
        password = gen_rand_password(8)
        data = {
            'form': form,
            'error': error,
            'login': login,
            'password': password
        }

        return render(request, 'students/create.html', data)
    else:
        return redirect('/')

class ArticlesLogOutView(View):
    def get(self, request, *args, **kwargs):
        if 'user' in request.session:
            del request.session['user']
        return redirect('/')

def add_task_to_student(request, student_id):
    student = Articles.objects.get(id=student_id)

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')  # Измените на ваш путь после сохранения формы
    else:
        form = AddTaskForm(instance=student)

    return render(request, 'students/add_task_to_student.html', {'form': form, 'student': student})

def list_students(request):
    students = Articles.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/students/tasks')  # Измените на ваш путь после сохранения формы
    else:
        form = TaskForm()

    return render(request, 'students/create_task.html', {'form': form})


def gen_rand_login(length):
    characters = string.ascii_letters + string.digits
    login = ''.join(random.choice(characters) for _ in range(length))
    return login

def gen_rand_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password