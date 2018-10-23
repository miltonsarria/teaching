import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.linear_model import LogisticRegression

file1='artificial_data.h5'
file2='artificial_data_test.h5'
########### cargar datos de entrenamiento y datos de prueba
hf = h5py.File(file1, "r")
X1 = np.array(hf.get('X1')); Y1=np.array(hf.get('lab1'));
X2 = np.array(hf.get('X2')); Y2=np.array(hf.get('lab2'));
hf.close()
#datos de entrenamiento
X=np.vstack((X1,X2))
Y=np.append(np.zeros(Y1.size).astype(int),np.ones(Y2.size).astype(int))

hf = h5py.File(file2, "r")
#datos de prueba
X1t = np.array(hf.get('X1')); Y1=np.array(hf.get('lab1'));
X2t = np.array(hf.get('X2')); Y2=np.array(hf.get('lab2'));
hf.close()

#graficar
plt.figure(1)
plt.plot(X1[:,0],X1[:,1],'ob')
plt.plot(X2[:,0],X2[:,1],'or')


#calcular media
meanX=X.mean(axis=0)
X=X-meanX
#calcular matriz de covarianzas
Sigma=np.cov(X.transpose())

u, s, vh = np.linalg.svd(Sigma, full_matrices=True)
Xp=np.dot(X,u)
plt.figure(2)
plt.plot(Xp[Y==0,0],Xp[Y==0,1],'ob')
plt.plot(Xp[Y==1,0],Xp[Y==1,1],'or')
plt.show()



