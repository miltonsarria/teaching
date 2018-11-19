
##############################################
class estufas():
    def __init__(self,recipiente=None):
        self.encendida  = False
        self.recipiente = recipiente
    def encender(self):
        self.encendida  = True
        self.nivel      = "Alto"
        self.recipiente.temperatura  = 101    

class ollas():
    def __init__(self):
        self.llena        = False
        self.temperatura  = 25
        self.hervir       = False
    def cocinar(self):
        if self.temperatura > 100:    
            self.hervir = True
##############################################        
olla = ollas()
estufa = estufas(olla)    
olla.llena = True
olla.cocinar()
print('llena:', olla.llena)
print('temp:', olla.temperatura)

estufa.encender()
olla.cocinar()
print('temp:', olla.temperatura)
print('herv.:',olla.hervir)




    




