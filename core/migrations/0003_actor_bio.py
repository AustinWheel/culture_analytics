# Generated by Django 4.2.4 on 2024-04-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_actor_age_actor_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
