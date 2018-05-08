# Generated by Django 2.0.4 on 2018-05-07 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourismSiteDestiny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('published_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de Publicacion')),
            ],
            options={
                'verbose_name': 'Destino de Sitio Turistico',
                'verbose_name_plural': 'Destinos de Sitios Turisticos',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TourismSiteService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='NA', max_length=150, verbose_name='Item de servicio')),
                ('image', models.ImageField(null='true', upload_to='media/', verbose_name='Imagen')),
                ('published_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de Publicacion')),
            ],
            options={
                'verbose_name': 'Servicio de Sitio Turistico',
                'verbose_name_plural': 'Servicios  de Sitios Turisticos',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TourismSiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('published_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de Publicacion')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.TourismSiteDestiny', verbose_name='Lugar')),
            ],
            options={
                'verbose_name': 'Tipo de Sitio Turistico',
                'verbose_name_plural': 'Tipos de Sitios Turisticos',
                'ordering': ['title'],
            },
        ),
        migrations.RemoveField(
            model_name='lodgmentservice',
            name='lodgment',
        ),
        migrations.RemoveField(
            model_name='transportservice',
            name='type_service',
        ),
        migrations.AddField(
            model_name='lodgment',
            name='lodgment',
            field=models.ManyToManyField(to='tour.LodgmentService', verbose_name='Servicio'),
        ),
        migrations.AddField(
            model_name='transporttypeservice',
            name='service',
            field=models.ManyToManyField(to='tour.TransportService', verbose_name='Servicios'),
        ),
        migrations.RemoveField(
            model_name='tourismsite',
            name='schedule',
        ),
        migrations.AddField(
            model_name='tourismsite',
            name='schedule',
            field=models.ManyToManyField(to='tour.Schedule', verbose_name='Horarios'),
        ),
        migrations.AlterField(
            model_name='transporttypeservice',
            name='title',
            field=models.CharField(default='NA', max_length=150, verbose_name='Tipo de Servicio'),
        ),
        migrations.AddField(
            model_name='tourismsite',
            name='service',
            field=models.ManyToManyField(to='tour.TourismSiteService', verbose_name='Servicios'),
        ),
    ]