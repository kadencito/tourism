# Generated by Django 2.0.4 on 2018-04-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_auto_20180413_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(upload_to='media/', verbose_name='Image')),
                ('address', models.CharField(default='S/N', max_length=150, unique=True)),
                ('location', models.URLField()),
                ('rating', models.CharField(choices=[('1', '✭'), ('2', '✭✭'), ('3', '✭✭✭'), ('4', '✭✭✭✭'), ('5', '✭✭✭✭✭')], default=1, max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Lodgment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.DeleteModel(
            name='Tourism_agency',
        ),
        migrations.RemoveField(
            model_name='lodgment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='description',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='description',
        ),
        migrations.AddField(
            model_name='lodgment',
            name='address',
            field=models.CharField(default='S/N', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='S/N', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='transport',
            name='address',
            field=models.CharField(default='S/N', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='lodgment',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tourism_site',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transport',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='agency',
            name='service',
            field=models.ManyToManyField(to='tour.Service_Agency'),
        ),
        migrations.AddField(
            model_name='lodgment',
            name='service',
            field=models.ManyToManyField(to='tour.Service_Lodgment'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='service',
            field=models.ManyToManyField(to='tour.Service_Restaurant'),
        ),
        migrations.AddField(
            model_name='transport',
            name='service',
            field=models.ManyToManyField(to='tour.Service_Transport'),
        ),
    ]
