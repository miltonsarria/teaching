#from  tkinter import * 
#to use different versions of python
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
    import tkMessageBox 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from tkinter import messagebox as tkMessageBox

class parProcess(threading.Thread):
     '''
     class to create a parallel process object
     '''
     def __init__(self, counter,sleep):
         threading.Thread.__init__(self)
         self.counter = counter
         self.sleep = sleep
     def run(self):
         print("iniciar proceso...")         
         while self.counter > 0:
             time.sleep(self.sleep)
             print('contador ', self.name, self.counter)
             self.counter=self.counter-1
             


#############################################################################################
class mainApp():
     def __init__(self,tkObject):
        self.master  = tkObject     
        self.nombre  = ''
        self.apellido= ''
        self.id      = ''
        #inicializar las dos ventanas        
        self.initMaster()
     #############################################################################################
     #funcion para inicialiciar la ventana principal
     def initMaster(self):
        self.master.title('Ejemplo - principal') 
        self.master.geometry('300x400+0+0')
        #generar boton de aceptar los datos ingresados
        self.boton = Button(self.master,text="Salir", command= self.on_exit )
        self.boton.place(x=200, y=370)
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
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

     def on_exit(self):
        """When you click to exit, this function is called"""
        if tkMessageBox.askyesno("Salir", "Quiere salir de la aplicacion?"):
        
            self.master.destroy()
            
        
     #############################################################################################                     
     def initProc1(self):        
        pass                


#############################################################################################                        

def main():    
        tkObject = Tk()       #generar objeto tipo Tk
        mainProcess = mainApp(tkObject) 
        mainProcess.master.mainloop()


if __name__ == '__main__':
    main()

