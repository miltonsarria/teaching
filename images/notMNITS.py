# These are all the modules we'll be using later. Make sure you can import them
# before proceeding further.
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

# Config the matplotlib backend as plotting inline in IPython
%matplotlib inline
#####################################################
url = 'http://commondatastorage.googleapis.com/books1000/'
last_percent_reported = None

def download_progress_hook(count, blockSize, totalSize):
  """A hook to report the progress of a download. This is mostly intended for users with
  slow internet connections. Reports every 1% change in download progress.
  """
  global last_percent_reported
  percent = int(count * blockSize * 100 / totalSize)

  if last_percent_reported != percent:
    if percent % 5 == 0:
      sys.stdout.write("%s%%" % percent)
      sys.stdout.flush()
    else:
      sys.stdout.write(".")
      sys.stdout.flush()
      
    last_percent_reported = percent
        
def maybe_download(filename, expected_bytes, force=False):
  """Download a file if not present, and make sure it's the right size."""
  if force or not os.path.exists(filename):
    print('Attempting to download:', filename) 
    filename, _ = urlretrieve(url + filename, filename, reporthook=download_progress_hook)
    print('\nDownload Complete!')
  statinfo = os.stat(filename)
  if statinfo.st_size == expected_bytes:
    print('Found and verified', filename)
  else:
    raise Exception(
      'Failed to verify ' + filename + '. Can you get to it with a browser?')
  return filename

#######################################################
for root in train_folders:
    list_im=sorted(os.listdir(root))
    indx=np.random.permutation(len(list_im))
    im=root+'/'+list_im[indx[0]]
    display(Image(filename=im))
  
####################################################### 
image_size = 28  # Pixel width and height.
pixel_depth = 255.0  # Number of levels per pixel.

def load_letter(folder, min_num_images):
  """Load the data for a single letter label."""
  image_files = os.listdir(folder)
  dataset = np.ndarray(shape=(len(image_files), image_size, image_size),
                         dtype=np.float32)
  print(folder)
  num_images = 0
  for image in image_files:
    image_file = os.path.join(folder, image)
    try:
      image_data = (ndimage.imread(image_file).astype(float) - 
                    pixel_depth / 2) / pixel_depth
      if image_data.shape != (image_size, image_size):
        raise Exception('Unexpected image shape: %s' % str(image_data.shape))
      dataset[num_images, :, :] = image_data
      num_images = num_images + 1
    except IOError as e:
      print('Could not read:', image_file, ':', e, '- it\'s ok, skipping.')
    
  dataset = dataset[0:num_images, :, :]
  if num_images < min_num_images:
    raise Exception('Many fewer images than expected: %d < %d' %
                    (num_images, min_num_images))
    
  print('Full dataset tensor:', dataset.shape)
  print('Mean:', np.mean(dataset))
  print('Standard deviation:', np.std(dataset))
  return dataset
        
def maybe_pickle(data_folders, min_num_images_per_class, force=False):
  dataset_names = []
  for folder in data_folders:
    set_filename = folder + '.pickle'
    dataset_names.append(set_filename)
    if os.path.exists(set_filename) and not force:
      # You may override by setting force=True.
      print('%s already present - Skipping pickling.' % set_filename)
    else:
      print('Pickling %s.' % set_filename)
      dataset = load_letter(folder, min_num_images_per_class)
      try:
        with open(set_filename, 'wb') as f:
          pickle.dump(dataset, f, pickle.HIGHEST_PROTOCOL)
      except Exception as e:
        print('Unable to save data to', set_filename, ':', e)
  
  return dataset_names

train_datasets = maybe_pickle(train_folders, 45000)
test_datasets = maybe_pickle(test_folders, 1800)  




def make_arrays(nb_rows, img_size):
  if nb_rows:
    dataset = np.ndarray((nb_rows, img_size, img_size), dtype=np.float32)
    labels = np.ndarray(nb_rows, dtype=np.int32)
  else:
    dataset, labels = None, None
  return dataset, labels

def merge_datasets(pickle_files, train_size, valid_size=0):
  num_classes = len(pickle_files)
  valid_dataset, valid_labels = make_arrays(valid_size, image_size)
  train_dataset, train_labels = make_arrays(train_size, image_size)
  vsize_per_class = valid_size // num_classes
  tsize_per_class = train_size // num_classes
    
  start_v, start_t = 0, 0
  end_v, end_t = vsize_per_class, tsize_per_class
  end_l = vsize_per_class+tsize_per_class
  for label, pickle_file in enumerate(pickle_files):       
    try:
      with open(pickle_file, 'rb') as f:
        letter_set = pickle.load(f)
        # let's shuffle the letters to have random validation and training set
        np.random.shuffle(letter_set)
        if valid_dataset is not None:
          valid_letter = letter_set[:vsize_per_class, :, :]
          valid_dataset[start_v:end_v, :, :] = valid_letter
          valid_labels[start_v:end_v] = label
          start_v += vsize_per_class
          end_v += vsize_per_class
                    
        train_letter = letter_set[vsize_per_class:end_l, :, :]
        train_dataset[start_t:end_t, :, :] = train_letter
        train_labels[start_t:end_t] = label
        start_t += tsize_per_class
        end_t += tsize_per_class
    except Exception as e:
      print('Unable to process data from', pickle_file, ':', e)
      raise
    
  return valid_dataset, valid_labels, train_dataset, train_labels
            
            
train_size = 200000
valid_size = 10000
test_size = 10000

