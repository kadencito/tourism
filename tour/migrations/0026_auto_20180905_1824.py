# Generated by Django 2.0.3 on 2018-09-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0025_assignmentagency_assignmentlodging_assignmentrestaurant_assignmentsite_assignmenttransport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourismsite',
            name='web',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Pagina Web'),
        ),
    ]
