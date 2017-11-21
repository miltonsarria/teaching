#Milton Orlando Sarria

import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from six.moves import cPickle as pickle
from tools_dnn import *
####################################################################


#en este programa se extraen todas las imagenes, se organizan de forma adecuada y se
#guardan en archivos separados por clase

num_classes = 10

#archivos .tar que contienen todos los datos
train_filename='/home/sarria/data/notMNIST_large.tar.gz'
test_filename='/home/sarria/data/notMNIST_small.tar.gz'

#tamano esperado
expected_bytes_train=247336696
expected_bytes_test=8458043

#Verificar tamano y extraer archivos
train_folders = maybe_extract(train_filename,expected_bytes_train,num_classes)
test_folders = maybe_extract(test_filename,expected_bytes_test,num_classes)

#cargar todas las imagenes de cada clase y guardar en archivos separados
image_size = 28      # dimensiones de la imagen (image_size x image_size).
pixel_depth = 255.0  # Numero de valores por pixel

#Guardar datos de entrenamiento
min_num_images_per_class=45000
train_datasets = maybe_pickle(train_folders, min_num_images_per_class,image_size,pixel_depth)
#guardar datos de prueba
min_num_images_per_class=1800
test_datasets = maybe_pickle(test_folders, min_num_images_per_class,image_size,pixel_depth)

#Guardar listas de archivos de entrenamiento y prueba
#y tambien seleccionar algunos ejemplos para visualizar
train_files= os.path.splitext(os.path.splitext(train_filename)[0])[0] +'/notMNIST_train.txt'
test_files=os.path.splitext(os.path.splitext(test_filename)[0])[0]+'/notMNIST_test.txt'
tr_fh=open(train_files,'w')
te_fh=open(test_files,'w')

IM=np.zeros(image_size*10+1)
nbr_samples=[]


for root1,root2 in zip(train_datasets,test_datasets):
    tr_fh.write(root1+'\n')
    te_fh.write(root2+'\n')  

    f=open(root1,'rb')    
    xx=pickle.load(f)
    f.close()
    xx_root=np.zeros([image_size,1])    
    indx=np.random.permutation(xx.shape[0])
    nbr_samples.append(xx.shape[0])
    for ii in np.arange(10):
         xx_root=np.hstack((xx_root,xx[indx[ii],:,:]))
    IM=np.vstack((IM,xx_root))
    
tr_fh.close()
te_fh.close()

plt.imshow(IM,cmap="gray")
plt.show()









