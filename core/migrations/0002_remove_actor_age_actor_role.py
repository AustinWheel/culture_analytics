# Generated by Django 4.2.4 on 2024-04-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='age',
        ),
        migrations.AddField(
            model_name='actor',
            name='role',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
