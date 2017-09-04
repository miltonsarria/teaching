#!/usr/bin/python

#Milton Orlando Sarria
#USC 2017


import numpy as np
import h5py
        
path_feats='features/'
files = ['feat1.h5', 'feat2.h5']
DATA = []

###################leer datos####
#forma  simple
hf = h5py.File("features/Archivo.h5", "r")
array = hf.get('arr')
hf.close()

DATA = []
for f in files:
  with h5py.File(path_feats+f,'r') as hf:
    print 'List of arrays in this file: \n', hf.keys()
    campos=hf.keys()    
    data = hf.get(campos[0])
    np_data = np.array(data)
    DATA.append(np_data)
    hf.close()
    
