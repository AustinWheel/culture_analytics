from core.models import Movie
from bs4 import BeautifulSoup
import requests

all_movies = Movie.objects.all()

deleted_urls = []

for i, movie in enumerate(all_movies):
    if i % 50 == 0:
        print(f"Processing movie {i} of {len(all_movies)}, {i/len(all_movies)*100:.2f}% complete.")
    try:
        url = movie.url
        n = movie.url.split('/')[-1]
        name = n.split('.')[0]


        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

        links = soup.find_all('a', href=True)
        valid_links = [link['href'] for link in links if link['href'].startswith('/scripts/')]
        if valid_links:
            movie.script_url = "https://imsdb.com" + valid_links[0]
            movie.name = name
            movie.save()
        else:
            print(f"No script found for {movie.url}")
            deleted_urls.append(name)
            movie.delete()
    except Exception as e:
        print(f"Error fetching script for {movie.url}: {e}")
        continue

print(f"Deleted {len(deleted_urls)} movies: {deleted_urls}")