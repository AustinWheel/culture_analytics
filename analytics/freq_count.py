from core.models import Actor
from tabulate import tabulate
from collections import defaultdict
import json

races = []
all_actors = Actor.objects.all()
for a in all_actors:
    if a.race != "" and a.race != "unknown" and a.race not in races: races.append(a.race)

percentages = defaultdict(int)
total_actors = 0
for a in all_actors:
    unique_words = set()
    for word in a.no_named.lower().split(" "): unique_words.add(word)
    for word in unique_words:
        percentages[word] += 1
    total_actors += 1
for k, v in percentages.items():
    percentages[k] = v / total_actors


top_words = []
for race in races:
    actors = Actor.objects.filter(race=race)
    counts = defaultdict(int)
    for a in actors:
        for word in a.no_named.lower().split(" "): 
            if percentages[word] < 0.10 and word != "" and len(word) > 2: counts[word] += 1
    list_counts = [ [ k, v ] for k, v in counts.items() ]
    list_counts.sort(key=lambda x: x[1], reverse=True)
    top = [ x for x in list_counts[:30] ]
    # top = str(top)
    top_words.append([race, top])

# print("\n")
# print(tabulate(top_words, headers=["Race", "Top 30 Words"], tablefmt='orgtbl'))
# print("\n")
with open('data/freq_count.json', 'w') as f:
    json.dump(top_words, f, indent=2)