#!/usr/bin/env python3

import numpy as np
from PIL import ImageGrab
import cv2
import time
from pynput import keyboard
import keypress
import os
from alexnet import alexnet
from pynput.keyboard import Key, Controller

keyboard = Controller()

WIDTH=80
HEIGHT=60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'endless-flighter-{}-{}-{}.model'.format(LR, 'alexnetv2', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

while(True):
    screen = np.array(ImageGrab.grab(bbox=(20,220, 420, 450)))

    last_time = time.time()
    print('Frame took {} seconds'.format(time.time() - last_time))
    # cv2.imshow('window', cv2.resize(cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY), (80, 60)))
    screen = cv2.resize(cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY), (80, 60))

    prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
    moves = list(np.around(prediction))
    print(moves, prediction)

    if moves == [1.0, 0, 0]:
        keyboard.press('a')
        keyboard.release('s')
    elif moves == [0, 1.0, 0]:
        keyboard.press('s')
        keyboard.release('a')
    elif moves == [0, 0, 1.0]:
        keyboard.release('a')
        keyboard.release('s')
