from core.models import Actor
from collections import defaultdict
import json

def load_data(file):
    with open (file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

entities_race = load_data("data/named_entities.json")

all_entities = set()
for k, v in entities_race.items():
    for entity in v:
        all_entities.add(entity[0])

for a in Actor.objects.all():
    cleaned = a.cleaned
    new_words = []
    for word in cleaned.split(" "):
        if not word in all_entities:
            new_words.append(word)
    a.no_named = " ".join(new_words)
    a.save()