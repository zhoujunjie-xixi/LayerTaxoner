import sys, os
# 从nametotax文件提取taxid
from config import Download_Data
path = Download_Data.parent_path
gen_name = Download_Data.gen_name1

path = 'K:/dataset/ncbi/pathogens_v1'

file_read = os.path.join(path, 'nametotax.txt')  #"K:/dataset/ncbi/pathogens/nametotax.txt"
file_write = os.path.join(path, 'taxid.txt')
# file_write = "K:/dataset/ncbi/pathogens/taxid.txt"

def get_taxid():
    with open(file_write, mode='w') as f_w:
        with open(file_read) as f_r:
            for line in f_r.readlines():
                line_list = line.split('\t')
                f_w.write(line_list[-1])
                print(line_list)
get_taxid()

#gen_name = Download_Data.gene_name1
gen_name = [
        'Streptococcus hemolyticus',
        'Haemophilus influenzae',
        'Streptococcus pneumoniae',
        'Stenotrophomonas maltophilia',
        'Legionella pneumophila',
        'Staphylococcus aureus',
        'Pseudomonas aeruginosa',
        'Klebsiella pneumoniae',
        'Acinetobacter baumannii',
        'Mycobacterium tuberculosis',
        'Streptococcus pyogenes',
        'Mycoplasma pneumoniae',
        'Chlamydia pneumoniae'
    ]

def mkdir():
    for name in gen_name:
        os.mkdir(name)

def output_name():
    output_path = 'K:/dataset/ncbi/pathogens_v1/names.txt'
    with open(output_path, 'w') as f:
        for name in gen_name:
            f.write(name)
            f.write('\n')

# output_name()