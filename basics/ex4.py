#programa para ilustrar el uso de ciclos y condicionales, parte 1
#antes es necesario conocer algunas operaciones logicas

# Expresion	Funcion
#==========================
# <	        Menor que
# <=	        Menor o igual a 
# >	        Mayor que
# >=	        Mayor igual a
# !=	        Diferente de
# <>	        Diferente de (forma alternativa)
# ==	        Igual a 

#el resultado de usar estas operaciones es una variable logica False o True
#5>3 dara como resultado True
#3>5 dara como resultado False


#analizar los siguientes ciclos y analizar lo que se hace en cada instruccion

#######################################################################
print('#######################################################################')
print("Ejemplo 1:")
print("Mostraremos los numeros pares hasta 20 ")
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n)
    n = n + 1
print("Listo, termine.")

print('#######################################################################')

print("\n\nEjemplo 2:")

a = 1
if a > 5:
    print("Esto no deberia pasar")
else:
    print("esto si deberia pasar")
    

print('#######################################################################')
print("\n\nEjemplo 3:")    
    
a = 10
while a > 0:
    print(a)
    if a > 5:
        print("Numero grande!")
    elif a % 2 != 0:
        print("Este es un numero impar")
        print("No es mayor que 5")
    else:
        print("Este numero no es mayor a 5")
        print("Es un numero par")
        print("te sientes especial")
    a = a - 1
    print("Ahora el valor de 'a' vale una unidad menos")
    print("Mientras no sea menor que cero, haremos el ciclo de nuevo")
print("Parece que ya 'a' es menor a cero")
print("El ciclo ha finalizado")
