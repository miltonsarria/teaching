#Milton Orlando Sarria
#USC
#realizar una primera clasificacion
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from six.moves import cPickle as pickle
from tools_dnn import *
####################################################################

#en este programa se extraen todas las imagenes, se organizan de forma adecuada y se
#guardan en archivos separados por clase

root_path='/home/sarria/data/'
train=root_path+'notMNIST_large/notMNIST_train.txt'
test =root_path+'notMNIST_small/notMNIST_test.txt'

train_datasets=read_sets(train)
test_datasets =read_sets(test)


train_size = 200000
valid_size = 10000
test_size = 10000
image_size = 28  # Altura y ancho en pixeles.
pixel_depth = 255.0  # Numero de niveles por pixel

valid_dataset, valid_labels, train_dataset, train_labels = merge_datasets(
  image_size,train_datasets, train_size, valid_size)
_, _, test_dataset, test_labels = merge_datasets(image_size,test_datasets, test_size)

#imprimir las dimensiones de los nuevos conuntos creados
print('Entrenamiento:', train_dataset.shape, train_labels.shape)
print('Validacion:', valid_dataset.shape, valid_labels.shape)
print('Prueba:', test_dataset.shape, test_labels.shape)

#mezclar los datos de forma aleatoria
train_dataset, train_labels = randomize(train_dataset, train_labels)
test_dataset, test_labels   = randomize(test_dataset, test_labels)
valid_dataset, valid_labels = randomize(valid_dataset, valid_labels)

#verificar que se tienen los datos de forma correcta despues de realizar la mezcla
IM=np.zeros(image_size*10+1)
models = np.unique(train_labels)
idx    = np.arange(train_labels.size)
for mm in models:    
    xx_root=np.zeros([image_size,1])     
    idx_mm = idx[train_labels == mm]    
    for ii in range(10):
         xx_root=np.hstack((xx_root,train_dataset[idx_mm[ii],:,:]))
    IM=np.vstack((IM,xx_root))
plt.imshow(IM,cmap="gray")
plt.show()

#guardar los conjuntos de forma separada

pickle_file = root_path+'notMNIST.pickle'

try:
  f = open(pickle_file, 'wb')
  save = {
    'train_dataset': train_dataset,
    'train_labels': train_labels,
    'valid_dataset': valid_dataset,
    'valid_labels': valid_labels,
    'test_dataset': test_dataset,
    'test_labels': test_labels,
    }
  pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
  f.close()
except Exception as e:
  print('No se puede guardar los datos en el archivo: ', pickle_file, ':', e)
  raise
  
statinfo = os.stat(pickle_file)
print('Archivo en bytes :', statinfo.st_size)  
  

#
models = np.unique(train_labels)
idx_tr    = np.arange(train_labels.size); c_tr = np.zeros(train_labels.size);
idx_va    = np.arange(valid_labels.size); c_va = np.zeros(valid_labels.size);
idx_te    = np.arange(test_labels.size);  c_te = np.zeros(test_labels.size);

for mm in models:   
    im_tr = idx_tr[train_labels == mm]    
    im_va = idx_va[valid_labels == mm]    
    im_te = idx_te[test_labels == mm]
    Xv  = valid_dataset[im_va,:,:]
    Xv  = np.reshape(Xv,(im_va.size,28*28))
    Xt = test_dataset[im_te,:,:]
    Xt = np.reshape(Xt,(im_te.size,28*28))
            
    for lb_tr in im_tr:
        x1 = train_dataset[lb_tr,:,:]
        
        diff  = ((Xv - x1.ravel())**2).sum(axis=1)
        diff = diff == 0
        
        if diff.sum() > 0: 
            c_tr[lb_tr] = c_tr[lb_tr]+1;
            c_va[im_va[diff]] = c_va[im_va[diff]]+1;
            
        
        diff  = ((Xt - x1.ravel())**2).sum(axis=1)
        diff = diff == 0
        if diff.sum() > 0: 
            c_tr[lb_tr] = c_tr[lb_tr]+1;
            c_te[im_te[diff]] = c_te[im_te[diff]]+1;


print([[(c_tr!=0).sum(), (c_va!=0).sum(), (c_te!=0).sum()],[c_tr.size, c_va.size, c_te.size]])


#guardar una version depurada de la base de datos, sin datos repetidos los conjuntos de entrenamiento validacion y prueba
p_pickle_file = root_path+'notMNIST_depurada.pickle'
p_train_dataset = train_dataset[c_tr==0]; p_train_labels = train_labels[c_tr==0];
p_valid_dataset = valid_dataset[c_va==0]; p_valid_labels = valid_labels[c_va==0];
p_test_dataset = test_dataset[c_te==0];   p_test_labels  = test_labels[c_te==0];
try:
  f = open(p_pickle_file, 'wb')
  data = {
    'train_dataset': p_train_dataset,
    'train_labels': p_train_labels,
    'valid_dataset': p_valid_dataset,
    'valid_labels': p_valid_labels,
    'test_dataset': p_test_dataset,
    'test_labels': p_test_labels,
    }
  pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
  f.close()
except Exception as e:
  print('No se puede guardar el archivo: ', p_pickle_file, ':', e)
  raise
  
  
  



