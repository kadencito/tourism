# Generated by Django 2.0.4 on 2018-08-03 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0015_auto_20180802_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='function',
            options={'ordering': ['title'], 'permissions': (('show_fucntion', 'Can Details Function'), ('index_function', 'Can List Function')), 'verbose_name': 'Funcion', 'verbose_name_plural': 'Funciones'},
        ),
        migrations.AlterModelOptions(
            name='objective',
            options={'ordering': ['title'], 'permissions': (('show_objective', 'Can Details Objective'), ('index_objective', 'Can List Objective')), 'verbose_name': 'Objetivo', 'verbose_name_plural': 'Objetivos'},
        ),
        migrations.RemoveField(
            model_name='function',
            name='description',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='description',
        ),
        migrations.AddField(
            model_name='function',
            name='title',
            field=models.TextField(default=1, unique=True, verbose_name='Descripcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objective',
            name='title',
            field=models.TextField(default=1, unique=True, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]
