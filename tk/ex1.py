from  Tkinter import *

#############################################################################################
class VPrincipal():
     def __init__(self,tkObject,topObject):
        self.master  = tkObject
        self.second  = topObject        
        self.nombre  = ''
        self.apellido= ''
        self.id      = ''
        #inicializar las dos ventanas        
        self.initMaster()
        self.initSecond()
     #############################################################################################
     #funcion para inicialiciar la ventana principal
     def initMaster(self):
        self.master.title('Ejemplo - principal') 
        self.master.geometry('300x400+0+0')
        #generar boton de aceptar los datos ingresados
        self.boton = Button(self.master,text="Aceptar", command= self.guardarDatos )
        self.boton.place(x=200, y=370)
        #generar label 1 yentrada 1 para indicar donde debe ingresar nombre
        self.label1 = Label(self.master, text="Nombre:").place(x=10,y=10)
        self.entry1 = Entry(self.master, bd =2)
        self.entry1.pack()
        self.entry1.place(x=75,y=10)
        #generar label 2 y entrada 2 para indicar donde debe ingresar apellido
        self.label2 = Label(self.master, text="Apellido:").place(x=10,y=40)
        self.entry2 = Entry(self.master, bd =2)
        self.entry2.pack()
        self.entry2.place(x=75,y=40)
        #generar label 3 y entrada 3 para indicar donde debe ingresar apellido   
        self.label3 = Label(self.master, text="Cedula:").place(x=10,y=70)
        self.entry3 = Entry(self.master, bd =2)
        self.entry3.pack()
        self.entry3.place(x=75,y=70)
     #############################################################################################        
     #funcion para inicialiciar la ventana secundaria
     def initSecond(self):
        self.second.title('Ejemplo - secundaria') 
        self.second.geometry('300x400+100+100')
        #generar boton para volver a la principal
        self.botonBack = Button(self.second,text="Volver", command= self.volverPrincipal )
        self.botonBack.place(x=200, y=370)
        #generar label 4 para indicar el nombre, ventana 2
        self.label4 = Label(self.second, text="Nombre:").place(x=10,y=10)
        #generar label 5 para indicar el apellido, ventana 2
        self.label5= Label(self.second, text="Apellido:").place(x=10,y=40)
        #generar label 6 para indicar el id, ventana 2  
        self.label6 = Label(self.second, text="Cedula:").place(x=10,y=70)

          
        self.second.withdraw()  
     #############################################################################################                     
     #esta funcion guarda los datos y muestra la ventana 2 con los datos que ha guardado
     def guardarDatos(self):        
        self.nombre  =self.entry1.get()
        self.apellido=self.entry2.get()
        self.id      =self.entry3.get()
        #generar labels para mostrar informacion
        #generar label 7 para mostrar el nombre, ventana 2
        self.label7 = Label(self.second, text=self.nombre).place(x=75,y=10)
        #generar label 8 para mostrar el apellido, ventana 2
        self.label8= Label(self.second, text=self.apellido).place(x=75,y=40)
        #generar label 9 para mostrar el id, ventana 2  
        self.label9 = Label(self.second, text=self.id).place(x=75,y=70)
        
        self.second.deiconify() 
        self.master.withdraw()                
     #############################################################################################        
     def volverPrincipal(self):                
        self.second.withdraw() 
        self.master.deiconify()        
#############################################################################################                        

def main():    
        tkObject = Tk()       #generar objeto tipo Tk
        topObject = Toplevel()#generar la ventana secundaria
        #generar un objeto que contiene informacion relevante y como atributos se
        #van a usar dos objetos TK uno como ventana principal y otro como ventana secundaria
        ventana1 = VPrincipal(tkObject,topObject) 
        ventana1.master.mainloop()
 
 
if __name__ == '__main__':
    main()

