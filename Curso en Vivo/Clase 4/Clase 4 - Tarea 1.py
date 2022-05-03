#Ejercicio 1
palabra = input("Escriba una palabra")
index = 0
while index < 10:
    print(palabra)
    index +=1

#Alternativa:
palabra2 = input("Escriba una palabra: ")
for x in range(0,10):
    print(palabra2)

#Ejercicio 2
edad = int(input("¿Qué edad tiene?"))
index = 1
while index <= edad:
    print(index)
    index +=1

#Alternativa for
edad_for = int(input("Escriba su edad: "))
for x in range(1,edad-1):
    print(x)

#Ejercicio 3
numero3 = int(input("Ingrese un numero entero"))
for i in range(1,numero3+1,2):
    print(i, end=",")

#Ejercicio 4
numero4: int = int(input("Ingrese un numero entero"))
for i in range(numero4,-1,-1):
    print(i, end=",")

#Ejercicio 5
capital = float(input("Ingrese el monto a invertir: "))
interes = float(input("Ingrese el interes deseado: "))
años = int(input("Ingrese los años que mantendra la inversion: "))
for i in range(1,años+1):
    bruto = round(capital * (1 + (interes / 100)) ** i,2)
    print(f"El capital al final del año {i} será de {bruto}")

#alternativa
capital = float(input("Ingrese el monto a invertir: "))
interes = float(input("Ingrese el interes deseado: "))
años = int(input("Ingrese los años que mantendra la inversion: "))
index = 1
while index < años+1:
    bruto = round(capital * (1 + (interes / 100)) ** index, 2)
    print(f"El capital al final del año {index} será de {bruto}")
    index +=1

#Ejercicio 6
altura = int(input("Ingrese un numero entero positivo: "))
for i in range(1,altura+1):
    print("*"*i)

#Ejercicio 7
n = 10
for i in range(1,11):
    print(f"{n} por {i} es igual a {i*n}")

#Ejercicio 8
numero8 = int(input("Ingrese un numero entero positivo: "))
for i in range(1,numero8+1,2):
   for escalera in range(i,0,-2):
       print(escalera, end  = " ")
    print("")

#Ejercicio 9
password = input("Introduzca su contraseña: ")
repita = ""
while repita != password:
    repita = input("Repita la contraseña: ")
    print("Contraseña Incorrecta. Intente nuevamente")
else:
    print("contraseña correcta")

#Ejercicio 10
numero10 = int(input("Ingrese un numero entero positivo mayor que 2: "))
for i in range(2,numero10):
    if numero10 % i == 0:
        break
if i + 1 == numero10:
    print(f"El numero {numero10} es primo")
else:
    print(f"El numero {numero10} no es primo")

#Ejercicio 11
palabra11 = input("Ingrese una palabra: ")
for letra in palabra11[::-1]:
    print(letra)

#Ejercicio 12
frase = input("Introduzca una frase: ")
letra = input("Elija una letra que aparezca en esa frase")
veces = frase.count(letra)
print(f"La letra {letra} aparece {veces} veces en la frase '{frase}'")

#alternativa
frase = input("Introduzca una frase: ")
letra = input("Elija una letra que aparezca en esa frase")
veces = 0
for i in frase:
    if i == letra:
        veces +=1
print(f"La letra {letra} aparece {veces} veces en la frase '{frase}'")

#Ejercicio 13
frase = ""
while frase.upper() != "SALIR":
    frase = input("Introduzca una frase: ")
    print(frase)
else:
    print("Ha indicado  salir del programa")
