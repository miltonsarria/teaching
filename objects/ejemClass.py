#basic example on how to define a class

#this example ilustrates the sintax to define a general class, and after how to use or modify objects 
#that are part of shuch a class


#class definition
class silla():
   #the function  __init__() will define the default properties of the objects
   def __init__(self):
      self.material     ='plastico'
      self.soporte      ='metalico'
      self.color        ='azul'
      self.funcion      ='rodar'
      self.posicion     =[0,0]
   #a function
   def desplazar(self,distancia):  
      if self.funcion=='rodar':
         self.posicion=[distancia,distancia]      

      
def main():
    silla1=silla()
    silla1.funcion='HH'      
    
    silla2=silla()
    silla2.reclinable='no'
    
    silla1.desplazar(4)
    silla2.desplazar(4)
    
    print silla1.posicion    
    print silla2.posicion

if __name__ == '__main__':
    main()
