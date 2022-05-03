#Ejercicio 1
edad_usuario = input("Introduzca su edad en números: ")
if int(edad_usuario) >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")

#Ejercicio 2
contraseña = input("Contraseña: ")
pedido = input ("Ingrese nuevamente su contraseña: ")
if contraseña.lower() == pedido.lower():
    print ("La contraseña coincide con la guardada")
else:
    print ("La contraseña es incorrecta")

#Ejercicio 3
numero1 = input ("Ingreso un número")
numero2 =int(input ("Ingrese otro número"))
if numero2 != 0:
    division = round(int(numero1) / numero2, 2)
    print (f"La división entre {numero1} y {numero2} es igual a {division}")
else:
    print ("Error")

#alternativa
numero1 = input ("Ingreso un número")
numero2 = int(input ("Ingrese otro número"))
if numero2 == 0:
    print("Error")
else:
    division = round(int(numero1) / numero2, 2)
    print(f"La división entre {numero1} y {numero2} es igual a {division}")

#Ejercicio 4
numero =input ("Introduzca un número: ")
resto = int(numero) % 2
if resto == 0:
    print (numero +" es un número par")
else:
    print (f"{numero} es un número impar")

#Ejercicio 5
edad = int(input("Ingrese su edad: "))
if edad <= 16:
    print ("Es menor de 16 años - No tributa")
else:
    ingresos = float(input("Declare sus ingresos mensuales: "))
    if ingresos >= 1000:
        print ("Usted debe tributar")
    else:
        print ("No alcanza el monto de ingresos mínimos - No tributa")

#Ejercicio 6
genero = input("Indique su género escrribiendo 'M' para masculino y 'F' para femenino: ")
letra_nombre = input("Escriba la primera letra de su nombre: ")
if genero.upper() == "F":
    if letra_nombre.upper() <= "M":
        print ("Usted corresponde al grupo A")
    else:
        print ("Usted corresponde al grupo B")
else:
    if letra_nombre.upper() >= "N":
        print ("Usted corresponde al grupo A")
    else:
        print ("Usted corresponde al grupo B")

#Alternativa
genero = input("Indique su género escrribiendo 'M' para masculino y 'F' para femenino: ")
letra_nombre2 = input("Escriba su nombre: ")
if genero.upper() == "F":
    if letra_nombre2[0].upper() <= "M":
        print ("Usted corresponde al grupo A")
    else:
        print ("Usted corresponde al grupo B")
else:
    if letra_nombre2[0].upper() >= "N":
        print ("Usted corresponde al grupo A")
    else:
        print ("Usted corresponde al grupo B")

#Ejercicio 7
ingresos_usuario = float(input("Ingrese el monto de sus ingresos: "))
if ingresos_usuario < 10000:
    print ("Su tipo impositivo es de un 5%")
else:
    if ingresos_usuario >= 10000 and ingresos_usuario < 20000:
        print ("Su tipo impositivo es de un 15%")
    else:
        if ingresos_usuario >= 20000 and ingresos_usuario < 35000:
            print("Su tipo impositivo es de un 20%")
        else:
            if ingresos_usuario >= 35000 and ingresos_usuario < 60000:
                print("Su tipo impositivo es de un 30%")
            else:
                print ("Su tipo impositivo es de un 45%")

#Ejercicio 8
puntuacion = float(input("Introduzca su puntuación: "))
monto = round((puntuacion * 2400),2)
if puntuacion == 0.0:
    print("Su nivel de rendimiento es 'Inaceptable'; no recibirá dinero")
elif puntuacion == 0.4:
    print(f"Su nivel de rendimiento es 'Aceptable', recibirá una cantidad de $ {monto}")
elif puntuacion >= 0.6:
    print(f"Su nivel de rendimiento es 'Meritorio', recibirá una cantidad de $ {monto}")
else:
    print("La puntuación no es válida")

#Ejercicio 9
edad_jugador = int(input("Ingrese su edad"))
entrada_rango1 = 5
entrada_rango2 = 10
if edad_jugador < 4:
    print("No debe pagar")
elif edad_jugador >= 4 and edad_jugador < 18:
    print(f"El monto a pagar es $ {entrada_rango1}")
else:
    print(f"El monto a pagar es $ {entrada_rango2}")

#Ejercicio 10
vegetarianas = ["TOFU","PIMIENTO"]
no_vegetarianas = ["PEPERONI","JAMON","SALMON"]
eleccion_veg = ""
eleccion_noveg = ""
menu = input("Ingrese el menu que desea: 'V' para vegetariano y 'NV' para no vegetariano")
if menu.upper() == "V":
    print("Las opciones vegetarianas son :")
    print(*vegetarianas,sep = " - ")
    while eleccion_veg.upper() not in vegetarianas:
        eleccion_veg = input("Seleccione la opcion que prefiera:")
        if eleccion_veg.upper() == "TOFU":
            print("La pizza seleccionada es vegetariana y tendra mozzarella, tomate y tofu")
        elif eleccion_veg.upper() == "PIMIENTO":
         print("La pizza seleccionada es vegetariana y tendra mozzarella, tomate y pimiento")
        else:
            print("Opcion incorrecta")
else:
    print("Las opciones no vegetarianas son :")
    print(*no_vegetarianas,sep = " - ")
    while eleccion_noveg.upper() not in no_vegetarianas:
        eleccion_noveg = input("Seleccione la opcion que prefiera:")
        if eleccion_noveg.upper() == "PEPERONI":
            print("La pizza seleccionada es no vegetariana y tendra mozzarella, tomate y peperoni")
        elif eleccion_noveg.upper() == "JAMON":
            print("La pizza seleccionada es no vegetariana y tendra mozzarella, tomate y jamon")
         elif eleccion_noveg.upper() == "SALMON":
             print("La pizza seleccionada es no vegetariana y tendra mozzarella, tomate y salmon")
        else:
            print("Valor invalido. Revise opcion ingresada")

