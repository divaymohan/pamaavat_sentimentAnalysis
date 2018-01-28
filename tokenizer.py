import re
import json
from collections import Counter
from textblob import TextBlob

emoticons_str = r"""
(?:
   [:=;] #Eyes
   [oO\-]? #Nose (optional)
   [D\)\]\(\]/\\OpP] #Mouth
)"""
regex_str = [
    emoticons_str,
    r'<[^>]+>', #html tag
    r'(?:@[\w_]+)', # @mention
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)" ,# hash tags
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' ,#urls
    r'(?:(?:\d+,?)+(?:\,?\d+)?)', #numbers
    r"(?:[a-z][a-z'\-_]+[a-z])" ,#words with - and
    r'(?:[\w_]+)', #other words
    r'(?:\S)' #anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')',re.VERBOSE | re.IGNORECASE)
emotion_re = re.compile(r'^'+emoticons_str+'$',re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)
def preprocess(s,lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emotion_re.search(token) else token.lower() for token in tokens]
    return tokens

from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english')
fname = 'padmaavat.json'

with open(fname,'r',newline='\r\n') as f:
    count = 0
    count_all = Counter()
    for line in f:
        if line.strip():

            tweet = json.loads(line)
            txtblb = TextBlob(tweet["text"]).sentiment
            print(tweet,txtblb.polarity,txtblb.subjectivity)
            if(txtblb.subjectivity*100>60):
                output = open("padmavat.txt",'a')
                output.write(str(txtblb.polarity))
                output.write('\n')
                output.close()

            #create a list with all the terms

            count = count+1
            print(count)
            print(preprocess(tweet['text']))

            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            #count terms only once, equivalent to Document Frequency
            term_single = set(terms_stop)
            #count hash tags only
            term_hash = [term for term in preprocess(tweet['text']) if term.startswith("#")]
            #Count term only (no hashtag no mention)
            term_only = [term for term in preprocess(tweet['text'].lower()) if term not in stop]

            term_all = [term for term in preprocess(tweet['text'])]
        new_term =[]
        for term in term_only:
            if len(term) > 3:
                new_term.append(term)


        #update the counnter
        count_all.update(new_term)

    print(count_all.most_common(50))
import  matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

data = count_all.most_common(50)
df = pd.DataFrame(data)
df.columns= ('terms','frec')
print(df.head())
word_string = ' '
for index, row in df.iterrows():
    word_string += (row['terms'] + ' ')*row['frec']

wordcloud = WordCloud(font_path = 'Aaargh.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1200,
                      height = 1000
                      ).generate(word_string)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()