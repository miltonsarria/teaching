#from  tkinter import * 
#to use different versions of python

import numpy as np

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


#############################################################################################
class genInterfaz():
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
        self.master.geometry('800x800+0+0')
        #generar boton de aceptar los datos ingresados
        self.boton = Button(self.master,text="Aceptar", command= self.guardarDatos )
        self.boton.place(x=600, y=700)
        #generar label 1 yentrada 1 para indicar donde debe ingresar nombre
        self.label1 = Label(self.master, text="Nombre:").place(x=10,y=10)
        self.entry1 = Entry(self.master, bd =2)
        #self.entry1.pack()
        self.entry1.place(x=75,y=10)
        #generar label 2 y entrada 2 para indicar donde debe ingresar apellido
        self.label2 = Label(self.master, text="Apellido:").place(x=10,y=40)
        self.entry2 = Entry(self.master, bd =2)
        #self.entry2.pack()
        self.entry2.place(x=75,y=40)
        #generar label 3 y entrada 3 para indicar donde debe ingresar apellido   
        self.label3 = Label(self.master, text="Cedula:").place(x=10,y=70)
        self.entry3 = Entry(self.master, bd =2)
        #self.entry3.pack()
        self.entry3.place(x=75,y=70)
        
        self.fig = plt.figure(1)
        plt.ion()
        t = np.arange(0.0,3.0,0.01)
        s = np.sin(np.pi*t)
        plt.plot(t,s)
        canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        plot_widget = canvas.get_tk_widget()

        

        plot_widget.grid(row=300, column=300)
        self.botUpdate = Button(self.master,text="Update",command=self.update).grid(row=1, column=0)
     


     def update(self):
            self.fig.clear() 
            t = np.arange(0.0,3.0,0.01)
            s = np.cos(np.pi*t)
            plt.plot(t,s)
            self.fig.canvas.draw()   
     def on_exit(self):
         self.second.destroy()
         self.master.destroy()



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

        #generar labels para mostrar informacion
        #generar label 7 para mostrar el nombre, ventana 2
        self.label7 = Label(self.second, text='')
        self.label7.place(x=75,y=10)
        #generar label 8 para mostrar el apellido, ventana 2
        self.label8= Label(self.second, text='')
        self.label8.place(x=75,y=40)
        #generar label 9 para mostrar el id, ventana 2  
        self.label9 = Label(self.second, text='')
        self.label9.place(x=75,y=70)
        
          
        self.second.withdraw()  
     #############################################################################################                     
     #esta funcion guarda los datos y muestra la ventana 2 con los datos que ha guardado
     def guardarDatos(self):        
        self.nombre  =self.entry1.get()
        self.apellido=self.entry2.get()
        self.id      =self.entry3.get()
        #mostrar informacion en ventana 2, usando los labels ya generados
        #usar label 7 para mostrar el nombre, ventana 2
        self.label7['text'] = self.nombre
        #usar label 8 para mostrar el apellido, ventana 2
        self.label8['text'] = self.apellido
        #usar label 9 para mostrar el id, ventana 2  
        self.label9['text'] = self.id
        
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
        mainProcess = genInterfaz(tkObject,topObject) 
        mainProcess.master.mainloop()
 
 
if __name__ == '__main__':
    main()

