import os, sys
import re
from tkinter.filedialog import SaveAs
import numpy as np
os.chdir(sys.path[0])

from collections import OrderedDict

# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # cpu

from tools import *
import numpy as np
import os
import tensorflow as tf
import tensorflow_core.python.keras.callbacks
import keras
from keras.layers import Conv2D, MaxPooling2D, Input
from keras import optimizers

from keras import backend as K
from model import *
import itertools
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn.metrics import *


import optparse

prog_base = os.path.split(sys.argv[0])[1]
parser = optparse.OptionParser()
parser.add_option("-i", "--in", action = "store", type = "string", dest = "input_fa", 
                  help = "input fasta file")
parser.add_option("-o", "--out", action = "store", type = "string", dest = "output_dir",
				  default='./results', help = "output directory")
parser.add_option("-w", "--weights", action = "store", type = "string", dest = "weights",
				  default='./weights/config_v1/BranchModel7_v6.hdf5', help = "model weights")

input_fa = '/root/dgh_v1/zjj/test_data/pathogens/abundance/data/abundance.fa'

options, args = parser.parse_args()
if options.input_fa is None:
    sys.stderr.write(prog_base + ": ERROR: missing required command-line argument")
	# filelog.write(prog_base + ": ERROR: missing required command-line argument")
    parser.print_help()
    sys.exit(0)

input_fa = options.input_fa
output_dir = options.output_dir
weights = options.weights

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

config = {
    'gen_name':'Streptococcus pyogenes',
    'k_length' : 100,
    'interval' : 1
}

with open('./parent_information/parent_v1.json', 'r', encoding='utf-8') as f:
    parent_list = json.load(f)
parent = parent_list[1]

NUCLE_DICT = {'A':[1,0,0,0], 'a':[1,0,0,0],  'C':[0,1,0,0], 'c':[0,1,0,0], 'T':[0,0,1,0], 't':[0,0,1,0], 'G':[0,0,0,1], 'g':[0,0,0,1], 'N':[0,0,0,0]}

def encode(seq):
    #encode = np.zeros((len(seq), 4))
    encode = [NUCLE_DICT[s] for s in seq]
    # print(encode)
    return encode

# encode(seq)
def handle_non_ACTG(sequence):
    ret = re.sub('[^ATCGatcg]', 'N', sequence)
    return ret

def handle_seq(seq, k_length):
    # 将序列处理成 k-mer 形式
    assert len(seq) > k_length
    seq_list = []
    for start_idx in range(0, len(seq)-k_length+1, config['interval']):
        fragment = seq[start_idx:(start_idx+k_length)]
        if len(fragment) < k_length:
            pass
        seq_list.append(fragment.upper())
    seq_list.append(seq[-k_length:])

    ret = []
    for seq in seq_list:
        ret.append(encode(seq))
    return ret

def handle_FastaToNp(path):
    S_list = []
    seq = None
    with open(path) as f:
        for line in f:
            line = line.strip() 
            # print(line)
            if line.startswith('>'):
                if seq is not None:
                    S_list.extend(handle_seq(seq, config['k_length']))
                seq = ''
            else:
                seq += handle_non_ACTG(line)
        S_list.extend(handle_seq(seq, config['k_length']))
    return np.array(S_list)


sgd = optimizers.SGD(lr=0.001, momentum=0.9, nesterov=True)

alpha = K.variable(value=0.99, dtype="float32", name="alpha")
beta = K.variable(value=0.01, dtype="float32", name="beta")
inputs = Input(shape=(None, 4))  # The input shape doesn’t include the number of samples.

inputs = Input((config['k_length'], 4))

model = get_BranchModel(inputs)
print(model.summary())
# model.load_weights('./weights/config_v1/BranchModel7_v6.hdf5')
model.load_weights(weights)

model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              loss_weights=[alpha, beta],
              metrics=['accuracy'])

def predict(model, x):
    y = model.predict(x)
    if not isinstance(y, list):
        y = [y]
    # print(y)
    return y

# filter
def Filter(Y, threshold=0.9):
    level_num = len(Y)
    y_filter = []
    for i in range(len(Y[level_num - 1])):
        cur_level = level_num - 1
        while(cur_level >= 0):
            yy = Y[cur_level][i]
            idx = np.argmax(yy)
            if yy[idx] >= threshold:
                y_filter.append(idx)
            else:
                y_filter.append(-1)
            cur_level -= 1
    return y_filter
