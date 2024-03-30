from django.db import models
import random
import string

class Tasks(models.Model):
    number_tasks = models.IntegerField('Номер в ЕГЭ')
    image_tasks = models.ImageField('Картинка')
    otvet_tasks = models.CharField('Правильный ответ', max_length=100)

    def __str__(self):
        return str(self.number_tasks)
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

class Articles(models.Model):

    def gen_rand_login(length):
        characters = string.ascii_letters + string.digits
        login = ''.join(random.choice(characters) for _ in range(length))
        return login

    def gen_rand_password(length):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    name_student = models.CharField('ФИО', max_length=100)
    number_class = models.IntegerField('Номер класса')
    word_class = models.CharField("Буква класса", max_length=10)
    login1 = models.CharField("Логин", max_length=8, default=gen_rand_login(8), unique=True)
    password1 = models.CharField("Пароль", max_length=8, default=gen_rand_password(8))
    tests = models.ManyToManyField(Tasks, verbose_name='Задания', blank=True)
    def __str__(self):
        return self.name_student
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

class Answer(models.Model):
    user = models.ForeignKey(Articles, on_delete=models.CASCADE)
    answer = models.CharField(verbose_name='Ответ', max_length=200)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.task.number_tasks)
    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'

class Statistic(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Пользователь')
    bal = models.CharField(verbose_name='Набранный балл', max_length=200)
    count_question = models.CharField(verbose_name='Количество вопросов', max_length=200)
    def __str__(self):
        return str(self.user.login1)
    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'