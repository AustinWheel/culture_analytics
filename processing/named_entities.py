from core.models import Actor
from collections import defaultdict
import spacy

nlp = spacy.load("en_core_web_sm")

all_actors = Actor.objects.all()
named_entities_by_race = defaultdict(list)

races = set()
for a in all_actors:
    if a.race != "" and a.race != "unknown": races.add(a.race)

for race in races:
    actors = Actor.objects.filter(race=race)
    for a in actors:
        doc = nlp(a.dialog)
        for ent in doc.ents:
            named_entities_by_race[race].append(ent.text)
            
for race, entities in named_entities_by_race.items():
    entity_count = defaultdict(int)
    for entity in entities: entity_count[entity] += 1
    named_entities_by_race[race] = sorted(entity_count.items(), key=lambda x: x[1], reverse=True)

import json
with open('data/named_entities', 'w') as f:
    json.dump(named_entities_by_race, f, indent=2)