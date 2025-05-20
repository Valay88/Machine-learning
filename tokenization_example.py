import nltk
print("Downloading punkt...")
nltk.download('punkt')

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize 

corpus = """Hello , My name is Valay Panchal and welcome to my NLP tutorial.
please watch my full tutorial! to get expert in NLP
"""

print("Tokenized Sentences:")
print(sent_tokenize(corpus))

print("tokenize word:")
print(word_tokenize(corpus))