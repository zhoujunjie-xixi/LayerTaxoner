class Record:
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
    parent_dir = 'K:/dataset/ncbi/pathogens'
    a = 100

config = {
    'a'
}

class Config:
    config = {
        'parent_path': 'K:/dataset/ncbi/pathogens/',
        'v1' : {
            'gen_name':
                [['Bocaparvovirus', 10],
                 ['Human mastadenovirus A', 2],
                 ['Severe acute respiratory syndrome coronavirus 2', 2],
                 ['Rhinovirus', 1],
                 ['Metapneumovirus', 2],
                 ['Stenotrophomonas maltophilia', 200],
                 ['Streptococcus pneumoniae', 200],
                 ['Staphylococcus aureus', 200],
                 ['Acinetobacter baumannii', 200],
                 # ['Mycobacterium tuberculosis', 200],
                 ['Streptococcus pyogenes', 200]],
            'data_path':'K:/dataset/ncbi/pathogens/data/',
            'k-mer':200
        },
        'v2': {
            'gen_name':
                [['Bocaparvovirus', 10],
                ['Human mastadenovirus A', 2],
                ['Severe acute respiratory syndrome coronavirus 2', 2],
                ['Rhinovirus', 1],
                ['Metapneumovirus', 2],
                ['Stenotrophomonas maltophilia', 50],
                ['Streptococcus pneumoniae', 50],
                ['Staphylococcus aureus', 50],
                ['Acinetobacter baumannii', 50],
                # ['Mycobacterium tuberculosis', 200],
                ['Streptococcus pyogenes', 50]],
            'data_path': 'K:/dataset/ncbi/pathogens/data/train1',
            'k-mer': 100
        }
    }

class Download_Data:
    gen_name1 = [
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
    parent_path = '/root/zjj/dataset/pathogens_v1'