from core.models import Movie
from bs4 import BeautifulSoup
import requests
from time import sleep

all_movies = Movie.objects.all()

deleted_movies = []

for i, movie in enumerate(all_movies):
    if i % 50 == 0:
        print(f"Processing movie {i} of {len(all_movies)}, {i/len(all_movies)*100:.2f}% complete.")
    try:
        url = movie.script_url
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
        else: raise Exception("Error fetching the page", response.status_code)

        movie.script = soup.find('pre').text
        movie.save()
    except Exception as e:
        print(f"Error fetching script for {movie.script_url}: {e}")
        deleted_movies.append(movie.name)
        movie.delete()
        continue

print(f"Deleted {len(deleted_movies)} movies: {deleted_movies}")