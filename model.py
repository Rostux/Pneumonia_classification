import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from keras.callbacks import ReduceLROnPlateau
import cv2
import tensorflow as tf


from augmentation import datagen
from preprocessing import x_train


learning_rate_reduction = ReduceLROnPlateau(
    monitor='val_accuracy', patience=2, verbose=1, factor=0.3, min_lr=0.000000000001)


datagen.fit(x_train)


dp = 0.6
model3 = Sequential()
model3.add(Conv2D(32, (3, 3), strides=1, padding='same',
                  activation='relu', input_shape=(150, 150, 1)))
model3.add(MaxPool2D((2, 2), strides=2, padding='same'))
model3.add(Conv2D(64, (3, 3), strides=1, padding='same', activation='relu'))
model3.add(MaxPool2D((2, 2), strides=2, padding='same'))
model3.add(Conv2D(128, (3, 3), strides=1, padding='same', activation='relu'))
model3.add(MaxPool2D((2, 2), strides=2, padding='same'))
model3.add(Conv2D(128, (3, 3), strides=1, padding='same', activation='relu'))
model3.add(MaxPool2D((2, 2), strides=2, padding='same'))
model3.add(Flatten())
model3.add(Dropout(0.2))
model3.add(Dense(units=512, activation='relu'))
model3.add(Dense(units=1, activation='sigmoid'))
model3.compile(optimizer="rmsprop", loss='binary_crossentropy',
               metrics=['accuracy'])
model3.summary()
