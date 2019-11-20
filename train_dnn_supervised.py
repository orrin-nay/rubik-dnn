from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import random

from rubik.supervised_model import make_model

print(tf.__version__)

model = make_model()
model.load_weights('./supervised_model1.h5')

# Xs_validate = np.load('train/Xs3.npy')
# Ys_validate = np.load('train/Ys3.npy')
training_sets = [0, 1, 2, 3, 4]
callbacks = [
  # Write TensorBoard logs to `./logs` directory
  tf.keras.callbacks.TensorBoard(log_dir='./logs')
]
# for i in range(2):
#     random.shuffle(training_sets)
#     for train_set in training_sets:
#         Xs = np.load('train/Xs' + str(train_set) + '.npy')
#         Ys = np.load('train/Ys' + str(train_set) + '.npy')
#         model.fit(Xs, Ys, epochs=1, callbacks=callbacks,
#          validation_data=(Xs_validate, Ys_validate),
#          batch_size=100000)
for i in range(4):
    random.shuffle(training_sets)
    for train_set in training_sets:
        print(i)
        Xs = np.load('train/Xs' + str(train_set) + '.npy')
        Ys = np.load('train/Ys' + str(train_set) + '.npy')
        model.fit(Xs, Ys, epochs=1, callbacks=callbacks,
         batch_size=100)
# for i in range(10):
#     random.shuffle(training_sets)
#     for train_set in training_sets:
#         print(i)
#         Xs = np.load('train/Xs' + str(train_set) + '.npy')
#         Ys = np.load('train/Ys' + str(train_set) + '.npy')
#         model.fit(Xs, Ys, epochs=1, callbacks=callbacks,
#          validation_data=(Xs_validate, Ys_validate),
#          batch_size=1)
model.save('supervised_model.h5')