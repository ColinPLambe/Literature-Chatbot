
import json
import random
import nltk
import sumy
import numpy as np
import string
from nltk.tokenize import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

LANGUAGE = "english"
stemmer = Stemmer(LANGUAGE)
sentences = 3

lemmer = nltk.stem.WordNetLemmatizer()


with open('all_books.json') as file:
    metadata = json.load(file)[0]

with open('all_reviews.json') as file:
    reviews = json.load(file)
    cleaned_reviews = {}
    for review in reviews:
        if review["book_title"] not in cleaned_reviews:
            cleaned_reviews[review["book_title"]] = []
            print("Reviews for ", review["book_title"])

        text = review['text']

        parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
        summarizer = LexRankSummarizer(stemmer)
        summary = summarizer(parser.document, sentences)
        summary_str = ""
        for sentence in summary:
            summary_str += str(sentence) + "\n"

        cleaned_reviews[review["book_title"]].append(summary_str)

with open('cleaned_reviews.json', 'w') as file:
    json.dump(cleaned_reviews, file)



print(metadata.keys())
print(random.choice(cleaned_reviews.get('Siddhartha')))



def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
