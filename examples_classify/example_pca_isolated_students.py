import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.linear_model import LogisticRegression
lista='lista_feats_estudiantes_sil_rem.txt'
#lista='lista_feats_estudiantes.txt'
hf = open(lista,'r')
lines=hf.readlines()
#load all feats
Y=[]
X=[]
for line in lines:
    hf = h5py.File(line[:-1], "r")
    feats = (hf.get('fbank')).value
    lab=(hf.get('label')).value
    if True:#(lab==5) or (lab==6):
        X.append(np.mean(feats,axis=0))
        Y.append(lab)
    hf.close()
    
X=np.array(X)      
Y=np.array(Y)



#calcular media
meanX=X.mean(axis=0)
X=(X-meanX)/X.std(axis=0)
#calcular matriz de covarianzas
Sigma=np.cov(X.transpose())

u, s, vh = np.linalg.svd(Sigma, full_matrices=True)
Xp=np.dot(X,u)
plt.figure(1)
#label={'mesa':1,'pesa':2,'queso':3,'peso':4, 'si':5,'no':6}
l1,=plt.plot(Xp[Y==1,0],Xp[Y==1,1],'ob',label='Mesa')
l2,=plt.plot(Xp[Y==2,0],Xp[Y==2,1],'og',label='Pesa')
l3,=plt.plot(Xp[Y==3,0],Xp[Y==3,1],'ok',label='Queso')
l4,=plt.plot(Xp[Y==4,0],Xp[Y==4,1],'oy',label='Peso')
l5,=plt.plot(Xp[Y==5,0],Xp[Y==5,1],'or',label='Si')
l6,=plt.plot(Xp[Y==6,0],Xp[Y==6,1],'oc',label='No')
plt.legend(handles=[l1,l2,l3,l4,l5,l6])
plt.show()



