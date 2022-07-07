import os, sys
os.chdir(sys.path[0])  # 解决vscode下相对路径的问题
# import numpy as np
from collections import OrderedDict

from tools import *
import numpy as np
import os
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
from keras.initializers import he_normal
from keras import optimizers
from keras.callbacks import LearningRateScheduler, TensorBoard
from keras.layers.normalization import BatchNormalization
# from keras.layers.normalization.batch_normalization_v1 import BatchNormalization
from keras.utils.data_utils import get_file
from keras import backend as K

from config import Config
version = 'v6'

# gen_name = Config.config[version]['gen_name']

gen_name = Config.config_v1[version]['gen_name']
config = {
    'gen_name': 'Streptococcus pyogenes',
    'p_path': 'K:/dataset/ncbi/pathogens',
    'k_length': 100,
    'interval': 10
}

config['k_length'] = Config.config_v1[version]['k-mer']
k_len = config['k_length']

num_classes = Config.config_v1[version]['num_classes']
epochs = 60

batch_size = 512

tr_rate = 0.8
val_rate = 0.2

def load_data():
    idx = 0
    code_list = OrderedDict()
    for curname, interval in gen_name:
        load_name = curname + '_k' + str(config['k_length']) \
                    + '_i' + str(interval) + '.npy'
        load_path = Config.config[version]['data_path']
        load_path = os.path.join(load_path, load_name)
        code = np.load(load_path)

        code = shuf_data(code)
        code_tr = code[:int(code.shape[0] * tr_rate)]
        code_val = code[int(code.shape[0] * tr_rate):]
        if idx == 0:
            # X_all = code
            X_tr = code_tr
            X_val = code_val
            Y_tr = np.repeat(idx, X_tr.shape[0])
            Y_val = np.repeat(idx, X_val.shape[0])
        else:
            X_tr = np.concatenate((X_tr, code_tr))
            X_val = np.concatenate((X_val, code_val))
            Y_tr = np.concatenate((Y_tr, np.repeat(idx, code_tr.shape[0])))
            Y_val = np.concatenate((Y_val, np.repeat(idx, code_val.shape[0])))

        len = code.shape[0]
        # code_list[curname] = code
        idx = idx + 1
        del code
        del code_tr
        del code_val
        print(idx)
    return X_tr, Y_tr, X_val, Y_val
def load_data_v1():
    idx = 0
    interval = Config.config_v1[version]['interval']
    k_length = Config.config_v1[version]['k-mer']
    code_list = OrderedDict()
    for curname in gen_name:
        load_name = curname + '_k' + str(k_length) \
                    + '_i' + str(interval) + '.npy'
        load_path = Config.config_v1[version]['data_path']

        #------------------测试的加载路径--------------------
        # load_name = curname + '_k' + str(100) \
        #                     + '_i' + str(1000) + '.npy'

        # load_path = '/root/dgh_v1/zjj/dataset/pathogens_v1/test'
        #--------------------------------------------------
        
        load_path = os.path.join(load_path, load_name)
        code = np.load(load_path)
        print(code.shape)
        code = shuf_data(code)  # 随机打乱
        code_tr = code[:int(code.shape[0] * tr_rate)]  # 训练
        code_val = code[int(code.shape[0] * tr_rate):]  # 验证
        if idx == 0:
            # X_all = code
            X_tr = code_tr
            X_val = code_val
            Y_tr = np.repeat(idx, X_tr.shape[0])
            Y_val = np.repeat(idx, X_val.shape[0])
        else:
            X_tr = np.concatenate((X_tr, code_tr))
            X_val = np.concatenate((X_val, code_val))
            Y_tr = np.concatenate((Y_tr, np.repeat(idx, code_tr.shape[0])))
            Y_val = np.concatenate((Y_val, np.repeat(idx, code_val.shape[0])))

        len = code.shape[0]
        # code_list[curname] = code
        idx = idx + 1
        del code
        del code_tr
        del code_val
        print(idx)
        print(X_tr.shape)
    return X_tr, Y_tr, X_val, Y_val


X_tr, Y_tr, X_val, Y_val = load_data_v1()

Y_tr = keras.utils.to_categorical(Y_tr, num_classes)
Y_val = keras.utils.to_categorical(Y_val, num_classes)

# shuffle
index = list(range(0, X_tr.shape[0]))
np.random.shuffle(index)
X_tr = X_tr[index]
Y_tr = Y_tr[index]

index = list(range(0, X_val.shape[0]))
np.random.shuffle(index)
X_val = X_val[index]
Y_val = Y_val[index]

import json

with open('./parent_information/parent_v1.json', 'r', encoding='utf-8') as f:
    parent_list = json.load(f)

parent = parent_list[1]

n1 = len(parent_list[0])
n2 = len(parent_list[1])

p_num = len(parent_list[0])
yp_tr = np.zeros((Y_tr.shape[0], p_num)).astype("float32")
yp_val = np.zeros((Y_val.shape[0], p_num)).astype("float32")
for i in range(yp_tr.shape[0]):
    yp_tr[i][parent[str(np.argmax(Y_tr[i]))]] = 1.0
for i in range(yp_val.shape[0]):
    yp_val[i][parent[str(np.argmax(Y_val[i]))]] = 1.0
#------------------------------------------------------------------

print('train', X_tr.shape)
print('valid', X_val.shape)
# ------------------------model---------------------------
from model import *
savepath = './weights/config_v1/'
if not os.path.exists(savepath):
    os.mkdir(savepath)
# ========================================================

# # ===================== model ==================================
alpha = K.variable(value=0.5, dtype="float32", name="alpha")

beta = K.variable(value=0.5, dtype="float32", name="beta")

inputs = Input(shape=(None, 4))  # The input shape doesn’t include the number of samples.

sgd = optimizers.SGD(lr=0.001, momentum=0.9, nesterov=True)

inputs = Input((config['k_length'], 4))
model = get_BranchModel(inputs)
print(model.summary())

# ---------------------- load weights -------------------------------------
#model.load_weights('./weights/config_v1/BranchModel7_v6.hdf5')
# -------------------------------------------------------------------------
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              loss_weights=[alpha, beta],
              metrics=['accuracy'])


modelname = '{0}_epochs{1}_{2}.hdf5'.format(model.name, epochs, version)

savepath = os.path.join(savepath, modelname)
checkpoint = keras.callbacks.ModelCheckpoint(savepath, monitor='val_fc_acc', verbose=1, save_best_only=True, save_weights_only=True, mode='max')
tb_cb = tf.keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=0)

callbacks_list = [checkpoint]

from sklearn.utils import class_weight

y_classes = np.argmax(Y_tr, axis=-1)
class_weights = class_weight.compute_class_weight('balanced', np.unique(y_classes), y_classes)
class_weights = dict(enumerate(class_weights))
history = model.fit(X_tr, [yp_tr, Y_tr],
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              #class_weight=class_weights,
              callbacks=callbacks_list,
              validation_data=(X_val, [yp_val, Y_val]))

score = model.evaluate(X_val, [yp_val, Y_val], verbose=0)

# --------------------------------------------------------------------
# history
import pickle
history_log = './logs/history/config_v1/'
if not os.path.exists(history_log):
    os.mkdir(history_log)
history_save_name = '{0}_epochs{1}_{2}.txt'.format(model.name, epochs, version)

history_save_path = os.path.join(history_log, history_save_name)
with open(history_save_path, 'wb') as file_txt:
    pickle.dump(history.history, file_txt)

# ------------------------------------
print('score is: ', score)