## porter stemmer
from nltk.stem import PorterStemmer 
words = ["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalize"]
stemming =PorterStemmer()
for word in words:
    print(word+"--->"+stemming.stem(word))


