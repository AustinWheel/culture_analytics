'''
Retrieves the page content from imsdb.com/all-scripts.html and saves it to a file.
This contains links to every movie script on the site.

processing/extract_urls.py will extract the URLs from this file.
'''

import requests
from bs4 import BeautifulSoup

url = "https://imsdb.com/all-scripts.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    with open("data/all_scripts.html", "w") as file:
        file.write(str(soup))
else:
    print("Error fetching the page.")