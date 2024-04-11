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
    age = models.IntegerField(default=0, blank=True)
    race = models.CharField(max_length=255, choices=race_options, blank=True, default='')
    sex = models.CharField(max_length=255, choices=sex_options, default='Other', blank=True)
    dialog = models.TextField(blank=True, default='')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, blank=True, null=True)

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