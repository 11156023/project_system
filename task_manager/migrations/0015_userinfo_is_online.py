# Generated by Django 5.1.6 on 2025-06-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0014_alter_project_start_date_alter_task_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
