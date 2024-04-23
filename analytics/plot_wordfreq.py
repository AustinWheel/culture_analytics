from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def create_cloud( word_freq: dict, fName ):
    '''
    word_freq = { word : frequency }
    fName = `name of the file to save the wordcloud`
    '''
    mask = np.array(Image.open("data/circle_mask.png"))
    
    wordcloud = WordCloud(width=800, height=800, background_color='black', mask=mask).generate_from_frequencies(word_freq)
    
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Create bar plot of word frequencies
    plt.subplot(2, 1, 2)
    words = list(word_freq.keys())
    frequencies = list(word_freq.values())
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Word Frequencies')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(fName+'-wordfreq.png')
    
