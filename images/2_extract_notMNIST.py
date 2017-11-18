#Milton Orlando Sarria

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from six.moves import cPickle as pickle
from tools_dnn import *
####################################################################


#this script extracts all images  and saves separate files per class containing 3-D arrays per class
num_classes = 10

#tar files containing training and testing data
train_filename='/home/sarria/data/notMNIST_large.tar.gz'
test_filename='/home/sarria/data/notMNIST_small.tar.gz'

#expected size in bytes
expected_bytes_train=247336696
expected_bytes_test=8458043

#check file size and extract images 
train_folders = maybe_extract(train_filename,expected_bytes_train,num_classes)
test_folders = maybe_extract(test_filename,expected_bytes_test,num_classes)

#load data and save it in pickle format
image_size = 28      # Pixel width and height (image_size x image_size).
pixel_depth = 255.0  # Number of levels per pixel.

#save training data
min_num_images_per_class=45000
train_datasets = maybe_pickle(train_folders, min_num_images_per_class,image_size,pixel_depth)
#save testing data
min_num_images_per_class=1800
test_datasets = maybe_pickle(test_folders, min_num_images_per_class,image_size,pixel_depth)

#display some examples of images
IM=np.zeros(image_size*10+1)
nbr_samples=[]
for root in train_datasets:
    f=open(root,'rb')    
    xx=pickle.load(f)
    f.close()
    xx_root=np.zeros([image_size,1])    
    indx=np.random.permutation(xx.shape[0])
    nbr_samples.append(xx.shape[0])
    for ii in np.arange(10):
         xx_root=np.hstack((xx_root,xx[indx[ii],:,:]))
    IM=np.vstack((IM,xx_root))
plt.imshow(IM,cmap="gray")
plt.show()





