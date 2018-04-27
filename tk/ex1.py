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
     def __init__(self,tkObject):
        self.master  = tkObject

        self.A   = 0
        self.F   = 0
        self.phi = 0
        #inicializar las dos ventanas        
        self.initMaster()

     #############################################################################################
     #funcion para inicialiciar la ventana principal
     def initMaster(self):
        self.master.title('Ejemplo - principal') 
        self.master.geometry('800x800+0+0')
        #generar boton de aceptar los datos ingresados
        self.boton = Button(self.master,text="Salir >>", command= self.on_exit )
        self.boton.place(x=600, y=700)
        #generar label 1 yentrada 1 para indicar donde debe ingresar nombre
        self.label1 = Label(self.master, text="Amplitud:").place(x=10,y=600)
        self.entry1 = Entry(self.master, bd =2)
        #self.entry1.pack()
        self.entry1.place(x=75,y=600)
        #generar label 2 y entrada 2 para indicar donde debe ingresar apellido
        self.label2 = Label(self.master, text="Frecuencia:").place(x=10,y=640)
        self.entry2 = Entry(self.master, bd =2)
        #self.entry2.pack()
        self.entry2.place(x=75,y=640)
        #generar label 3 y entrada 3 para indicar donde debe ingresar apellido   
        self.label3 = Label(self.master, text="Fase:").place(x=10,y=670)
        self.entry3 = Entry(self.master, bd =2)
        #self.entry3.pack()
        self.entry3.place(x=75,y=670)
        
        self.fig = plt.figure(1)
        plt.ion()
        t = np.arange(0.0,3.0,0.01)
        s = np.sin(np.pi*t)
        plt.plot(t,s)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.plot_widget = self.canvas.get_tk_widget()

        

        self.plot_widget.grid(row=100, column=100)
        self.botUpdate = Button(self.master,text="Update",command=self.update)
        self.botUpdate.place(x=75,y=700)


     def update(self):
            self.A  = float(self.entry1.get())
            self.F  = float(self.entry2.get())
            self.phi = float(self.entry3.get())/180.0*np.pi
        
            self.fig.clear() 
            t = np.arange(0.0,3.0,0.01)
            s = self.A*np.cos(2*np.pi*self.F*t+self.phi)
            plt.plot(t,s)
            self.fig.canvas.draw()   
            
     def on_exit(self):
            plt.ioff()
            plt.close()
            self.master.destroy()



     #############################################################################################        
     
    
       
#############################################################################################                        

def main():    
        tkObject = Tk()       #generar objeto tipo Tk
        
        #generar un objeto que contiene informacion relevante y como atributos se
        #van a usar dos objetos TK uno como ventana principal y otro como ventana secundaria
        mainProcess = genInterfaz(tkObject) 
        mainProcess.master.mainloop()
 
 
if __name__ == '__main__':
    main()

