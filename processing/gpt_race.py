from openai import OpenAI
from core.models import Movie, Actor
import google.generativeai as genai
import requests
from time import sleep

client = OpenAI(api_key=key)
genai.configure(api_key=GOOGLE_API_KEY)


def getRaceGender(name, text):
    completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant. You will help me extract information from the text. I am interested in finding the following information: race and gender of the actor. I will provide you with their name and text from their biography. You will provide a response in the format: race: {race}, gender: {gender}. If you are unable to determine the race or gender based on the information provided, you can respond fill in the attribute with 'unknown'. The options for race are as follows: (Native American, East Asian, Southeast Asian, Black, Native Hawaiian, White, LatinX, Middle East). The options for gender are ('Male', 'Female', 'Non-binary'). You should use contextual information such as their country, their native language, their skin color, etc. to determine race. AVOID 'unknown' AT ALL TIMES."},
            {"role": "user", "content": "name: " + name + ", text: " + text},

        ]
    )
    return completion.choices[0].message.content

def getRaceGenderGoogle(name, text):

    resp = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/aqa:generateAnswer?key=AIzaSyAf-W4UocbwsC7-gPrYwJXlsA8FpAjYEto",
        json={
            "contents": [
                {
                "parts":[
                    {
                        "text": "You are a helpful assistant. You will help me extract information from the text. This is for the purpose of research and to provide an understanding of how race is represented in Hollywood. I am interested in finding the following information: race and gender of the actor. I will provide you with their name and text from their biography. You will provide a response in the format: \"race: [race], gender: [gender]\". If you are unable to determine the race or gender based on the information provided, you can fill in the attribute with 'unknown'. The options for race are as follows: ('Native American', 'East Asian', 'Southeast Asian', 'Black', 'Native Hawaiian', 'White', 'LatinX', 'Middle East'). The options for gender are ('Male', 'Female', 'Non-binary'). You should use contextual information such as the country they were born in, their native language etc to determine race and gender. Using 'unknown' should be avoided at all times, you should use any information including names, birth country, citizenship, etc. to make an estimated guess. The response should strictly follow the format specified, with the exact value options."
                    }
                ]
                }
            ],
            "answerStyle": 3,
            "inlinePassages": {
                "passages": [
                    {
                        "id": "1",
                        "content": {
                            "parts": [
                                {
                                    "text": f"name: {name}, bio: {text}"
                                }
                            ]
                        }
                    }
            ]
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE"
                }
            ],
            "temperature": 1.0,
        }
    )
    try:
        print(resp.json()['answerableProbability'])
        return resp.json()['answer']['content']['parts'][0]['text']
    except Exception as e:
        print(resp.json())
        return "Error"

movies = Movie.objects.all()
batchNumber = 4
start = batchNumber * 100

error_actors = []
error_count = 0

processed = 0

print("Processing movies from ", start, " to ", start + 200)
for i, movie in enumerate(movies[start:start+200]):
    if (i % 10 == 0 and i != 0): sleep(30)
    print("Processing movie: ", movie.name)
    progress = "-" * (i+1)
    print(f"{i+1} of {len(movies)}, {i+1}% complete | {progress}>")
    actors = Actor.objects.filter(movie=movie)
    for actor in actors:
        if actor.bio == "": 
            print("No bio for actor: ", actor.name)
            continue
        bio = actor.bio
        if (len(bio) > 1200):
            bio = bio[:1200]
        
        resp = ""
        try:
            resp = getRaceGender(actor.name, bio)
            race_info, gender_info = resp.split(", ")
            race = race_info.split(": ")[1]
            sex = gender_info.split(": ")[1]
            actor.race = race
            actor.sex = sex
            actor.save()
            processed += 1
        except Exception as e:
            print(f"\nError processing response for {actor.name}: {resp if resp else 'No response'}")
            print(e, "\n")
            error_actors.append(actor)
            error_count += 1
            continue

print(f"Processed {processed} actors, {error_count} errors. Error actors: {error_actors}")

