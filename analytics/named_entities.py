import json
from plot_wordfreq import create_cloud
def load_data(file):
    with open (file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)
    
data = load_data("data/named_entities.json")
for race, d in data.items():
    freq_count = {}
    for entity, count in d:
        e = entity.lower()
        if len(freq_count.keys()) > 19: break
        if e=="" or e in ("one","two","three","four","five"): continue
        freq_count[entity] = count
        
    create_cloud(freq_count, f"data/named_entities/{race}")