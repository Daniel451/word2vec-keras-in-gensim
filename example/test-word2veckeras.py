import sys
import numpy as np
import gensim
from word2veckeras.word2veckeras import Word2VecKeras

def compare_w2v(w2v1,w2v2):
    s=0.0
    count =0
    for w in w2v1.vocab:
        if w in w2v2.vocab:
            d=np.linalg.norm(w2v1[w]-w2v2[w])
            count +=1
            s += d
    return s/count


input_file = 'test.txt'
sents=gensim.models.word2vec.LineSentence(input_file)

v_iter=1
v_size=5
sg_v=1
topn=4

vs1 = gensim.models.word2vec.Word2Vec(sents,hs=1,negative=0,sg=sg_v,size=v_size,iter=1)
                      
print vs1['the']
vsk1 = Word2VecKeras(sents,hs=1,negative=0,sg=sg_v,size=v_size,iter=1)
print( vsk1.most_similar('the', topn=topn))
print vsk1['the']
print np.linalg.norm(vs1.syn0-vsk1.syn0),compare_w2v(vs1,vsk1)
vsk1 = Word2VecKeras(sents,hs=1,negative=0,sg=sg_v,size=v_size,iter=5)
print vsk1['the']
print( vsk1.most_similar('the', topn=topn))
print( vs1.most_similar('the', topn=topn))
print np.linalg.norm(vs1.syn0-vsk1.syn0),compare_w2v(vs1,vsk1)


from nltk.corpus import brown
#brown_sents=list(brown.sents())[:2000]
brown_sents=list(brown.sents())

#for sg_v in [1,0]:
for sg_v in [0]:    
    print sg_v
    brc = gensim.models.word2vec.Word2Vec(brown_sents,hs=1,negative=0,sg=sg_v,iter=1)
    print brc.most_similar_cosmul(positive=['she', 'him'], negative=['he'], topn=topn)
    #ns=[1,2,5,10,20]
    ns=[100]
    for n in ns :
        print n
        brck = Word2VecKeras(brown_sents,hs=1,negative=0,iter=n,sg=sg_v)
        print compare_w2v(brc,brck)
        print brck.most_similar_cosmul(positive=['she', 'him'], negative=['he'], topn=topn)
    
    

