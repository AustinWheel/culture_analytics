'''
Issue where some movie names have "Script" or ", The Script" at the end of the name.
Need to clean the names of these movies. so that the names are consistent, and this makes using
external lookup easier like wikipedia or IMDB.
'''

from core.models import Movie
from time import sleep
all_movies = Movie.objects.all()

error_movies = []

for i, movie in enumerate(all_movies):
    if i % 50 == 0:
        print(f"Processing movie {i} of {len(all_movies)}, {i/len(all_movies)*100:.2f}% complete.")
    try:
        name = movie.name
        name = name.replace(", The Script", "")
        name = name.replace(" Script", "")
        movie.name = name
        movie.save()
    except Exception as e:
        print(f"Error renaming movie for {movie.name}: {e}")
        error_movies.append(movie.name)
        continue

print(f"Errors renaming {len(error_movies)} movies: {error_movies}")