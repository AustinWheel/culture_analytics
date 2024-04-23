import json
from plot_wordfreq import create_cloud
def load_data(file):
    with open (file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)
    
data = load_data("data/freq_count.json")
for d in data:
    race = d[0]
    words = d[1]
    word_count = {}
    for word, count in words:
        word_count[word] = count
    create_cloud(word_count, f"data/{race}")

print("Wordclouds created!")