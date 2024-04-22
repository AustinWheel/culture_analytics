import matplotlib.pyplot as plt

sentiment_scores = [
    ["White", 0.09591319159517597],
    ["Black", 0.052138624338624304],
    ["LatinX", 0.09937029972752048],
    ["Southeast Asian", 0.03516926829268294],
    ["Middle East", 0.037946540880503137],
    ["East Asian", 0.0344246963562753],
    ["Native American", -0.05919818181818182],
    ["Pacific Islander", -0.2198227272727273]]

plt.figure(figsize=(10, 6))
plt.barh([ a[0] for a in sentiment_scores ], [ a[1] for a in sentiment_scores ], color='skyblue')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Racial Groups')
plt.title('Average Sentiment Score by Racial Group')
plt.gca().invert_yaxis()
plt.savefig('data/sentiment.png')