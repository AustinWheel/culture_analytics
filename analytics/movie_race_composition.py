# goal is to find the race composition of the movies
# this will be done by iterating over all movies and retrieving the cast
# then we will iterate over the cast and retrieve their dialog grouped by race
# finally we will calculate the percentage
# groups: >90%, 70-90%, 50-70%, 30-50%, 10-30%, <10%

# have a list for every race, with a length of 6, and each index stores the count of
# movies that had a percentage of dialog spoken by that race.
# races = ['White', 'Black', 'LatinX', 'Middle Eastern', 'Native American', 'Pacific Islander', 'South Asian', 'East Asian']
from core.models import Movie, Actor


bars = [
    [0, 0, 0, 0, 0, 0], # white
    [0, 0, 0, 0, 0, 0], # black
    [0, 0, 0, 0, 0, 0], # latin
    [0, 0, 0, 0, 0, 0], # middle eastern
    [0, 0, 0, 0, 0, 0], # native american
    [0, 0, 0, 0, 0, 0], # pacific islander
    [0, 0, 0, 0, 0, 0], # south asian
    [0, 0, 0, 0, 0, 0], # east asian
]

for movie in Movie.objects.all():
    actors = Actor.objects.filter(movie=movie)
    total_dialog = sum([len(a.dialog.split(" ")) for a in actors])
    if len(actors) == 0 or total_dialog == 0: continue
    counts = [0, 0, 0, 0, 0, 0, 0, 0]
    counts[0] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "White"])
    counts[1] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "Black"])
    counts[2] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "Latin"])
    counts[3] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "Middle Eastern"])
    counts[4] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "Native American"])
    counts[5] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "Pacific Islander"])
    counts[6] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "South Asian"])
    counts[7] = sum([len(a.dialog.split(" ")) for a in actors if a.race == "East Asian"])
    for i, count in enumerate(counts):
        percentage = count / total_dialog
        if percentage > 0.9:
            bars[i][0] += 1
        elif percentage > 0.7:
            bars[i][1] += 1
        elif percentage > 0.5:
            bars[i][2] += 1
        elif percentage > 0.3:
            bars[i][3] += 1
        elif percentage > 0.1:
            bars[i][4] += 1
        else:
            bars[i][5] += 1

bottoms = []
for i, b in enumerate(bars):
    bottom = [0, 0, 0, 0, 0, 0]
    for j in range(len(b)):
        for k in range(i):
            bottom[j] += bars[k][j]
    bottoms.append(bottom)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import pandas as pd

rc('font', weight='bold')
r = [0, 1, 2, 3, 4, 5]
names = ["+90%", "90-70%", "70-50%", "50-30%", "30-10%", "10-0%"]
barWidth = 0.75


plt.figure(figsize=(10, 10))


plt.bar(r, bars[0], color='#c7522a', edgecolor='white', width=barWidth, label='White')
plt.bar(r, bars[1], bottom=bottoms[1], color='#e5c185', edgecolor='white', width=barWidth, label='Black')
plt.bar(r, bars[2], bottom=bottoms[2], color='#f0daa5', edgecolor='white', width=barWidth, label='LatinX')
plt.bar(r, bars[3], bottom=bottoms[3], color='#fbf2c4', edgecolor='white', width=barWidth, label='Middle Eastern')
plt.bar(r, bars[4], bottom=bottoms[4], color='#b8cdab', edgecolor='white', width=barWidth, label='Native American')
plt.bar(r, bars[5], bottom=bottoms[5], color='#74a892', edgecolor='white', width=barWidth, label='Pacific Islander')
plt.bar(r, bars[6], bottom=bottoms[6], color='#008585', edgecolor='white', width=barWidth, label='South Asian')
plt.bar(r, bars[7], bottom=bottoms[7], color='#004343', edgecolor='white', width=barWidth, label='East Asian')

plt.figlegend(bbox_to_anchor=(0.5, 0.75), ncol=1)
plt.title("Dialog Composition by Race in Movies")
plt.xticks(r, names, fontweight='bold')
plt.xlabel("Percentage of Dialog Spoken by race")
plt.ylabel("Number of Movies (non-unique)")
 
plt.savefig("data/movie_race_composition")