import gensim
from gensim.models import word2vec,keyedvectors
# downloading word2vec by making google
import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
vec_king = wv['king']
shape = vec_king.shape
print('shape of the king vector is:',shape)
print('showing 300 arrays of king:\n',vec_king)
vec_teaching = wv['teaching']
simmilar_word = wv.most_similar('teaching')
print('most simillar word of teaching is:\n',simmilar_word)
simillarity = wv.similarity('hockey','cricket')
print('similarity between hockey & cricket is:\n',simillarity)
vec = wv['king']-wv['man']+wv['woman']
similar_king=wv.most_similar([vec])
print('the output of the vec is:\n',similar_king)
