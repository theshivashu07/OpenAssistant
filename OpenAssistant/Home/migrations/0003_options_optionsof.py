# Generated by Django 4.0.6 on 2024-03-12 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_optionsof_optionsgroup_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='optionsof',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Home.optionsof'),
        ),
    ]
