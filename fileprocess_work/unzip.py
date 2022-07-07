import imp
import os, sys
import gzip
 
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
    'Streptococcus pyogenes'
]
# sys.path.append('../')
from config import Download_Data
gen_name = Download_Data.gen_name1
parent_filedir = Download_Data.parent_path

# 将目标文件夹下的.gz文件解压
def un_gz(file_name):
    
    # 获取文件的名称，去掉后缀名
    f_name = file_name.replace(".gz", "")
    # 开始解压
    g_file = gzip.GzipFile(file_name)
    #读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    open(f_name, "wb+").write(g_file.read())
    g_file.close()
    
# un_gz('D:\\python36\\config.gz')

# parent_filedir = 'K:/dataset/ncbi/pathogens'
for curname in gen_name:
    path = os.path.join(parent_filedir, curname)
    
    list_dir = os.listdir(path)
    list_gz = [line for line in list_dir if line.find('.gz') != -1]
    print(len(list_gz))
    print(list_gz)
    for gz_file in list_gz:
        gz_name = os.path.join(path, gz_file)
        un_gz(gz_name)