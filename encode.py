import os, sys
import re
import numpy as np

from collections import OrderedDict
from Bio.Seq import Seq

gen_name = [
        'Bocaparvovirus',
        'Human mastadenovirus A',
        'Severe acute respiratory syndrome coronavirus 2',
        'Rhinovirus',
        'Metapneumovirus',
        'Stenotrophomonas maltophilia',
        'Streptococcus pneumoniae',
        'Staphylococcus aureus',
        'Acinetobacter baumannii',
        #'Mycobacterium tuberculosis'
        'Streptococcus pyogenes'
    ]

NUCLE_DICT = {'A':[1,0,0,0], 'C':[0,1,0,0], 'T':[0,0,1,0], 'G':[0,0,0,1], 'N':[0,0,0,0]}
seq = 'ACCTGAAA'
p_path = 'K:/dataset/ncbi/pathogens'
path = './merge1.fasta'
k_length = 3  # k-mer

from config import Download_Data
p_path = Download_Data.parent_path


# gen_name = [['Pseudomonas aeruginosa', 1000]]
gen_name = Download_Data.gen_name1
config = {
    'gen_name':'Streptococcus pyogenes',
    'p_path' : p_path,
    'k_length' : 100,
    'interval' : 1000
}

path = os.path.join(config['p_path'], config['gen_name'], 'merge1.fasta')

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

def handle_fasta(path):
    S_dict = OrderedDict()
    key = None
    seq = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            # print(line)
            if line.startswith('>'):
                if key is not None:
                    S_dict[key] = handle_seq(seq, config['k_length'])
                key = line.lstrip('>').split()[0]
                seq = ''
            else:
                seq += handle_non_ACTG(line)
        S_dict[key] = handle_seq(seq, config['k_length'])
    return S_dict

#handle_fasta(path)
def handle_FastaToNp(path):
    S_list = []
    seq = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq is not None:
                    S_list.extend(handle_seq(seq, config['k_length']))
                    # ===================reverse_complement=====================
                    seqR = Seq(seq).reverse_complement()
                    S_list.extend(handle_seq(seqR, config['k_length']))
                    # ===============================================
                seq = ''
            else:
                seq += handle_non_ACTG(line)
        S_list.extend(handle_seq(seq, config['k_length']))
        # ================reverse_complement=========================
        seqR = Seq(seq).reverse_complement()
        S_list.extend(handle_seq(seqR, config['k_length']))
        # ================================================
    return np.array(S_list)

def save_numpy(code):
    save_name = config['gen_name'] + '_k' + str(config['k_length']) \
                    + '_i' + str(config['interval'])
    save_path = os.path.join(config['p_path'], 'data/train4', save_name)
    np.save(save_path, code)

# res = handle_FastaToNp(path)
# # res = handle_fasta(path)
# k_num = res.shape[0]
# save_numpy(res)
# print('hello')


# gen_name = ['Haemophilus influenzae']
# for curname, interval in gen_name:
for curname in gen_name:
    config['gen_name'] = curname
    # config['interval'] = interval

    path = os.path.join(config['p_path'], config['gen_name'], 'merge1.fasta')
    # path = os.path.join(config['p_path'], config['gen_name'], 'test/test.fna')

    res = handle_FastaToNp(path)
    # res = handle_fasta(path)
    k_num = res.shape[0]
    save_numpy(res)
    del res

    print('hello')

#np.save(save_path, res)
#print(res.shape)
# print(res)

