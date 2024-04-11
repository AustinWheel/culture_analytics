# Generated by Django 4.2.4 on 2024-04-11 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('year', models.IntegerField(blank=True, default=0)),
                ('genre', models.CharField(blank=True, default='', max_length=255)),
                ('url', models.TextField(blank=True, default='')),
                ('script_url', models.TextField(blank=True, default='')),
                ('script', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('race', models.CharField(blank=True, choices=[('White', 'White'), ('Black', 'Black'), ('Native American', 'Native American'), ('East Asian', 'East Asian'), ('Southeast Asian', 'Southeast Asian'), ('Middle East', 'Middle East'), ('LatinX', 'LatinX')], default='', max_length=255)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=255)),
                ('dialog', models.TextField(blank=True, default='')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.movie')),
            ],
        ),
    ]
