#ciclo FOR
#el ciclo for permite fe forma iterativa realizar una serie de operaciones desde un punto inicial a un punto final
#Es un ciclo donde se puede indicar de antemano el numero minimo de iteraciones que la instruccion realizara

#en el siguiente ejemplo se ilustra el funcionamiento basico al imprimir cada una de las letras de una palabra


# Porristas
print(" Ejemplo 1: porras")

try:
  word = input("Python 3: Cual es su equipo de futbol favorito? ")
except:
  word = raw_input("Python 2: Cual es su equipo de futbol favorito? ")


for letter in word:
    call = "Dame la " + letter + "!"
    print(call)
    print(letter + "!")

print("Que dice?!!")
print(word + "!!!!!!")


print("\n\n ---------------")
print("Ejemplo 2: indices")
#ejemplo 2
#definir una lista de indices

indices=[0,1,2,3,4,5,6,7,8,9]

#iterar sobre esos indices y realizar una operacion
for i in indices:
    print('----------')
    print('indice: ',i)
    print('i^2 es: ', i**2)
    



