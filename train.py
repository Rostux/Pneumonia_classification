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

from preprocessing import x_test, x_val, x_train, y_test, y_train, y_val
from augmentation import datagen
from model import model3


learning_rate_reduction = ReduceLROnPlateau(
    monitor='val_accuracy', patience=2, verbose=1, factor=0.3, min_lr=0.000000000001)


history = model3.fit(datagen.flow(x_train, y_train, batch_size=32), epochs=24,
                     validation_data=datagen.flow(x_val, y_val), callbacks=[learning_rate_reduction])
t1, t2 = model3.evaluate(x_test, y_test, batch_size=32)
print(t1)
print(t2)

#y1=model3.predict(x_test)
y2 = model3.predict_classes(x_test)
y3 = np.zeros((624, 1))
#y4=model4.predict(x_test)
print(classification_report(y_test, y2, target_names=[
      'Pneumonia (Class 0)', 'Normal (Class 1)']))
