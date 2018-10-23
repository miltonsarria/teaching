import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.linear_model import LogisticRegression
lista='lista_feats_isolated.txt'
#lista='lista.txt'
hf = open(lista,'r')
lines=hf.readlines()
#load all feats
Y=[]
X=[]
for line in lines:
    hf = h5py.File(line[:-1], "r")
    feats = (hf.get('fbank')).value
    lab=(hf.get('label')).value
    X.append(np.mean(feats,axis=0))
    Y.append(lab)
    hf.close()
    
X=np.array(X)      
Y=np.array(Y)



#calcular media
meanX=X.mean(axis=0)
X=X-meanX
#calcular matriz de covarianzas
Sigma=np.cov(X.transpose())

u, s, vh = np.linalg.svd(Sigma, full_matrices=True)
Xp=np.dot(X,u)
plt.figure(1)
#label={'mesa':1,'casa':2,'pesa':3,'queso':4,'peso':5}
l1,=plt.plot(Xp[Y==1,0],Xp[Y==1,1],'ob',label='Mesa')
l2,=plt.plot(Xp[Y==2,0],Xp[Y==2,1],'or',label='Casa')
l3,=plt.plot(Xp[Y==3,0],Xp[Y==3,1],'og',label='Pesa')
l4,=plt.plot(Xp[Y==4,0],Xp[Y==4,1],'ok',label='Queso')
l5,=plt.plot(Xp[Y==5,0],Xp[Y==5,1],'oy',label='Peso')
plt.legend(handles=[l1,l2,l3,l4,l5])
plt.show()



