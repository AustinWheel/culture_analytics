# Generated by Django 4.2.4 on 2024-04-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_actor_cleaned'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='no_named',
            field=models.TextField(blank=True, default=''),
        ),
    ]
