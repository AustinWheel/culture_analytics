# Generated by Django 4.2.4 on 2024-04-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_actor_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='race',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='actor',
            name='sex',
            field=models.CharField(blank=True, default='Other', max_length=255),
        ),
    ]