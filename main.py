#!/usr/bin/env python3

import numpy as np
from PIL import ImageGrab
import cv2
import time
from pynput import keyboard
import keypress
import os

last_time = time.time()

file_name = 'training_data.npy'

if(os.path.isfile(file_name)):
    print('File exists')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exists')
    training_data = []


while(True):
    screen = np.array(ImageGrab.grab(bbox=(20,220, 420, 450)))

    last_time = time.time()
    print('Frame took {} seconds'.format(time.time() - last_time))
    # cv2.imshow('window', cv2.resize(cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY), (80, 60)))
    screen = cv2.resize(cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY), (80, 60))
    keys = keypress.kb_state()
    training_data.append([screen, keys])

    if len(training_data) % 100 == 0:
        print(len(training_data))
        np.save(file_name, training_data)

    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break
