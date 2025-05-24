import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# reading file 
message = pd.read_csv('SMSspamcollection.csv')

#calling lemmatization
lemmatiozer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

#data cleaning
corpus = []
for i in range(0,len(message)):
    review = re.sub('[^a-zA-Z]',' ',message['message'][i])
    review = review.lower()
    review = review.split()
    review = [lemmatiozer.lemmatize(word) for word in review if word not in stop_words]
    review = ' '.join(review)
    corpus.append(review)
print('after cleaning data:',corpus[:5])

# build model with use of BOW
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer (max_features= 200, binary= True, ngram_range=(1,2))
x = cv.fit_transform(corpus).toarray()
print ('first represent size of sentences & second represent feature which we use:',x.shape)
print(cv.vocabulary_)
