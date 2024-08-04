import nltk
import re
import string
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
stop_words=nltk.corpus.stopwords.words('english')
punctuations=set(string.punctuation)
#Creating Frequency Distributions
def process(text):
    res=sia.polarity_scores(text)
    pprint(res)
process("i am sad asf i hate myself ")