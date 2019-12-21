# Generated by Django 3.0 on 2019-12-21 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('task_tracker', '0008_auto_20191220_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Organization'),
        ),
    ]