valid_dataset, valid_labels, train_dataset, train_labels = merge_datasets(
  train_datasets, train_size, valid_size)
_, _, test_dataset, test_labels = merge_datasets(test_datasets, test_size)

print('Training:', train_dataset.shape, train_labels.shape)
print('Validation:', valid_dataset.shape, valid_labels.shape)
print('Testing:', test_dataset.shape, test_labels.shape)

########################################################
def randomize(dataset, labels):
  permutation = np.random.permutation(labels.shape[0])
  shuffled_dataset = dataset[permutation,:,:]
  shuffled_labels = labels[permutation]
  return shuffled_dataset, shuffled_labels
train_dataset, train_labels = randomize(train_dataset, train_labels)
test_dataset, test_labels = randomize(test_dataset, test_labels)
valid_dataset, valid_labels = randomize(valid_dataset, valid_labels)

IM=np.zeros([2,282])
models = np.unique(train_labels)
idx    = np.arange(train_labels.size)
for mm in models:    
    xx_root=np.zeros([28,2])     
    idx_mm = idx[train_labels == mm]    
    for ii in range(10):
         xx_root=np.hstack((xx_root,train_dataset[idx_mm[ii],:,:]))
    IM=np.vstack((IM,xx_root))
plt.imshow(IM,cmap="gray")
plt.show()

##########################################

pickle_file = 'notMNIST.pickle'

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
  print('Unable to save data to', pickle_file, ':', e)
  raise
  
statinfo = os.stat(pickle_file)
print('Compressed pickle size:', statinfo.st_size)
###############################################3  
#prune data, delete repeated samples in training, test and validation sets
models = np.unique(train_labels)
idx_tr    = np.arange(train_labels.size); c_tr = np.zeros(train_labels.size);
idx_va    = np.arange(valid_labels.size); c_va = np.zeros(valid_labels.size);
idx_te    = np.arange(test_labels.size);  c_te = np.zeros(test_labels.size);

for mm in models:   
    im_tr = idx_tr[train_labels == mm]    
    im_va = idx_va[valid_labels == mm]    
    im_te = idx_te[test_labels == mm]
    for lb_tr in im_tr:
        x1 = train_dataset[lb_tr,:,:]
        X  = valid_dataset[im_va,:,:]
        X = np.reshape(X,(im_va.size,28*28))
        diff  = ((X - x1.ravel())**2).sum(axis=1)
        diff = diff == 0
        
        if diff.sum() > 0: 
            c_tr[lb_tr] = c_tr[lb_tr]+1;
            c_va[im_va[diff]] = c_va[im_va[diff]]+1;
            
        X = test_dataset[im_te,:,:]
        X = np.reshape(X,(im_te.size,28*28))
        diff  = ((X - x1.ravel())**2).sum(axis=1)
        diff = diff == 0
        if diff.sum() > 0: 
            c_tr[lb_tr] = c_tr[lb_tr]+1;
            c_te[im_te[diff]] = c_te[im_te[diff]]+1;

[[(c_tr!=0).sum(), (c_va!=0).sum(), (c_te!=0).sum()],[c_tr.size, c_va.size, c_te.size]]
p_pickle_file = 'notMNIST_pruned.pickle'
p_train_dataset = train_dataset[c_tr==0]; p_train_labels = train_labels[c_tr==0];
p_valid_dataset = valid_dataset[c_va==0]; p_valid_labels = valid_labels[c_va==0];
p_test_dataset = test_dataset[c_te==0];   p_test_labels  = test_labels[c_te==0];
try:
  f = open(p_pickle_file, 'wb')
  save = {
    'train_dataset': p_train_dataset,
    'train_labels': p_train_labels,
    'valid_dataset': p_valid_dataset,
    'valid_labels': p_valid_labels,
    'test_dataset': p_test_dataset,
    'test_labels': p_test_labels,
    }
  pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
  f.close()
except Exception as e:
  print('Unable to save data to', p_pickle_file, ':', e)
  raise
  
del  p_train_dataset, p_train_labels, p_valid_dataset, p_valid_labels, p_test_dataset, p_test_labels
############################################################3  
from sklearn import linear_model, datasets

def split_train(train_dataset,train_labels,nsc):
    models = np.unique(train_labels)
    small_train  = []
    small_labels = np.array([])
    idx_tr    = np.arange(train_labels.size);
    for mm in models:
        idx_mm = idx_tr[train_labels==mm]
        sub = train_dataset[idx_mm[:nsc],:]
        small_train.append(sub)
        small_labels = np.append(small_labels,mm*np.ones(nsc))
    small_train = np.vstack(small_train)
    return small_train, small_labels


X  = np.reshape(train_dataset,(train_labels.size,28*28))
Y  = np.reshape(valid_dataset,(valid_labels.size,28*28))
Z  = np.reshape(test_dataset,(test_labels.size,28*28))


NS = [50., 100., 1000., 5000.]
CC = [1e5, 1e4, 1e3, 1e2]

RES = []
models = []
for ns in NS:
    ACC = []
    nsc = int(np.ceil(ns/num_classes))
    x,y = split_train(X,train_labels,nsc)    
    for c in CC:
        logreg = linear_model.LogisticRegression(C=c)
        logreg.fit(x,y)
        valid_pred = logreg.predict(Y)
        acc = float((valid_labels == valid_pred).sum())/valid_labels.size
        
        ACC.append(acc)
    print(ACC)
    RES.append(ACC)

 


