#create artificial data in 2-D
import numpy as np
import matplotlib.pyplot as plt
import h5py


#generar puntos de entrenamiento 
N=[500,500,500,500]
mvalues=np.array([[0.5,0.5],[4,4],[1,3],[4,1]])
std = [0.5,0.4,0.4,0.6]
X1=np.array([])
Y1=np.array([])
#grupo 1 media por debajo de 5
for ii in range(len(N)):
    x= std[ii]*np.random.randn(N[ii],2)+mvalues[ii]
    if ii==0:
      X1= x
    else:
      X1=np.vstack((X1,x))
    y=np.ones(N[ii])*ii; 
    Y1= np.append(Y1,y)
Y1=Y1.astype(int)    

X2=np.array([])
Y2=np.array([])
#grupo 2 media por encima de 5
std = [0.5,0.7,0.6,0.8]
mvalues=np.array([[-4,4.5],[1,2],[4,-4],[4,4]])
mvalues=mvalues+5
for ii in range(len(N)):
    x= std[ii]*np.random.randn(N[ii],2)+mvalues[ii]
    if ii==0:
      X2= x
    else:
      X2=np.vstack((X2,x))
    y=np.ones(N[ii])*ii+len(N); 
    Y2= np.append(Y2,y)
Y2=Y2.astype(int)    

#agrupar en una sola variable todos los valores



hf = h5py.File('artificial_data.h5', "w") #handle file
dset = hf.create_dataset('X1', data=X1)
dset = hf.create_dataset('lab1', data=Y1)
dset = hf.create_dataset('X2', data=X2)
dset = hf.create_dataset('lab2', data=Y2)
hf.close()

#graficar
plt.plot(X1[:,0],X1[:,1],'ob')
plt.plot(X2[:,0],X2[:,1],'or')
plt.show()
