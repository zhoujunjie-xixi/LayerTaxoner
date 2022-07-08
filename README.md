# LayerTaxoner
## Description
LayerTaxoner is a novel approach to classify metagenomic data for bacterial respiratory pathogens at a reasonable level based on deep hierarchical networks.
LayerTaxoner achieved better performance and estimated the abundance more precisely than traditional approaches. The advantage lies in our strategy of choosing a high-confident layer of hierarchical network output and constructing a classification tree to make reasonable prediction.

## Dependencies
```
conda create --name dvf python=3.6 numpy theano=1.0.3 keras=2.2.4 scikit-learn Biopython h5py tensorflow=1.15.0
```

```
conda activate dvf
```

## Usage
### Predict
```
python LayerTaxoner.py [-i input_fasta] [-o output_dir] [-w weight]
```

#### Options
```
-h, --help              show this help message and exit
-i input_fa, --in=input_fa  
                        input fasta file
-o output_dir, --out=output_dir
                        output directory
-w weights, --weights=weights
                        model weights
```
### Training
```
python training.py
```

You can configure the training format and content in the config.py
