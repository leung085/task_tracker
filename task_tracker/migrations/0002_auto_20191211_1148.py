# Generated by Django 3.0 on 2019-12-11 03:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]