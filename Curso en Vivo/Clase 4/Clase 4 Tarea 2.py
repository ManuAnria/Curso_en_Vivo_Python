#Ejercicio 1
materias = ["Matematicas","Fisica","Lengua","Quimica","Economia"]
print(*materias, sep = ",")

#Ejercicio 2
materias = ["Matematicas","Fisica","Lengua","Quimica","Economia"]
for materia in materias:
    print(f"Yo estudio {materia}")

#Ejercicio 3
materias = ["Matematicas","Fisica","Lengua","Quimica","Economia"]
notas = []
for materia in materias:
    nota = input(f"Que nota sacaste en {materia}?: ")
    notas.append(nota)
for i in range(len(materias)):
    print(f"En la materia {materias[i]} has sacado un {notas[i]}")

#Ejercicio 4
loteria = []
for i in range(5):
    numero = int(input("Ingrese un numero ganador: "))
    loteria.append(numero)
loteria.sort()
print(loteria)

#Ejercicio 5
primeros_10 = [1,2,3,4,5,6,7,8,9,10]
primeros_10.reverse()
print(*primeros_10, sep=", ")

#Ejercicio 6
materias = ["Matematicas","Fisica","Lengua","Quimica","Economia"]
for i in range(0, len(materias)):
    nota = float(input(f"¿Qué nota sacaste en {materias[i]}?: "))
    if nota >= 5:
        materias.pop(i)
print(f"Tienes que repetir " + str(materias))


#Ejercicio 7
abc = ["a","b","c","d","e","f","g","h","i","j","k","l"]
for i in range(0,len(abc)):
    if i % 3 == 0:
        abc.pop(i-1)
print(abc)

#Ejercicio 8
palabra = input("Ingrese una palabra: ")
if palabra == palabra[::-1]:
    print(f"La palabra '{palabra}' es palindromo")
else:
    print(f"La palabra '{palabra}' no es palindromo")

#Ejercicio 9
palabra9 = input("Ingrese una palabra: ")
vocales = ["a","e","i","o","u"]
lista9 = list(palabra9)
for vocal in vocales:
    cantidad = lista9.count(vocal)
    print(f"La vocal {vocal} aparece {cantidad} veces en {palabra9}")

#Ejercicio 10
numeros10 = [50,75,46,22,80,65,8]
min = max = numeros10[0]
for numero in numeros10:
    if numero < min:
        min = numero
    elif numero >  max:
        max = numero
print(f"El menor numero es {min}")
print(f"El mayor numero es {max}")


#Alternativa
numeros10 = [50,75,46,22,80,65,8]
numeros10.sort()
print(f"El menor numero es {numeros10[0]}")
print(f"El mayor numero es {numeros10[-1]}")

#Ejercicio 11
vectores1 = [1,2,3]
vectores2 = [-1,0,2]
resultado = 0
for i in range(len(vectores2)):
   resultado += vectores1[i]*vectores2[i]
print(f"El producto escalar de los vectores {vectores1} y {vectores2} es igual a {resultado}")

#Ejercicio 12
import math
pedido = list(input("Ingrese 5 numeros, separados por coma: "))
muestra = []
suma_desvios = 0
for i in range(0,len(pedido),2):
    muestra.append(int(pedido[i]))
media = sum(muestra)/len(muestra)
for item in muestra:
    desvio = (item - media)**2
    suma_desvios += desvio
desvio_est = suma_desvios / (len(muestra)-1)
desvio_est2 = round(math.sqrt(desvio_est),4)
print(f"La media de los numeros ingresados es {media}")
print(f"La desviacion estandar de los numeros ingresados es de {desvio_est2}")




