from core.models import Actor, Movie
from bs4 import BeautifulSoup
import requests

def get_actors_wiki(name):
    url = f"https://en.wikipedia.org/w/index.php?search={name}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.title.text

    if "search results" in title.lower():
        search_results = soup.find('ul', class_='mw-search-results')

        first_result = search_results.find('li')
        first_result_link = first_result.find('a')['href']
        first_result_link.replace("https://en.wikipedia.org", "")
        resp = requests.get(f"https://en.wikipedia.org{first_result_link}")
        soup = BeautifulSoup(resp.text, 'html.parser')

    pTags = soup.find_all('p')
    information = []
    for pTag in pTags:
        information.append(pTag.text)

    bio = "\n".join(information)
    return bio

all_actors = Actor.objects.all()
errors = []
for i, actor in enumerate(all_actors):
    if i % 10 == 0:
        progress = "=" * int(((i / len(all_actors)) * 100)//1)
        print(f"Processed {i}> actors : {i}/{len(all_actors)}, {i/len(all_actors) * 100}% | {progress}")
    try:
        actor.bio = get_actors_wiki(actor.name)
        actor.save()
    except Exception as e:
        print(f"Error gettings actors for {actor.name} : {e}")
        errors.append(actor.name)

print(f"Ran into {len(errors)} errors for actors: ", errors)