# Generated by Django 3.1 on 2020-08-26 04:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='tutorials')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='topics')),
                ('vedio_link', models.URLField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('tutorials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.tutorials')),
            ],
        ),
    ]
