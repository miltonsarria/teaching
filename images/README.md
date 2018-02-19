to run a simple example using MNIST dataset you neet to install the mnist helper to read the dataset

$pip install python-mnist

neet to have:
t10k-images-idx3-ubyte
t10k-labels-idx1-ubyte
train-images-idx3-ubyte
train-labels-idx1-ubyte

Then run

$python 1_example_mnist.py


how to install tensorflow using anaconda

Create a conda environment named tensorflow to run a version of Python by invoking the following command:

$conda create -n tensorflow python=3.4 matplotlib scipy scikit-learn IPython Pillow
activate the environmentPillow

$source activate tensorflow

install tensorflow using pip

$pip install tensorflow 


Need to have:
notMNIST_large.tar.gz
notMNIST_small.tar.gz

to generate the pickle files which will contain training and testing data you have to run
$python 2_extract_notMNIST.py



If you want to work with text, it is useful to install nltk for python
$pip install nltk


then python
>>>import nltk
>>>nltk.download()
and download all









