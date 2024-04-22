from core.models import Actor
from tabulate import tabulate
from collections import defaultdict

races = set()
all_actors = Actor.objects.all()
for a in all_actors:
    if a.race != "" and a.race != "unknown" : races.add(a.race)
races = list(races)


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
            if percentages[word] < 0.20 and word != "": counts[word] += 1
    list_counts = [ [ k, v ] for k, v in counts.items() ]
    list_counts.sort(key=lambda x: x[1], reverse=True)
    top = [ x[0] for x in list_counts[:10] ]
    top = str(top)
    top_words.append([race, top])

print(tabulate(top_words, headers=["Race", "Top 10 Words"], tablefmt='orgtbl'))

# need to remove named entities
# I want to keep the current cleaned data so I should make a new attribute that has cleaned data without named entities
# I will remove words that are entirely uppercase from cleaned and the new attribute
# Then for words that only start with uppercase, I will not add those to the new attribute.