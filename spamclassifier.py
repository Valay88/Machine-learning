import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

## reading csv file data 
message = pd.read_csv('SMSspamcollection.csv')

#calling porter stemmer function with variable
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

#cleaning the data 
corpus = []
for i in range(0,len(message)):
    #removing regular expression with using substitute function (from small a to z and A to Z apart from this remove all special character)
    review = re.sub('[^a-zA-Z]',' ',message['message'][i])
    #lower all the case
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in stop_words]
    review = ' '.join(review)
    corpus.append(review)
print('After cleaning data:',corpus[:5])
