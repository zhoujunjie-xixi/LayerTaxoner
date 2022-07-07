import numpy as np
import os,sys
os.chdir(sys.path[0])  # 解决vscode下相对路径的问题
import tensorflow as tf
import tensorflow_core.python.keras.callbacks
import keras

from keras.datasets import cifar10
from keras.models import Model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import GlobalMaxPooling1D, MaxPooling1D, GlobalAveragePooling1D, AveragePooling1D
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Input
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import Dense, LSTM, Bidirectional, GRU
from keras.initializers import he_normal
from keras import optimizers
from keras.callbacks import LearningRateScheduler, TensorBoard
from keras.layers.normalization import BatchNormalization
# from keras.layers.normalization.batch_normalization_v1 import BatchNormalization
from keras.utils.data_utils import get_file
from keras import backend as K

from keras.layers.recurrent import LSTM,GRU,RNN

n_filter1 = 150
n_filter2 = 100

filter1_size = 30
filter2_size = 10

import json
os.chdir(sys.path[0])

with open('./parent_information/parent_v1.json', 'r', encoding='utf-8') as f:
    parent_list = json.load(f)

p_num = len(parent_list[0])
num_classes = len(parent_list[1])

inputs = Input(shape=(None, 4))

def get_BaseModel():
    x = Conv1D(filters=64, kernel_size=10, activation='relu')(inputs)
    x = BatchNormalization()(x)

    x = Conv1D(filters=128, kernel_size=10, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Conv1D(filters=256, kernel_size=10, activation='relu')(x)
    x = BatchNormalization()(x)

    x = Conv1D(filters=512, kernel_size=10, activation='relu')(x)
    x = BatchNormalization()(x)
    x = GlobalMaxPooling1D()(x)

    x = Dense(1024, activation='relu', name='f1')(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, activation='relu', name='f2')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    fine_pred = Dense(num_classes, activation='softmax', name='fc')(x)

    model = Model(input=inputs, output=[fine_pred], name='medium_dynamic')
    model.name = 'BasehModel'
    return model

def get_BranchModel(inputs):  # 给k-mer=100
    # 训练次数结尾带1，代表去了最后两个Conv1D层

    # -------block----------
    #inputs = Input(shape=(None, 4))
    x = Conv1D(filters=64, kernel_size=10, activation='relu')(inputs)
    x = BatchNormalization()(x)

    x = Conv1D(filters=128, kernel_size=10, activation='relu')(x)
    x = BatchNormalization()(x)

    # -------coarse branch-----------
    c2_bch = Conv1D(filters=256, kernel_size=10, activation='relu')(x)
    c2_bch = BatchNormalization()(c2_bch)
    #c2_bch = MaxPooling1D(2, 2)(c2_bch)
    c2_bch = GlobalMaxPooling1D()(c2_bch)
    #c2_bch = Flatten(name='c2_flatten')(c2_bch)
    c2_bch = Dense(512, activation='relu', name='c2_f1')(c2_bch)
    c2_bch = Dropout(0.5)(c2_bch)
    c2_bch = Dense(512, activation='relu', name='c2_f2')(c2_bch)
    c2_bch = Dropout(0.5)(c2_bch)
    c2_pred = Dense(p_num, activation='softmax', name='c2_f3')(c2_bch)

    # -------block---------------------
    x = Conv1D(filters=256, kernel_size=10, activation='relu')(x)
    x = BatchNormalization()(x)

    # -----fine branch-----------------
    x = Conv1D(filters=512, kernel_size=10, activation='relu')(x)
    x = BatchNormalization()(x)
    x = GlobalMaxPooling1D()(x)

    x = Dense(1024, activation='relu', name='f1')(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, activation='relu', name='f2')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    fine_pred = Dense(num_classes, activation='softmax', name='fc')(x)

    model = Model(input=inputs, output=[c2_pred, fine_pred], name='medium_dynamic')
    model.name = 'BranchModel'
    return model