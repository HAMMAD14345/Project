# -*- coding: utf-8 -*-
"""CNN_test2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-cFOpVeZ-qWQvhSb5xN-pGl6-vbpmRu-

Its a **WORKING CODE** and uses model3 with max length 100
"""

from google.colab import drive
drive.mount('/content/drive')

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Embedding, Conv1D, GlobalMaxPooling1D, Dense
from tensorflow.keras.models import Model

# Set the maximum length of the input sequences to a higher value
max_len = 100

from tensorflow.keras.models import load_model

# Load the saved model
model = load_model('/content/drive/MyDrive/CNN/CNN_model3.h5')

# Define the input text
input_text = input("Enter your value: ")
# Tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([input_text])
sequences = tokenizer.texts_to_sequences([input_text])

# Pad the sequence
max_leng = 100
padded_sequence = pad_sequences(sequences, maxlen=max_leng, padding='post')
# Predict the class probabilities
class_probabilities = model.predict(padded_sequence)[0][0]

# Calculate the percentage of negative phrases in the input text
percentage = class_probabilities * 100
print(f"The percentage of negative phrases in the input text is {percentage:.2f}%")