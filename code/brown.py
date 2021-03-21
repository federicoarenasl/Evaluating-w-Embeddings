from nltk.corpus import brown 
from collections import defaultdict
from math import log
from nltk.stem import *
from nltk.stem.porter import *

STEMMER = PorterStemmer()

tf = defaultdict(int)
df = defaultdict(int)

def preprocess_word(word):
    word = word.lower() #remove capital letters
    return STEMMER.stem(word)


doc_num = 0
for cat in brown.categories():
    cat_ids = brown.fileids(categories=cat)
    for id in cat_ids:
        sequence_of_words = brown.words(id)
        sequence_of_words = [preprocess_word(word) for word in sequence_of_words]
        for word in sequence_of_words:
            tf[(word,doc_num)] += 1
        
        word_set = set(sequence_of_words)
        for word in word_set:
            df[word] += 1

        print('Finished ', doc_num)
        doc_num += 1

w = defaultdict(list)

for term in df.keys():
    tf_idf_vector = []
    for doc in range(doc_num):
        tf_idf_vector.append(log(tf[(term, doc)]+1,10)*log((doc_num+1)/df[term]))
    w[term] = tf_idf_vector


