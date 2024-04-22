from core.models import Actor, Movie
from bs4 import BeautifulSoup
import re

def extract_dialogues(text):
    pattern = r'([A-Z\s]+)\n(.*?)(?=\n{2,}|$)'
    dialogues = re.findall(pattern, text, re.DOTALL)
    for dialogue in dialogues:
        speaker = dialogue[0].strip()
        speech = dialogue[1].strip()
        print(f'Speaker: {speaker}\nSpeech: {speech}\n')

def check_name(text, name):
    name = name.lower().strip()
    name = name.replace('mr.', '').replace('mrs.', '').replace('ms.', '').replace('dr.', '').replace('prof.', '').replace('sr.', '').replace('jr.', '')
    name = name.split(' ')
    for n in name:
        if n == "": continue
        if n in text.lower():
            return True
    return False

def get_actor_dialog(actor, script):
    name = actor.role
    soup = BeautifulSoup(script, 'html.parser')
    soup = soup.text.split("\n")
    dialog =[]

    i = 1
    while i < len(soup):
        line = soup[i].strip()
        pLine = soup[i-1].strip()
        if check_name(line, name) and pLine == "":
            i += 1
            while i < len(soup) and soup[i].strip() != "":
                dialog.append(soup[i].strip())
                i += 1
        i += 1
    dialog = "\n".join(dialog)
    
    actor.dialog = dialog
    actor.save()


all_actors = Actor.objects.all()
errors = []
for i, actor in enumerate(all_actors[::-1]):
    if i % 50 == 0:
        progress = "=" * int(((i / len(all_actors)) * 100)//10)
        print(f"Processed {i}> actors : {i}/{len(all_actors)}, {i/len(all_actors) * 100}% | {progress}>")
    try:
        get_actor_dialog(actor, actor.movie.script)
    except Exception as e:
        print(f"Error gettings dialog for {actor.name} : {e}")
        errors.append(actor.name)

print(f"Ran into {len(errors)} errors for actors: ", errors)