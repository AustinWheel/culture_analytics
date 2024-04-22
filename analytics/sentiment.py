from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import defaultdict
from core.models import Actor

analyzer = SentimentIntensityAnalyzer()

sentiment_scores = defaultdict(list)

progress = 0
total = Actor.objects.count()

for actor in Actor.objects.all():
    print(f"Progress: {progress}/{total}") if progress % 100 == 0 else None
    progress += 1
    sentiment_score = analyzer.polarity_scores(actor.no_named)['compound']
    sentiment_scores[actor.race].append(sentiment_score)

print("Sentiment analysis complete.")
average_sentiment_scores = {}
for race, scores in sentiment_scores.items():
    average_sentiment_scores[race] = sum(scores) / len(scores)

for race, score in average_sentiment_scores.items():
    print(f"Average sentiment score for {race}: {score}")
    
'''
Output for actor.dialog:
    Average sentiment score for White: 0.14342430685067806
    Average sentiment score for Black: 0.09744656084656075
    Average sentiment score for LatinX: 0.07486021798365125
    Average sentiment score for unknown: 0.09791107692307692
    Average sentiment score for Southeast Asian: 0.06145999999999999
    Average sentiment score for : 0.12646124563923672
    Average sentiment score for Middle East: 0.09990062893081758
    Average sentiment score for East Asian: 0.02751417004048584
    Average sentiment score for Native American: 0.005965454545454528
    Average sentiment score for Pacific Islander: -0.20407727272727277
    
Output for actor.no_named:
    Average sentiment score for White: 0.09591319159517597
    Average sentiment score for Black: 0.052138624338624304
    Average sentiment score for LatinX: 0.09937029972752048
    Average sentiment score for unknown: 0.06659999999999996
    Average sentiment score for Southeast Asian: 0.03516926829268294
    Average sentiment score for : 0.07357949928175686
    Average sentiment score for Middle East: 0.037946540880503137
    Average sentiment score for East Asian: 0.0344246963562753
    Average sentiment score for Native American: -0.05919818181818182
    Average sentiment score for Pacific Islander: -0.2198227272727273
'''
