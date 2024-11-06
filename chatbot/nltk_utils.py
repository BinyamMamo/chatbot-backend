import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

# Download all required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('tokenizers/punkt/PY3/english.pickle')
except LookupError:
    nltk.download('punkt')

stemmer = PorterStemmer()

def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    try:
        return nltk.word_tokenize(sentence)
    except LookupError:
        nltk.download('punkt')
        return nltk.word_tokenize(sentence)

# Rest of your functions remain the same
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag