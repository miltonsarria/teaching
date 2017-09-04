from  Tkinter import*


class Ventana1(Tk):
     def __init__(self):
        self.title('Comidas') 
        self.geometry('600x700+650+0')
        self.boton = Button(self,text="Siguiente" ,command= self.siguiente )
        
        
     def siguiente(self):
         print("hola")


def main():    

 principal = Ventana1()
 principal.mainloop()
 
if __name__ == '__main__':
    main()

