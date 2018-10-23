#Milton Orlando Sarria
#USC 2018
import numpy as np
import h5py
        
path_feats='datos/'
files = ['datos1.h5', 'datos2.h5', 'datos3.h5','datos4.h5']


###################crear datos####
#forma  simple

for archivo in files:
    array=np.random.rand(100,13)
    
    hf = h5py.File(path_feats+archivo, "w") #handle file
    dset = hf.create_dataset('mfcc', data=array)
    hf.close()

del array, hf, dset
###################leer datos####
#forma  simple leer solo el primer archivo
hf = h5py.File(path_feats+files[1], "r")
array = np.array(hf.get('mfcc'))
print(array)
print(array.shape)



hf.close()
