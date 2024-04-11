'''
To run this script, you need to have the Django project running and the database set up.
You can run this with the command `python manage.py shell < processing/extract_urls.py`.
'''
from bs4 import BeautifulSoup
from core.models import Movie

with open('data/all_scripts.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# The anchor tags contain the URLS to the movie scripts
# We only want the links to the movies, so we can just consider those that start with "/Movie Scripts/".
links = soup.find_all('a', href=True)
movie_script_urls = ["https://imsdb.com/" + link['href'] for link in links if link['href'].startswith('/Movie Scripts/')]

Movie.objects.bulk_create([Movie(url=url) for url in movie_script_urls])
