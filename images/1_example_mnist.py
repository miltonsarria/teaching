import mnist
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier


#example using mnist


#load data
DATA_PATH='/home/sarria/data/mnist/'
mn = mnist.MNIST(DATA_PATH)
#en caso de tener nombres diferentes para los archivos, modificar las siguientes propiedades antes de cargar
#
# mn.test_img_fname = 't10k-images-idx3-ubyte'
# mn.test_lbl_fname = 't10k-labels-idx1-ubyte'

# mn.train_img_fname = 'train-images-idx3-ubyte'
# mn.train_lbl_fname = 'train-labels-idx1-ubyte'

test_img, test_label = mn.load_testing()
train_img, train_label = mn.load_training()
#comvert to numpy array
train_img     = np.array(train_img)
test_img      = np.array(test_img)
test_label    = np.array(test_label)
train_label   = np.array(train_label)

#create a subset to train using only images with labels 3 and 8
X_train_data  =np.vstack((train_img[train_label==3,:],train_img[train_label==8,:]))
X_train_labels=np.hstack((np.zeros(sum(train_label==3)),np.ones(sum(train_label==8))))

X_test_data  =np.vstack((test_img[test_label==3,:],test_img[test_label==8,:]))
X_test_labels=np.hstack((np.zeros(sum(test_label==3)),np.ones(sum(test_label==8))))

#randomize train data
new_order=np.random.permutation(X_train_labels.size)
X_train_data   = X_train_data[new_order,:]
X_train_labels = X_train_labels[new_order]

#display first 100 images in a 10 x 10 image array
IM=np.zeros(28*10+1)
im=0
for i in np.arange(10):
    aux=np.zeros((28,1))
    for j in np.arange(10):
       aux=np.hstack((aux,X_train_data[im].reshape(28,28)))
       im+=1
    IM=np.vstack((IM,aux))
plt.imshow(IM,cmap="gray")
plt.show()


print(X_train_labels[:100].reshape(10,10))
del IM, aux
  

#train MLP
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)

mlp.fit(X_train_data/255, X_train_labels)


print("Training set score: %f" % mlp.score(X_train_data/255, X_train_labels))
print("Test set score: %f" % mlp.score(X_test_data/255, X_test_labels))

