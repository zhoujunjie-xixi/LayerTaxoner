import pandas as pd
import numpy as np
import wget

def download(url=0):
    url = "ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz"
    url = 'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/173/775/GCF_002173775.1_ASM217377v1/GCF_002173775.1_ASM217377v1_genomic.fna.gz'
    url = 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/018/587/585/GCF_018587585.1_ASM1858758v1/GCF_018587585.1_ASM1858758v1_genomic.fna.gz'

    #wget.download(url, 'pythonLogo.png')
    path = 'K:/'
    wget.download(url, path)
download()
#df = pd.read_csv('examples/ex1.csv')


