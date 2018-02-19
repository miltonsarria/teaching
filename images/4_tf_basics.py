import os
#apagar wanings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

#definir dos constantes
x1 = tf.constant(5)
x2 = tf.constant(6)

#definir el resultado
result = x1*x2

print(result)
#inicializar una session
sess = tf.Session()
#ejecutar la session
r=sess.run(result)
print(r)
#cerrar
sess.close()

#abrir y cerrar la session de forma automatica
with tf.Session() as sess:
     r=sess.run(result)
     print(r)



