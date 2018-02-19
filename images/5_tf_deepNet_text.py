import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
#apagar wanings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
import pickle
import random
from collections import Counter

lemmatizer = WordNetLemmatizer()
hm_lines   = 10000000

#files
neg_file='/home/sarria/data/lexicon/neg.txt'
pos_file='/home/sarria/data/lexicon/pos.txt'

def create_lexicon(pos,neg):
    lexicon = []
    for fi in [pos,neg]:
        with open(fi,'r') as fh:
            contents = fh.readlines()
            for l in contents[:hm_lines]:
                all_words=word_tokenize(l.lower())
                lexicon +=list(all_words)
            
    lexicon=[lemmatizer.lemmatize(i) for i in lexicon]
    w_counts = Counter(lexicon)
    l2=[]
    for w in w_counts:
        if 1000>w_counts[w]>50:
            l2.append(w)
    return l2
            


def sample_handling(sample,lexicon,classification):
    featureset=[]
        
    with open(sample,'r') as fh:
        contents = fh.readlines()
        for l in contents[:hm_lines]:
            current_words = word_tokenize(l.lower())
            current_words = [lemmatizer.lemmatize(i) for i in current_words]
            features = np.zeros(len(lexicon))
            for word in current_words:
                if word.lower() in lexicon:
                    index_value = lexicon.index(word.lower())
                    features[index_value]+=1
                    featureset.append([features,classification])
                
    return featureset


def create_feature_sets_labels(pos_file,neg_file,test_size=0.1):
        lexicon = create_lexicon(pos_file,neg_file)
        print('Lexicon: ', len(lexicon))
        features=[]
        features+=sample_handling(pos_file,lexicon,[1,0])
        features+=sample_handling(neg_file,lexicon,[0,1])
        random.shuffle(features)
        features = np.array(features)
        
        testing_size=int(test_size*len(features))
        
        train_x=list(features[:,0][:-testing_size])
        train_y=list(features[:,1][:-testing_size])
        
        
        test_x=list(features[:,0][-testing_size:])
        test_y=list(features[:,1][-testing_size:])
        
        return train_x,train_y,test_x,test_y
        
#####################################################################################
#####################################################################################
#####################################################################################
print('Preparando datos...')
train_x,train_y,test_x,test_y=create_feature_sets_labels(pos_file,neg_file)     
#with open ('/home/sarria/data/lexicon/sentimen_set.pickle','wb') as fh:
#    pickle.dump([train_x,train_y,test_x,test_y],fh)
print('Done!!')

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_clases    = 2
batch_size  = 100

#dims = 28 x 28 = 784
x = tf.placeholder('float',[None,len(train_x[0])])
y = tf.placeholder('float')

def nn_model(data):
    #entrada*weights + biases
    hidden_1_layer={'weights':tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
                    'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                    'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                    'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_clases])),
                    'biases':tf.Variable(tf.random_normal([n_clases]))}


    l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']),hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)
    
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']),hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']),hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3,output_layer['weights']),output_layer['biases'])

    return output 


def train_nn(x):
    out = nn_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=out,labels=y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    epochs=10
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(epochs):
            epoch_loss = 0
            i=0
            while i<len(train_x):
                start =i
                end = i+batch_size
                e_x = np.array(train_x[start:end])
                e_y = np.array(train_y[start:end])

                _,c=sess.run([optimizer,cost],feed_dict={x: e_x, y: e_y})
                epoch_loss +=c
                i+=batch_size
            print('Epoca',epoch, ' completa, loss: ', epoch_loss)

        correct=tf.equal(tf.argmax(out,1),tf.argmax(y,1))
        acc=tf.reduce_mean(tf.cast(correct,'float'))
        print('Accuracy: ', acc.eval({x:test_x,y:test_y}))
                
train_nn(x)       
        
               


