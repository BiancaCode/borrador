#19/01/2022
#Bianca González

print(20 + 2)#Suma
print(250 - 30) #Resta
print(20 * 3) #Multiplicación
print(315 / 4) #División
print(315 // 4) #División Entera
print(315 % 4 ) #Módulo
print(4 ** 3) #Potencia

"""Usando Variables
Concatenando"""

nombre='Pedro'
saludos='Buenas Noches'
print(saludos+nombre)

nombre='Marcos'
cantidad=4
fruta='piñas'
accion='compro'
print(nombre+' '+accion+' '+str(cantidad)+" "+fruta)

#Usando print()
#Imprimiendo Variables
nombre='Ana'
edad = 18
print(nombre)
print(edad)

print(nombre, edad) #Imprimiendo varias variables

print(nombre)
print()#Deja una linea en blanco
print(edad)

print(nombre)
print("\n")#Provoca salto de linea
print(edad)


#Imprimiendo sin Salto de Línea

estudiante = 'Eric'
saludo = 'Bienvenido'
print(saludo, estudiante, end="")

#Combinación de Texto y Variables
nombre='Ana'
edad=18
print(nombre, 'tiene', edad, 'años de edad')

nombre='Pedro'
edad=20
print( nombre, 'tiene', edad*2, 'años de edad')

#Imprimiendo variables como parámetro

nombre='Luis'
print(f"Hola {nombre}!")

#Impresión utilizando Separadores

print(192,168,168,20, sep='.')

directorio = 'c:\Laboratorios'
archivo = 'Lab1.py'
print("Ruta:" + directorio, archivo, sep='\\')

#Imprimiendo con operadores de formato

numero = 50
nombre = 'Ana'
impuesto = 8.2545
print("El valor es: %d"%numero)
print("Buenas Noches %s"%nombre)
print("El impuesto es: %.2f"%impuesto)


