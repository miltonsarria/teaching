#este es un  programa que implementa una calculadora
#el objetivo es ilustrar como definir y usar funciones
# 

# NOTAR QUE EL CODIGO QUE SIGUE A CONTINUACION NO SE EJECUTARA INMEDIATAMENTE
# SE ESTA DEFINIENDO QUE HACER LUEGO, CUANDO SE NECESITE

# En esta parte definiremos funciones
# Esta funcion por ejemplo imprime el menu principal y pide que el usuarion seleccione una opcion
def menu():
    #Que opcipnes se tienen?
    print(" ")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Salir de calculator.py")
    print(" ")
    return int(input("Seleccionar una opcion: "))
    
# Esta funcion suma dos numeros a y b
def add(a,b):
    a=float(a)
    b=float(b)
    print(a, "+", b, "=", a + b)
    
# Esta funcion realiza la resta de dos numeros a y b
def sub(a,b):
    a=float(a)
    b=float(b)
    print(b, "-", a, "=", b - a)
    
# esta funcion multiplica dos numeros
def mul(a,b):
    a=float(a)
    b=float(b)
    print(a, "*", b, "=", a * b)
    
# esta funcion divide dos numeros
def div(a,b):
    a=float(a)
    b=float(b)
    print(a, "/", b, "=", a / b)

##################################################################    
# ESTA PARTE ES EL CODIGO PRINCIPAL Y LO QUE REALMENTE SE EJECUTA
##################################################################

print("Bienvenido a calculator.py")
print("Sus opciones son:")
loop = 1
choice = 0
while loop == 1:
    choice = menu()

    if choice == 1:
        add(input("Sumar: "),input("con: "))
    elif choice == 2:
        sub(input("Restar: "),input("de: "))
    elif choice == 3:
        mul(input("Multiplicar: "),input("por: "))
    elif choice == 4:
        div(input("Dividir: "),input("entre: "))
    elif choice == 5:
        loop = 0

print("Gracias por usar calculator.py!")

# El programa finaliza
