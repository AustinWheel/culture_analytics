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

races = set()
all_actors = Actor.objects.all()
for a in all_actors:
    if a.race != "" and a.race != "unknown": races.add(a.race)
races = list(races)

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

data.sort(key=lambda x: x[1] + x[2])
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
    
data.sort(key=lambda x: x[1])
print(tabulate(data, headers=["Race", "Average words per line", "Total words spoken", "Lines of dialog"], tablefmt='orgtbl'))
    
