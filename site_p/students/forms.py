from .models import Articles, Tasks
from django.forms import ModelForm, TextInput, NumberInput, DateInput, FileInput
from django import forms

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name_student', 'number_class', 'word_class','login1', 'password1']

        widgets = {
            "name_student": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО ученика'
            }),
            "number_class": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер класса'
            }),
            "word_class": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Буква класса'
            }),
            "login1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "password1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }

class ArticlesLoginForm(forms.Form):
    login = forms.CharField(max_length=8, widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder': 'Пароль'}), max_length=8)



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['tests']



class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['number_tasks', 'image_tasks', 'otvet_tasks']

        widgets = {
            "number_tasks": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер задания'
            }),
            "image_tasks": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка'
            }),
            "otvet_tasks": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Правильный ответ'
            })

        }
