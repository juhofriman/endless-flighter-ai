#!/usr/bin/env python3

import numpy as np
from PIL import ImageGrab
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import time
from pynput import keyboard
import os

file_name = 'training_data.npy'

train_data = np.load(file_name, allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

shuffle(train_data)

lefts = []
rights = []
forwards = []

for data in train_data:
    img = data[0]
    choice = data[1]

    if(choice == [1, 0]):
        lefts.append([img, [1, 0, 0]])

    if(choice == [0, 1]):
        rights.append([img, [0, 1, 0]])

    if(choice == [0, 0]):
        forwards.append([img, [0, 0, 1]])

forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

final_data = forwards + lefts + rights

shuffle(final_data)

df = pd.DataFrame(final_data)
print(df.head())
print(Counter(df[1].apply(str)))

np.save('training_data-balanced.npy', final_data)

# for data in train_data:
#     img = data[0]
#     choice = data[1]
#     cv2.imshow('test', img)
#     print(choice)
#
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
