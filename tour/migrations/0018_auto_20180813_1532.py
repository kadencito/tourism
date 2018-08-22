# Generated by Django 2.0.4 on 2018-08-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0017_secretary_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=150, verbose_name='Nombre')),
                ('whatsapp', models.CharField(max_length=150, verbose_name='Nombre')),
                ('instagram', models.CharField(max_length=150, verbose_name='Nombre')),
                ('twitter', models.CharField(max_length=150, verbose_name='Nombre')),
                ('youtube', models.CharField(max_length=150, verbose_name='Nombre')),
                ('register_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'permissions': (('show_social', 'Can Details Social'), ('index_social', 'Can List Social')),
            },
        ),
        migrations.AlterModelOptions(
            name='function',
            options={'ordering': ['title'], 'permissions': (('show_function', 'Can Details Function'), ('index_function', 'Can List Function')), 'verbose_name': 'Funcion', 'verbose_name_plural': 'Funciones'},
        ),
    ]
