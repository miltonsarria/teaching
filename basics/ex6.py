#existe otro tipo de variables
#en este programa se ilusta el uso de tuplas, listas y diccionarios
#son variables de multiple proposito que pueden almacenar numeros, caracteres, matrices....

#tuple: similar a un arreglo, pero una vez definida no se puede modificar
#Ejemplo
print('\n\n Tuple')
months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')

print(months)
#notar que el simbolo '\' al final de la primer linea, permite continuar con la instruccion en la siguiente linea
# se puede representar de la siguiente forma

#Indice	  Valor
#-----------
#0	  January
#1	  Feb
#2	  Mar
#3	  Apr
#4	  May
#5	  Jun
#6	  Jul
#7	  Aug
#8	  Sep
#9	  Oct
#10	  Nov
#11	  Dec

#List:  es un arreglo que permite guardar diferentes tipos de valores, similar a tuple, pero en este caso si se puede modificar
#ejemplo nombres de gatos
print('\n Listas')
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
print(cats[2])

#agregar un nuevo nombre, o un nuevo item a la lista
cats.append('Catherine')  
print(cats)

#borrar el 3er item de la lista
del cats[2]
#imprimir la lista resultante
print(cats)

#Dictionaries: es un tipo de variable que al igual que las listas y tuplas manejan indices para acceder a los datos guardados, pero los indices son personalizables, es decir, definidos por el usuario
print('\n\n Diccionarios')

phonebook = {'Andres Marin':8806336, \
'Emily Martinez':6784346, 'Pedro Ospina':7658344, \
'Luis Giraldo':1122345}

#agregar un item
phonebook['Barba Roja'] = 1234567
#eliminar un item
del phonebook['Andres Marin']

#mostrar el diccionario
print(phonebook)

print('\n\n Ejemplo diccionarios')
#ejemplos
#crear un diccionario vacio
edades = {}
#Agregar algunos datos
edades['Sara'] = 23
edades['Leidy'] = 19
edades['Carlos'] = 38
edades['Karen'] = 45

#usar la funcion has_key si se trabaja en python 2.7, de lo contrario usar el operador in
#esta funcion pregunta por un item, si existe retorna True, si no existe retorna False

if 'Sara' in edades:
    print("Sara esta en el diccionario. Ella tiene", \
edades['Sara'], "meses")

else:
    print("Sara no esta en el diccionario")

#usar la funcion keys
#Esta funcion retorna una lista de todos los indices o campos que existen en el diccionario

print("Las siguientes personas estan en el diccionario:")
print(edades.keys())


#Se puede usar la funcion values() para acceder unicamente a los valores contenidos en el diccionario
print("Las personas tienen las siguientes edades", \
edades.values())

print("\n\n-------------------")
#que operaciones se realizan y que se imprime despues de las siguientes instrucciones?
keys=list(edades.keys())
print(keys)
keys.sort()
print(keys)

values = list(edades.values())
print(values)
values.sort()
print(values)






