# Generated by Django 5.0 on 2023-12-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_alter_articles_login1_alter_articles_password1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='login1',
            field=models.CharField(default='GKmYn3rc', max_length=8, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='password1',
            field=models.CharField(default='uZGOLxXv', max_length=8, verbose_name='Пароль'),
        ),
    ]
