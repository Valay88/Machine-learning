from nltk.stem import RegexpStemmer
words = ['eating','played','takes','limited','ped']
reg_expression = RegexpStemmer('ing$|s$|ed$',min=4)
for word in words:
    print(word+"--->"+reg_expression.stem(word))