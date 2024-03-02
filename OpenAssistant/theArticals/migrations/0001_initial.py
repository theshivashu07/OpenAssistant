# Generated by Django 4.0.6 on 2024-03-02 17:22

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentFrom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RunningNewArticals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField(blank=True, default=dict, null=True)),
                ('USER', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.user')),
            ],
        ),
        migrations.CreateModel(
            name='ContentOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(default=None, max_length=50, null=True)),
                ('locations', models.CharField(default=None, max_length=100, null=True)),
                ('froms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='theArticals.contentfrom')),
            ],
        ),
        migrations.CreateModel(
            name='Articals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=150, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('discription', models.TextField(default=None, null=True)),
                ('joiningdate', models.DateTimeField(auto_now_add=True)),
                ('updationdate', models.DateTimeField(auto_now=True)),
                ('USER', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.user')),
            ],
        ),
    ]
