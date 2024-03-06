# Generated by Django 4.0.6 on 2024-03-05 18:17

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('discription', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('discription', models.TextField(default=None, null=True)),
                ('skillsof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.skillsof')),
            ],
        ),
        migrations.CreateModel(
            name='SkillSetsBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(default=None, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='skills.slug')),
                ('skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.skills')),
                ('skillsgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.skillsgroup')),
                ('skillsof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.skillsof')),
            ],
        ),
    ]