def Traverse_Level1(Y, cur_level, i, threshold, level_list):
    if cur_level < 0:
        return
    m = Y[cur_level][i]
    id = str(np.argmax(m))
    if m[int(id)] >= threshold[cur_level]:
        if id not in level_list[cur_level].keys():
            level_list[cur_level][id] = {}
            level_list[cur_level][id]['num'] = 0
            level_list[cur_level][id]['is_leaf'] = True
        level_list[cur_level][id]['num'] += 1
    else:
        Traverse_Level1(Y, cur_level-1, i, threshold, level_list)

def Find_Node(Y, threshold=[0.99, 0.999]):
    level_num = len(Y)
    level_list = [{} for i in range(level_num)]
    if not isinstance(Y, list):
        Y = [Y]
    level_num = len(Y)
    cur_level = level_num - 1
    total = len(Y[cur_level])
    for i in range(total):
        Traverse_Level1(Y, cur_level, i, threshold, level_list)
    return level_list

def test_score(ypred):
    y_class = np.argmax(ypred, axis=-1)
    return y_class

def test_score1(ypred, threshold):
    y_max = np.max(ypred, axis=-1)
    y1_idx = np.where(y_max >= threshold)
    y1_result = np.argmax(ypred, axis=-1)[y1_idx]
    return y1_result

def get_path_res(level_list, y):
    res = []
    level_num = len(y)

    for cur_level in range(level_num - 1, -1, -1):
        for key in level_list[cur_level].keys():
            if level_list[cur_level][key]['is_leaf'] == True:
                level_list[cur_level][key]['is_leaf'] = False
                id = str(key)
                res_dict = {}
                res_dict['level'] = cur_level
                res_dict['id'] = id

                path_weight = level_list[cur_level][key]['num']
                new_level = cur_level - 1
                while (new_level >= 0):
                    id = str(parent_list[new_level + 1][id])
                    if id not in level_list[new_level].keys():
                        path_weight += 0
                    else:
                        level_list[new_level][id]['is_leaf'] = False
                        path_weight += level_list[new_level][id]['num']
                    new_level -= 1
                res_dict['weights'] = path_weight
                res.append(res_dict)
    return res

def final_result(res):
    max_weight = 0
    for i in range(len(res)):
        if res[i]['weights'] > max_weight:
            res_idx = i
            max_weight = res[i]['weights']
    return res_idx

def evaluate_test(test_path, t1):
    result_dict={}
    for i in range(12):
        result_dict[str(i)] = 0

    with open(test_path) as f:
        lines = f.readlines()
        species_num = 0
        line_idx = 0
        non_detected_num = 0
        totoal_line = 10000
        for line in lines[:100]:
            line = line.strip()
            if line.startswith('>'):
                species_num+=1
                continue
            if len(line) < config['k_length']:
                continue
            kmer_res = np.array(handle_seq(line, config['k_length']))
            ypred = predict(model, kmer_res)

            level_list = Find_Node(ypred, threshold=[0.9, t1])
            # ==============================================================
            res = get_path_res(level_list, ypred)
            if len(res) == 0:
                non_detected_num += 1    
            else:
                res_idx = final_result(res)
                if res[res_idx]['level'] == 1:
                    result_dict[res[res_idx]['id']] += 1
    return result_dict, species_num

# t1 阈值
t1 = 0.9

input_fa = '/root/dgh_v1/zjj/test_data/pathogens/abundance/data/abundance.fa'
dic, species = evaluate_test(input_fa, t1)

print('dic: ')
print(dic)

names='Haemophilus_influenzae Streptococcus_pneumoniae Stenotrophomonas_maltophilia Legionella_pneumophila Staphylococcus_aureus Pseudomonas_aeruginosa Klebsiella_pneumoniae Acinetobacter_baumannii Mycobacterium_tuberculosis Streptococcus_pyogenes Mycoplasma_pneumoniae Chlamydia_pneumoniae'
name_list=names.split()

savename=os.path.join(output_dir, 'profile.txt')
with open(savename, 'w') as f:
    for key, value in dic.items():
        f.write(name_list[int(key)])
        f.write('\t')
        f.write(str(value))
        f.write('\n')



# savepath='./results/'
# if not os.path.exists(savepath):
#     os.mkdir(savepath)
# import json
# with open(savepath+'res_list.json', mode='w', encoding='utf-8') as f:
#     json.dump(res_list, f)
# with open(savepath+'spe_list.json', mode='w', encoding='utf-8') as f:
#     json.dump(spe_list, f)
