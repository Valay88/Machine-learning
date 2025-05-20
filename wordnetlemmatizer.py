import nltk
nltk.download('wordnet') 
from nltk.stem import WordNetLemmatizer
#creating lemmatizer variable and call the function
lemmatizer = WordNetLemmatizer()
words = ['eating','eats','eaten','writing','writes','programming','programs','history','finally','finalized','wrote']
for word in words:
    print(word+'--->'+lemmatizer.lemmatize(word,pos='v'))