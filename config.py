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
    parent_dir = '/root/dgh_v1/zjj/dataset/pathogens'
    a = 100

class Config:
    config = {
        'parent_path': '/root/dgh_v1/zjj/dataset/pathogens/',
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
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens/data/',
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
            'data_path': '/root/dgh_v1/zjj/dataset/pathogens/data/train1',
            'k-mer': 100
        }
    }

    config_v1 = {
        'parent_path': '/root/dgh_v1/zjj/dataset/pathogens_v1/',
        'v1' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train1',
            'interval':10,
            'k-mer':100,
            'num_classes':12
        },
        'v2' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train1',
            'interval':10,
            'k-mer':100,
            'num_classes':10
        },
        'v3' : {
            'gen_name':[
                'Haemophilus influenzae',
                'Streptococcus pneumoniae',
                'Stenotrophomonas maltophilia',
                'Legionella pneumophila',
                'Staphylococcus aureus',
                'Pseudomonas aeruginosa',
                'Klebsiella pneumoniae',
                'Acinetobacter baumannii',
                'Streptococcus pyogenes',
                'Mycoplasma pneumoniae',
                'Chlamydia pneumoniae'
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train1',
            'interval':10,
            'k-mer':100,
            'num_classes':11
        },
        'v4' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train2',
            'interval':10,
            'k-mer':100,
            'num_classes':12,
            'valid_data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/valid',
            'valid_interval':100,
        },
        'v4_1' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train2',
            'interval':10,
            'k-mer':100,
            'num_classes':12,
            'valid_data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/valid',
            'valid_interval':100,
        },
        # v5：kmer 50
        'v5' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train2',
            'interval':10,
            'k-mer':50,
            'num_classes':12
        },
        'v5_1' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train2',
            'interval':10,
            'k-mer':50,
            'num_classes':12,
            'valid_data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/valid',
            'valid_interval':100,
        },
        'v6' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train3',
            'interval':10,
            'k-mer':100,
            'num_classes':12
        },
         'v6_1' : {
            'gen_name':[
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
            ],
            'data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/data/train3',
            'interval':10,
            'k-mer':100,
            'num_classes':12,
            'valid_data_path':'/root/dgh_v1/zjj/dataset/pathogens_v1/valid',
            'valid_interval':100,
        },
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
    parent_path = '/root/dgh_v1/zjj/dataset/pathogens_v1'