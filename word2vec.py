import gensim
from gensim.models import word2vec,keyedvectors
# downloading word2vec by making google
import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
vec_king = wv['king']
shape = vec_king.shape
print('shape of the king vector is:',shape)
print('showing 300 arrays of king:\n',vec_king)

# getting vector array of teaching
vec_teaching = wv['teaching']

# showing most simillar words of teaching
simmilar_word = wv.most_similar('teaching')
print('most simillar word of teaching is:\n',simmilar_word)

## finding simmilarity between hockey and cricket
simillarity = wv.similarity('hockey','cricket')
print('similarity between hockey & cricket is:\n',simillarity)

#vectoring king - man + woman the output showing Queen 
vec = wv['king']-wv['man']+wv['woman']
similar_king=wv.most_similar([vec])
print('the output of the vec is:\n',similar_king)
