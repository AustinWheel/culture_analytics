# Culture Analytics of Race Depiction in Films

## Introduction
For an introduction of my reasons to explore this topic, please see the [Blog Post](https://austinwheeler.hashnode.dev/race-in-cinema). This project aims to understand the depiction of race in films by analyzing the dialog spoken by actors of different races and performing different text analysis techniques to find and understand any differences.

## Data

Data was scraped from the [IMSDB](https://www.imsdb.com/) website. The IMSDB website is a database of movie scripts that are freely available to the public. I scraped all of the scripts (~1200 movies) from the website. For each movie I scraped the `Top Cast` section from IMDB if there was an IMDB page available. For each actor in the `Top Cast` section, I scraped their Wikipedia page if one was available (For actors who did not immediately have a wikipedia page I manually selected the link during a semi-auto scraping process). With the wikipedia page of the actors I scraped each actor's entire biography. With the biography of the actors I was able to upload this to the `GPT-4-Turbo-Preview` API to identify the race of the actor.

Race could be one of eight values: White, Black, LatinX, Middle Eastern, Southeast Asian, East Asian, Native American, and Pacific Islander. These options come from a paper by Malik et al. "Representation of Racial Minorities in Popular Movies".

## Text Analysis

The text analysis methods I used are as follows:
- Word Count Analysis
  - Average Number of Words Spoken by Actors.
  - Average Length of a Speech turn by Actors.
  - Movie Dialogue Composition by Race.
  - Total words spoken by Race.
- Sentiment Analysis
- Frequency Analysis
- Named Entity Recognition

These are discussed in greater detail in the linked [blog post](https://austinwheeler.hashnode.dev/race-in-cinema)

The code for the analytics can be found in the `analytics` directory. The code is written in Python and uses Django for storing and managing the data in SQL. The code for scraping the data can be found in the `scraping` directory. Any data processing and cleaning I did is also found in the `processing` directory. Dependencies are listed in `requirements.txt` and can be installed with `pip install -r requirements.txt`. Documentation for using Django can be found [here](https://docs.djangoproject.com/en/4.0/).

I can provide a dump of the data that I scraped if you reach out to me at austinwheeler1112@gmail.com
