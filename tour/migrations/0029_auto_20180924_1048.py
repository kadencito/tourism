# Generated by Django 2.0.3 on 2018-09-24 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0028_auto_20180924_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentagency',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='assignmentlodging',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='assignmentrestaurant',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='assignmentsite',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='assignmenttransport',
            name='is_active',
        ),
    ]