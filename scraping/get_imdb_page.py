import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.models import Actor, Movie

driver = webdriver.Chrome()
def get_page_source(url):
    if not url: return None
    try:
        driver.get(url)
        # WebDriverWait(driver, 5)
        page = driver.page_source
        return page
    except Exception as e:
        print(f"Error getting page source for {url} : {e}")
        return None

def get_actors(movie):
    url = f"https://www.imdb.com/find/?q={movie.name}"
    initial_page = get_page_source(url)
    soup = BeautifulSoup(initial_page, 'html.parser')

    links = soup.find_all('a', href=True)
    valid_links = [link['href'] for link in links if link['href'].startswith('/title/')]
    first_link = "https://www.imdb.com" + valid_links[0] if valid_links else None

    page = get_page_source(first_link)
    soup = BeautifulSoup(page, 'html.parser')

    cast = soup.select('a[data-testid="title-cast-item__actor"]')
    characters = soup.select('a[data-testid="cast-item-characters-link"]')
    for actor, character in zip(cast, characters):
        actor = Actor.objects.create(name=actor.text, role=character.span.text, movie=movie)
        actor.save()
    
all_movies = Movie.objects.all()
errors = []
for i, movie in enumerate(all_movies):
    if i % 10 == 0:
        progress = "=" * int(((i / len(all_movies)) * 100)//10)
        print(f"Processed {progress}> movies : {i}/{len(all_movies)}, {i/len(all_movies) * 100}%")
    try:
        get_actors(movie)
    except Exception as e:
        print(f"Error gettings actors for {movie.name} : {e}")
        errors.append(movie.name)

print(f"Ran into {len(errors)} for movies: {errors}")
driver.quit()

