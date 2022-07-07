import numpy as np
import keras
import numpy as np
import pickle
import os
from keras.models import Model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, Input
from keras.initializers import he_normal
from keras import optimizers
from keras.callbacks import LearningRateScheduler, TensorBoard
from keras.layers.normalization import BatchNormalization
from keras.utils.data_utils import get_file
from keras import backend as K

def shuf_data(X):
    index = list(range(0, X.shape[0]))
    np.random.shuffle(index)
    X_shuf = X[np.ix_(index, range(X.shape[1]), range(X.shape[2]))]
    return X_shuf

class LossWeightsModifier(keras.callbacks.Callback):
  def __init__(self, alpha, beta):
    self.alpha = alpha
    self.beta = beta
    # self.gamma = gamma
    # customize your behavior
  def on_epoch_end(self, epoch, logs={}):
    if epoch == 100:
      K.set_value(self.alpha, 0.5)
      K.set_value(self.beta, 0.5)
      # K.set_value(self.gamma, 0.1)
    if epoch == 100:
      K.set_value(self.alpha, 0.01)
      K.set_value(self.beta, 0.99)
      # K.set_value(self.gamma, 0.7)
    if epoch == 100:
      K.set_value(self.alpha, 0.5)
      K.set_value(self.beta, 0.5)
      # K.set_value(self.gamma, 0.7)
    if epoch == 1000:
      K.set_value(self.alpha, 0)
      K.set_value(self.beta, 1)
      # K.set_value(self.gamma, 1)

