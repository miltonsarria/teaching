import os
#apagar wanings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
#import mnist
import numpy as np
#import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

'''
feedforward neural network
entrada -> pesos -> hidden layer 1 (funciones de activacion) -> pesos -> hidden layer 2
(funcion de activacion)-> pesos->output layer: salida

comparar la salida con lo que se espera > usando la funcion de costo (cost function): cross entropy

se emplea un algoritmo (optimizer) para minimizar la funcion de costo

backpropagation

feed forward + backpropagation = epoch
'''



#ejemplo usando mnist: 10 clases, digitos de 0 a 9
mnist=input_data.read_data_sets("/tmp/data/",one_hot=True)


n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_clases    = 10
batch_size  = 100

#dims = 28 x 28 = 784
x = tf.placeholder('float',[None,784])
y = tf.placeholder('float')

def nn_model(data):
    #entrada*weights + biases
    hidden_1_layer={'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
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
            for _ in range(int(mnist.train.num_examples/batch_size)):
                e_x,e_y = mnist.train.next_batch(batch_size)
                _,c=sess.run([optimizer,cost],feed_dict={x: e_x, y: e_y})
                epoch_loss +=c
            print('Epoca',epoch, ' completa, loss: ', epoch_loss)

        correct=tf.equal(tf.argmax(out,1),tf.argmax(y,1))
        acc=tf.reduce_mean(tf.cast(correct,'float'))
        print('Accuracy: ', acc.eval({x:mnist.test.images,y:mnist.test.labels}))
                
train_nn(x)       
        
        
        
        
