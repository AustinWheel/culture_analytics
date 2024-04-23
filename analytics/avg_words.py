print('\n\n')
print('#                       Counts the average words by Race                    #')
print('# ------------------------------------------------------------------------- #')
print('#   Average words including stopwords (ie: the, and, etc) and punctuation   #')
print('#   Average words cleaned removes the filler words                          #')
print('#   Max words by single actor is the highest word count by a single actor   #')
print('# ------------------------------------------------------------------------- #')


from core.models import Actor
from tabulate import tabulate
import re
import matplotlib.pyplot as plt


races = list()
all_actors = Actor.objects.all()
for a in all_actors:
    if a.race != "" and a.race != "unknown" and a.race not in races: races.append(a.race)

def clean_and_get_count(text):
    re.sub(r'\n', ' ', text)
    re.sub(r'\t', ' ', text)
    while "  " in text:
        text = text.replace("  ", " ")
    words = text.split(" ")
    return len(words)

data = []

for race in races:
    actors = Actor.objects.filter(race=race)
    total_words = 0
    total_words_cleaned = 0
    max_words = 0
    for actor in actors:
        words = clean_and_get_count(actor.dialog)
        words_cleaned = clean_and_get_count(actor.cleaned)
        total_words += words
        total_words_cleaned += words_cleaned
        max_words = max(max_words, words)

    avg_words = total_words / len(actors)
    avg_words_cleaned = total_words_cleaned / len(actors)
    data.append([race, avg_words, avg_words_cleaned, max_words])

race_data = [ d[0] for d in data ]
avg_words_data = [ d[1] for d in data ]

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))
plt.bar(race_data, avg_words_data, color=['#c7522a', '#e5c185', '#f0daa5', '#004343', '#008585', '#fbf2c4', '#b8cdab', '#74a892'])
plt.xlabel('Race')
plt.ylabel('Average Words per Film')
plt.title('Actors: Average Words, by Race')
plt.xticks(rotation=0)

for i, v in enumerate(avg_words_data):
    word = str(v)[::-1]
    word = ','.join([word[i:i+3] for i in range(0, len(word), 3)])[::-1]
    plt.text(i, v+1000, str(word), fontsize=12, fontfamily='monospace', horizontalalignment='center')

plt.savefig('data/avg_dialog')

print(tabulate(data, headers=['Race', 'Average Words', 'Average Words Cleaned', 'Max Words by Single Actor'], tablefmt='orgtbl'))
print("\n\n")


print('#          Counts the average words per line of dialog by Race              #')
print('#   ---------------------------------------------------------------------   #')
print('#   Average words including stopwords (ie: the, and, etc) and punctuation   #')
print('#   Total words is the sum of all words spoken by actors of a race          #')
print('#   Lines of dialog is the total number of lines spoken by actors           #')
print('#   ---------------------------------------------------------------------   #')

data = []
for race in races:
    actors = Actor.objects.filter(race=race)
    total_words = 0
    lines_spoken = 0
    for actor in actors:
        for line in actor.dialog.split("\n"):
            total_words += len(line.split(" "))
        lines_spoken += actor.lines_spoken
    data.append([race, total_words / lines_spoken, total_words, lines_spoken])
    
# data.sort(key=lambda x: x[1])
print(tabulate(data, headers=["Race", "Average words per line", "Total words spoken", "Lines of dialog"], tablefmt='orgtbl'))

race_data = [ d[0] for d in data ]
avg_words_data = [ d[1] for d in data ]

plt.figure(figsize=(14, 6))
plt.bar(race_data, avg_words_data, color=['#c7522a', '#e5c185', '#f0daa5', '#004343', '#008585', '#fbf2c4', '#b8cdab', '#74a892'])
plt.xlabel('Race')
plt.ylabel('Average Words per Speech Turn')
plt.title('Actors: Average Words per Speech Turn, by Race')
plt.xticks(rotation=0)

for i, v in enumerate(avg_words_data):
    word = str(v)[::-1]
    word = ','.join([word[i:i+3] for i in range(0, len(word), 3)])[::-1]
    plt.text(i, v+1000, str(word), fontsize=12, fontfamily='monospace', horizontalalignment='center')

plt.savefig('data/avg_by_line')
