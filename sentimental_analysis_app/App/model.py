# deep learning part
import tensorflow as tf
# preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#
#
import numpy as np
import json
import requests
import pickle
import ssl
# get tokens
TOKENIZER_PATH = 'sentimental_analysis/tokenizer.pickle'
tokenizer = pickle.load(open(TOKENIZER_PATH, 'rb'))
# source for maximum padding value (T) : google colab nlp sentiment analysis
T = 117

MODEL_URI = 'http://localhost:8501/v1/models/sentimental_analysis:predict'

def get_prediction(sentence):
    sequence = tokenizer.texts_to_sequences([sentence])
    sentence = pad_sequences(sequence, maxlen = T)
    print(sentence.shape)

    payload = {
    'instances': sentence.tolist()
    }
    data = json.dumps(payload)
    response = requests.post(MODEL_URI, data = data)
    result = json.loads(response.text)
    print(result, type(result))
    return 'Positive' if result['predictions'][0][0]>.5 else 'Negative'
