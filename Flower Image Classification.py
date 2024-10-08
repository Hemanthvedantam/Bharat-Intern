# -*- coding: utf-8 -*-
"""Untitled62.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14BsGmRgicZS1u1-xoCauyxLZDBs76xal
"""

#Flower image classification using iris data with Tensorflow and keras

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#well it is a warning showing in goolge colab while importing the tensorflow data-large amount

iris = load_iris()
X = iris.data
y = iris.target
#this is the sample data we load using iris model

df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = y
df['species'] = df['species'].apply(lambda x: iris.target_names[x])
print(df.head())


sns.pairplot(df, hue='species', markers=["o", "s", "D"])
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#it is the one line of code where we train and test the model to get the prediction

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#scaler model is used to merge and standard the unscaler data that means in formatted data
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()


history = model.fit(X_train, y_train, epochs=50, validation_split=0.2, verbose=2)

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy:.4f}")

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

print(classification_report(y_test, y_pred_classes))


plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


model.save('iris_classification_model.h5')
