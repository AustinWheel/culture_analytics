# the goal of this analysis is to find the total words of dialogue spoken by each race
import matplotlib.pyplot as plt
from core.models import Actor
from collections import defaultdict

counts = defaultdict(int)
for a in Actor.objects.all():
    if a.race == 'unknown' or a.race=="": continue
    
    dialog = a.dialog
    while '\n' in dialog: 
        dialog = dialog.replace('\n', ' ')
    counts[a.race] += len(dialog.split(" "))

all = counts.items()
all = sorted(all, key=lambda x: x[1], reverse=True)

races = [x[0] for x in all]
words = [x[1] for x in all]

plt.figure(figsize=(10, 6))
plt.bar(races, words, color=['#c7522a', '#e5c185', '#f0daa5', '#004343', '#008585', '#fbf2c4', '#b8cdab', '#74a892'])
plt.xlabel('Race')
plt.ylabel('Total Words')
plt.title('Actors: Total Words, by Race')
plt.xticks(rotation=0)

for i, v in enumerate(words):
    word = str(v)[::-1]
    word = ','.join([word[i:i+3] for i in range(0, len(word), 3)])[::-1]
    plt.text(i, v+1000, str(word), fontsize=12, fontfamily='monospace', horizontalalignment='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('data/total_words_by_race')
