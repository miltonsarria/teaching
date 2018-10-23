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

#crear un clasficador
clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
clf.fit(X,Y)

xx = np.linspace(-5, 15, 100)
yy = np.linspace(-5, 15, 100).T
xx, yy = np.meshgrid(xx, yy)
Xfull = np.c_[xx.ravel(), yy.ravel()]

plt.figure(2)
max_iteration = [2,4,6,8,10,12,14,16,50]
for ii in range(len(max_iteration)):
    clf.max_iter=max_iteration[ii]
    clf.fit(X,Y)
    probas = clf.predict_proba(Xfull)
    plt.subplot(3,3,ii+1)
    imshow_handle = plt.imshow(probas[:, 0].reshape((100, 100)), extent=(-5, 15, -5, 15), origin='lower')
    imshow_handle = plt.imshow(probas[:, 1].reshape((100, 100)),extent=(-5, 15, -5, 15), origin='lower')
    plt.plot(X1t[:,0],X1t[:,1],'ob')
    plt.plot(X2t[:,0],X2t[:,1],'or')
    b=clf.intercept_ 
    c=clf.coef_
    xx = np.linspace(-2, 12, 100)
    yy=(-c[0][0]*xx-b)/c[0][1]
    plt.plot(xx,yy,'k',linewidth=1.5)
    plt.axis([-2,12,-2,12])


plt.show()
