from  Tkinter import*


class Antojos (object):
   
     def __init__(self,master):
		 
		  self.master=master
		  self.master.title ('PRUEBA')
		  self.master.geometry ("600x700+0+0")
		  self.boton = Button(self.master,text=" SIGUIENTE >>>" ,command= self.siguiente ,  relief = GROOVE, height= 6, width= 18,justify="center", fg="blue").place(x=410, y=600)
		  #self.siguiente = cm
		  
		  
		  #self.boton1 = Button(self.master,text=" <<< ATRAS" ,command= self.atras ,  relief = GROOVE, height= 6, width= 18,justify="center", fg="blue").place(x=160, y=600)
		  
		  #self.atrass = atr
		  #self.master.ventana2=v2
		  #self.master.boton.clicked.connect(self.comidas)
		         
        
          	  
          

     #def salir (self):
		#    ventana.destroy()
   
## Esta es la inicializacion de boton siguiente (La idea es que aparezca en cada clase) 
     def siguiente (self):
		  root=Toplevel(self.master)
		  myGUI= Comida2(root)
### Inicializacion del boton atras. 		  
		  #def atras (self):
			#  root1 = Toplevel(self.master)
			 # myGUI=Antojos(root1)
		 #Antojos.iconify()
	 
            
  
### Clase de comidas, donde debe existir el boton siguiente y uno de atras. 		 		  
class Comida2(object):    
    def __init__(self,master):
            self.master=master
            self.master.title('Comidas') 
            self.master.geometry('600x700+650+0')
            #self.siguiente
     	  
        #super(Comidas2, self).__init__() 
        #self.objeto=objeto
        
def main():    

 ventana = Tk()
 myGUIAntojos=Antojos(ventana)
 
     
    #cm = Comida2()
 #v1 = Antojos(self, master ,cm)
 ventana.mainloop()
 
if __name__ == '__main__':
    main()

