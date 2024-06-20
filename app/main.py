import streamlit as st
import string
import gensim
from scipy.linalg import get_blas_funcs
from scipy.linalg.lapack import get_lapack_funcs
from scipy.special import psi 
import numpy as np 
import nltk
from gensim.models import Word2Vec

try:
    from numpy import triu
except ImportError:
   from scipy.linalg import triu


nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')

stop_words = set(stop_words)

EMBEDDING_DIM = 100
WORD2VEC_PATH = "models/word2vec.model"
word2Vec = Word2Vec.load(WORD2VEC_PATH)



def clean_word(word:str) -> str:

    word = word.lower()
    word = word.strip()

    for letter in word:
        if letter in string.punctuation:
            word = word.replace(letter, '')

    return word        



def clean_text(text:str) -> list[str]:

    clean_text_list = []
    for word in text.split():
        cleaned_word = clean_word(word)
        if cleaned_word not in stop_words:
            clean_text_list.append(cleaned_word)

    return clean_text_list



def vectorize_text(text:list[str]) -> np.ndarray:
    """Vectorize a text by averaging all the word vectors in the text

    Args:
       text(str): the text to vectorize

    Returns:
       np.ndarray: the vectorized text
    """

    text_vector = np.zeros(EMBEDDING_DIM, np.float32)
    for word in text:
        word_vector = word2Vec_model.wv[word]
        text_vector += word_vector

    text_vector/= len(text)

    return text_vector



st.title('Fake News Detector')

st.subheader('Detecting fake news with machine learning')

text_to_predict = st.text_area('Enter the news to check if it is fake or not')

text_to_predict_clean = clean_text(text_to_predict)

text_to_predict_vectorized = vectorize_text(text_to_predict_clean)


button = st.button('Analyze')

if button:
    st.text(text_to_predict_clean)
    st.text(text_to_predict_vectorized)
    st.success('The news are real!')
