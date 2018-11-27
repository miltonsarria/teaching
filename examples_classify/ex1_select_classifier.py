import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn import svm


file1='artificial_data.h5'
########### cargar datos de entrenamiento y datos de prueba###########
hf = h5py.File(file1, "r")
X1 = np.array(hf.get('X1')); Y1=np.array(hf.get('lab1'));
X2 = np.array(hf.get('X2')); Y2=np.array(hf.get('lab2'));
hf.close()
#datos consolidados en una sola variable
X=np.vstack((X1,X2))
#Y=np.append(np.zeros(Y1.size).astype(int),np.ones(Y2.size).astype(int))
Y=np.hstack((Y1,Y2))

XX=[]
YY=[]
labels = np.unique(Y)
count=0

target_train=[]
target_test =[]


for ii in labels:
     N=np.sum(Y==ii)
     indx  = np.random.permutation(N)
     train = int(0.8*N)     
     indx=indx+count
     XX.append(X[indx[:train],:])
     YY.append(X[indx[train:],:])
     
     target_train.append(Y[indx[:train]])
     target_test.append(Y[indx[train:]])
     count=count+N
     
##################################################################
# datos separados por conjuntos

XX=np.vstack(XX)
YY=np.vstack(YY)

target_train=np.hstack(target_train)
target_test=np.hstack(target_test)
#generar clasificador
clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
clf.fit(XX, target_train) 

#evaluar
prediction=clf.predict(YY)
result=np.sum(prediction==target_test)/float(target_test.size)

print(result)




