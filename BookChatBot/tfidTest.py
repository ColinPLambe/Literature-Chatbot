import pandas as pd
import numpy as np
import re
import nltk
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cdist

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    # lowercase and remove special characters\whitespace
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I | re.A)
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)

    return doc

def choose_review(input, reviews):
    #a specific book was found and we have the review list for that bok
    corpus = reviews.copy()
    corpus.insert(0, input)

    normalize_corpus = np.vectorize(normalize_document)
    norm_corpus = normalize_corpus(corpus)

    tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2',
    use_idf=True, smooth_idf=True)
    tv_matrix = tv.fit_transform(norm_corpus)
    tv_matrix = tv_matrix.toarray()
    vocab = tv.get_feature_names()

    #print(pd.DataFrame(np.round(tv_matrix, 2), columns=vocab))

    dists = cdist([tv_matrix[0]], tv_matrix[1:])[0]

    min = dists[1]
    min_index = 1
    for i in range(1, len(dists)):
        if dists[i] < min:
            min = dists[i]
            min_index = i
    return reviews[min_index]
