# -*- coding: utf-8 -*-
"""CNN_train2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kzSPd5sQ6bbuXI2zYsnFuCHtzgRiaBXm
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/drive/MyDrive/CNN/CNN_d1_prepro.csv")

print(df.head(5))

!pip install tensorflow numpy pandas

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout

# Split the data into training, validation, and test sets
from sklearn.model_selection import train_test_split

# Split the dataset into training, validation, and test sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
train_df, val_df = train_test_split(train_df, test_size=0.2, random_state=42)



# Set the maximum length of the input sequences
max_len = max([len(text.split()) for text in df['policy_text']])

# Tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_df['policy_text'])
train_sequences = tokenizer.texts_to_sequences(train_df['policy_text'])
val_sequences = tokenizer.texts_to_sequences(val_df['policy_text'])
test_sequences = tokenizer.texts_to_sequences(test_df['policy_text'])

# Pad the sequences to have a uniform length
train_padded_sequences = pad_sequences(train_sequences, maxlen=max_len, padding='post')
val_padded_sequences = pad_sequences(val_sequences, maxlen=max_len, padding='post')
test_padded_sequences = pad_sequences(test_sequences, maxlen=max_len, padding='post')

from tensorflow.keras.layers import Input


# Create the input layer
inputs = Input(shape=(max_len,))

# Add an embedding layer
embedding_dim = 50
embeddings = Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=embedding_dim)(inputs)

# Add convolutional layers
num_filters = 64
kernel_sizes = [3, 4, 5]
conv_layers = []
for kernel_size in kernel_sizes:
    conv_layer = Conv1D(filters=num_filters, kernel_size=kernel_size, activation='relu')(embeddings)
    pool_layer = GlobalMaxPooling1D()(conv_layer)
    conv_layers.append(pool_layer)

# Concatenate the outputs of the convolutional layers
concatenated = tf.keras.layers.concatenate(conv_layers, axis=1)

# Add a fully connected layer
hidden_dim = 128
dense_layer = Dense(units=hidden_dim, activation='relu')(concatenated)

# Add the output layer
num_classes = 1
output_layer = Dense(units=num_classes, activation='sigmoid')(dense_layer)

# Create the model
from tensorflow.keras.models import Model


model = Model(inputs=inputs, outputs=output_layer)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_padded_sequences, train_df['positive'], validation_data=(val_padded_sequences, val_df['positive']), epochs=10, batch_size=32)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(test_padded_sequences, test_df['positive'])
print('Test accuracy:', test_acc)

# Save the model
model.save('CNN_model2.h5')

# Download the saved model to your system
from google.colab import files
files.download('CNN_model2.h5')

"""the above code is ** WORKING **"""



