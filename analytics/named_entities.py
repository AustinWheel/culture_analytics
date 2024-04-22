from core.models import Actor

all_actors = Actor.objects.all()
for a in all_actors:
    cleaned = a.cleaned.split(" ")
    no_named = []
    for word in cleaned:
        if word.isupper():
            cleaned.remove(word)
        elif word and not word[0].isupper():
            no_named.append(word)
    a.no_named = " ".join(no_named)
    a.save()