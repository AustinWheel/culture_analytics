from django.db import models

# Create your models here.
# create a class called 'Actor' which inherits from 'models.Model'
# options: White, Black, Native American, East Asian, Southeast Asian, Middle East, and LatinX
race_options = (
    ('White', 'White'),
    ('Black', 'Black'),
    ('Native American', 'Native American'),
    ('East Asian', 'East Asian'),
    ('Southeast Asian', 'Southeast Asian'),
    ('Middle East', 'Middle East'),
    ('LatinX', 'LatinX'),
)

sex_options = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class Actor(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    race = models.CharField(max_length=255, blank=True, default='')
    sex = models.CharField(max_length=255, default='Other', blank=True)
    dialog = models.TextField(blank=True, default='')
    role = models.CharField(max_length=255, blank=True, default='')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    cleaned = models.TextField(blank=True, default='')
    no_named = models.TextField(blank=True, default='')
    lines_spoken = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    year = models.IntegerField(default=0, blank=True)
    genre = models.CharField(max_length=255, blank=True, default='')
    url = models.TextField(blank=True, default='')
    script_url = models.TextField(blank=True, default='')
    script = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name