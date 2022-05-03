#Ejercicio 1
nombre = input("¿Cual es tu nombre? ")
numero = input("Introduzca un numero: ")
print((nombre + "\n") *int(numero))

#Ejercicio 2
nombre = input("¿Cual es tu nombre completo? ")
print(nombre.upper() +"\n" +nombre.lower() +"\n" +nombre.title())

#Ejercicio 3
nombre = input("¿Cual es tu nombre? ")
cantidad_letras = len(nombre)
print(f"{nombre.upper()} tiene {cantidad_letras} letras")

#Ejercicio 4
telefono = input("Ingrese su numero de telefono, incluyendo codigo de area(con signo +) y extension, separado por guiones")
print(telefono[4:13])

#Ejercicio 5
frase = input("Escriba una frase")
print("".join(reversed(frase)))

#Ejercicio 6
frase = input("Escriba una frase")
letra = input("Elija una letra de esa frase")
print(frase.replace(letra,letra.upper()))

#Ejercicio 7
mail = input("Introduzca su correo electronico")
nombre_usuario = mail.split("@")
nombre_cortado = (nombre_usuario[0])
extension_edu = "@ceu.es"
nombre_educativo = nombre_cortado+extension_edu
print(nombre_educativo)

#Ejercicio 8
precio = input("Introduzca el precio en numero y con 2 decimales: ")
separados = precio.split(".")
euros = separados[0]
centimos = separados[1]
print(f"El precio es {euros} euros y {centimos} centimos")

#Ejercicio 9
fecha = input("Introduzca su fecha de cumpleaños en formato dd/mm/aaaa")
separados2 = fecha.split("/")
dia = separados2[0]
mes = separados2[1]
año = separados2[2]
print(f"El dia es {dia}."
      f"\n El mes es {mes}."
      f"\n El año es {año}.")

#ejercicio 10
lista = input("Inserte la lista de productos, separandolos con una coma")
print(lista.replace(",","\n"))

#Ejercicio 11
producto = input("Introduzca el nombre del producto")
precio = round(float(input("Introduzca el precio del producto")),2)
precio = "{:.2f}".format(precio)
cantidad = round(int(input ("introduzca la cantidad de unidades del producto")),2)
costo = float(precio)*float(cantidad)
costo = "{:.2f}".format(costo)
print(f"{producto} tiene un  costo de $ {precio.zfill(9)}; llevando {(str(cantidad).zfill(3))} unidades, el costo total es de $ {costo.zfill(11)}")
