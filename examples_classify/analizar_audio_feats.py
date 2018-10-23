#Milton Orlando Sarria
#calcular log fbank feats

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
import h5py

lista='lista_feats_si_no.txt'
hf = open(lista,'r')
lines=hf.readlines()
#load all feats
Y=[]
X=[]
for line in lines:
    hf = h5py.File(line[:-1], "r")
    feats = (hf.get('fbank')).value
    X.append(np.mean(feats,axis=0))
    lab=(hf.get('label')).value
    Y.append(lab)
    hf.close()
    
X=np.array(X)      
Y=np.array(Y)

pca = PCA(n_components=2)
pca.fit(X)

Xp=pca.transform(X)

plt.plot(Xp[Y==0,0],Xp[Y==0,1],'ob'); 
plt.plot(Xp[Y==1,0],Xp[Y==1,1],'or'); 
plt.show()

