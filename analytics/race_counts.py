from core.models import Actor
from collections import defaultdict
race_count = defaultdict(int)

for a in Actor.objects.all():
    if a.race == "" or a.race == "Unknown": continue
    race_count[a.race] += 1
    
for k, v in race_count.items():
    print(f"Race: {k}, total actors: {v}")