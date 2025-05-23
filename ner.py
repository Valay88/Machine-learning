import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import word_tokenize
sentence="""The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures."
"""
# tokenize word
words = word_tokenize(sentence)
print('Token:',words)

#part of speech tagging
tag_elements = nltk.pos_tag(words)
print('POS tag is:',tag_elements)

#Named entity recognization
chunk = nltk.ne_chunk(tag_elements)
chunk.draw()
