# Generated by Django 2.2.4 on 2020-03-22 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_id',
            field=models.IntegerField(default=1),
        ),
    ]