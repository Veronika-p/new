# Generated by Django 5.0 on 2023-12-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_articles_test_alter_articles_login1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='login1',
            field=models.CharField(default='EatDXW9F', max_length=8, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='password1',
            field=models.CharField(default='HCJ93C9Y', max_length=8, verbose_name='Пароль'),
        ),
    ]
