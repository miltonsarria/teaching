#!/usr/bin/python

#Milton Orlando Sarria
#USC 2017


import numpy as np
import h5py
        
path_feats='features/'
files = ['feat1.h5', 'feat2.h5']
DATA = []

###################crear datos####
#forma  simple
array=np.array([2,3,4,5])
hf = h5py.File("features/Archivo.h5", "w")
dset = hf.create_dataset("arr", data=array)
hf.close()

#con patrones de nombres
for f in files:
  with h5py.File(path_feats+f,'w') as hf:
     mu, sigma = 0, 0.1 # Media y desviacion estandard
     X = np.random.normal(mu, sigma, 1000)
     data1 =X.reshape(100,10)
     #guardar datos en formato 1
     dset1 = hf.create_dataset("datos1", data=data1)
     #guardar datos en formato 2
     data2 =X.reshape(500,2)
     dset2 = hf.create_dataset("datos2", data=data2)
     hf.close()
