# Generated by Django 4.0.6 on 2024-02-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_alter_user_profile_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Profile',
            field=models.ImageField(default='_user/profiles/default.jpeg', null=True, upload_to='_user/profiles/'),
        ),
    ]