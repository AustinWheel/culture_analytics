import string
from nltk.corpus import stopwords
import re

def remove_stops(text, stops):
    text = re.sub(r"AC\/\d{1,4}\/\d{1,4}", "", text)
    words = text.split()
    final = []
    for word in words:
        if word not in stops:
            final.append(word)
    final = " ".join(final)
    final = final.translate(str.maketrans("", "", string.punctuation))
    final = "".join([i for i in final if not i.isdigit()])
    while "  " in final:
        final = final.replace("  ", " ")
    return (final)


from core.models import Actor
stops = stopwords.words("english")
for a in Actor.objects.all():
    description = a.dialog
    cleaned = remove_stops(description, stops)
    a.cleaned = cleaned
    a.save()
