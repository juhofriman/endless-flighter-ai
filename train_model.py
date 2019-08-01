#!/usr/bin/env python3

import numpy as np
from alexnet import alexnet

WIDTH=80
HEIGHT=60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'endless-flighter-{}-{}-{}.model'.format(LR, 'alexnetv2', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('training_data-balanced.npy', allow_pickle=True)

train = train_data[:-300]
test = train_data[-300:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]

test_X = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_Y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS,
    validation_set=({'input': test_X}, {'targets': test_Y}),
    snapshot_step=100, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)
