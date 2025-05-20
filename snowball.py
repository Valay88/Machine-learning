from nltk.stem import SnowballStemmer
words = ['eating','eats','eaten','writing','wrties','programming','programs','finally','finalize']
snowballstemming = SnowballStemmer('english')
for word in words:
    print(word+'--->'+snowballstemming.stem(word))
    