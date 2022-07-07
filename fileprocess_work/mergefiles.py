import os, sys
os.chdir(sys.path[0])

# 将目标文件夹下的所有.fna文件合并成一个.fasta文件
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
# parent_filedir = 'K:/dataset/ncbi/pathogens'

from config import Download_Data
gen_name = Download_Data.gen_name1
parent_filedir = Download_Data.parent_path


def mergefiles(parent_filedir, curname):
    # parent_filedir = 'K:/dataset/ncbi/pathogens'
    # curname = 'Streptococcus pyogenes'  #选择要处理的文件夹名
    mergefiledir = os.path.join(parent_filedir, curname)
    # 获取当前文件夹中的文件名称列表  
    filenames = os.listdir(mergefiledir)
    filenames = [filename for filename in filenames if filename.endswith('.fna')]
    print(filenames)
    # 获取输出文件的路径
    filename_merge = os.path.join(mergefiledir, 'merge.fasta')
    file_merge=open(filename_merge, 'w')
    # 向文件中写入字符
    # file.write('test\n')
    
    for filename in filenames:  
        filepath=mergefiledir+'\\'+filename

        # print(filename)
        for line in open(filepath):
            #print(line)  
            file_merge.writelines(line)  
        # file_merge.write('\n')  
    file_merge.close()


def mergefiles2(parent_filedir, curname, max_size):
    # parent_filedir = 'K:/dataset/ncbi/pathogens'
    # curname = 'Streptococcus pyogenes'  #选择要处理的文件夹名
    mergefiledir = os.path.join(parent_filedir, curname)
    # 获取当前文件夹中的文件名称列表  
    filenames = os.listdir(mergefiledir)
    filenames = [filename for filename in filenames if filename.endswith('.fna')]
    # print(filenames)
    # 获取输出文件的路径
    filename_merge = os.path.join(mergefiledir, 'merge.fasta')
    file_merge=open(filename_merge, 'w')

    idx = 0
    file_size = 0
    while True:
        file_num = len(filenames)
        filename = filenames[idx]
        
        filepath=mergefiledir+'\\'+filename
        
        file_stats = os.stat(filepath)
        file_size += file_stats.st_size / (1024 * 1024)
        
        if (file_size >= max_size):
            break
        print(filename)
        for line in open(filepath):
            #print(line)  
            file_merge.writelines(line)
        
        idx += 1
        idx %= file_num
    file_merge.close()


# 按最大的文件内容去均衡数据，最终文件大小一样
def mergefiles3(parent_filedir, curname, max_size):
    # parent_filedir = 'K:/dataset/ncbi/pathogens'
    # curname = 'Streptococcus pyogenes'  #选择要处理的文件夹名
    mergefiledir = os.path.join(parent_filedir, curname)
    # 获取当前文件夹中的文件名称列表  
    filenames = os.listdir(mergefiledir)
    filenames = [filename for filename in filenames if filename.endswith('.fna')]
    # print(filenames)
    # 获取输出文件的路径
    filename_merge = os.path.join(mergefiledir, 'merge1.fasta')
    file_merge=open(filename_merge, 'w')

    idx = 0
    file_size = 0
    while True:
        file_num = len(filenames)
        filename = filenames[idx]
        
        filepath=mergefiledir+'/'+filename
        
        file_stats = os.stat(filepath)
        file_size += file_stats.st_size / (1024 * 1024)
        
        if (file_size >= max_size):
            #file_size -= file_stats.st_size / (1024 * 1024)
            for line in open(filepath):
                file_merge.writelines(line)
                file_stats = os.stat(filename_merge)
                if (file_stats.st_size / (1024*1024)) >= max_size:
                    break
            break
        print(filename)
        for line in open(filepath):
            #print(line)  
            file_merge.writelines(line)
        
        idx += 1
        idx %= file_num
    file_merge.close()

def file_size():
    max_size = 0
    for curname in gen_name:
        mergefiledir = os.path.join(parent_filedir, curname)
        filenames = os.listdir(mergefiledir)
        filenames = [filename for filename in filenames if filename.endswith('.fna')]
        file_size = 0
        for filename in filenames:
            filepath=mergefiledir+'/'+filename
            file_stats = os.stat(filepath)
            file_size += file_stats.st_size / (1024 * 1024)
        if file_size >= max_size:
            max_size = file_size
    return max_size

print(file_size())

for curname in gen_name:
    max_size = file_size()
    # mergefiles2(parent_filedir, curname, max_size)
    mergefiles3(parent_filedir, curname, max_size)
