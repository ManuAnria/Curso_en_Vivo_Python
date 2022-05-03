#Ejercicio 1
print("¡Hola mundo!")

#Ejercicio 2
saludo="Hola mundo"
print(saludo)

#Ejercicio 3
nombre_usuario=input("¿Cómo es tu nombre?")
print("Hola "+nombre_usuario)

#Ejercicio 4
print(((3+2)/(2-5))**2)
#alternativa
operacion = (3+2)/(2-5)
print(operacion**2)

#Ejercicio 5
horas_trabajadas = int(input("Ingresa tus horas trabajadas"))
coste_hora = int(input("Ingresa tu sueldo por hora"))
sueldo_a_cobrar = (horas_trabajadas)*(coste_hora)

print("El sueldo que te corresponde es de $ " + str(sueldo_a_cobrar))

#Ejercicio 6
numero_aleatorio = int(input("Introduzca un número entero aleatorio"))
suma= (numero_aleatorio*(numero_aleatorio+1))/2
print("El número elegido es " +str(numero_aleatorio) +"\nLa suma de 1 hasta "+str(numero_aleatorio)+" es "+str(suma))

#Ejercicio 7
peso = input ("Introduzca su peso en Kg.: ")
altura = input ("Introduzca su altura en metros: ")
imc = round(float(peso)/(float(altura)**2),2)
print("Tu índice de masa corporal es "+str(imc))

#Ejercicio 8
numero1 = input("Ingresa un número entero: ")
numero2 = input("Ingresa otro número entero: ")
cociente = int(numero1)//int(numero2)
resto = int(numero1)%int(numero2)
print("La división entre "+str(numero1)+" y "+str(numero2)+" da por resultado un cociente igual a "+str(cociente)+" y un resto de "+str(resto))

#Ejercicio 9
cantidad_a_invertir = input("¿Cuánto quisiera invertir? ")
interes_anual = input("¿Qué porcentaje de interés anual quisiera obtener? ")
años = input("¿Cuántos años querría mantener su inversión? ")
ganancia = round(float(cantidad_a_invertir)*((1+(float(interes_anual)/100))**float(años)),2)
print ("Su capital al cierre será de $" +str(ganancia))

#Ejercicio 10
payasos_vendidos = input("Ingrese cantidad de payasos vendidos")
muñecas_vendidas = input("Ingrese cantidad de muñecas vendidas")
peso_total_payasos = int(payasos_vendidos)*112
peso_total_muñecas = int(muñecas_vendidas)*75
peso_paquete = round((peso_total_payasos+peso_total_muñecas)/1000,2)
print ("El peso del paquete es de "+str(peso_paquete)+ (" Kg."))

#alternativa ejercicio 10
payasos_vendidos = input("Ingrese cantidad de payasos vendidos")
muñecas_vendidas = input("Ingrese cantidad de muñecas vendidas")
peso_total_payasos = int(payasos_vendidos)*112
peso_total_muñecas = int(muñecas_vendidas)*75
peso_paquete = round((peso_total_payasos+peso_total_muñecas)/1000,2)
print (f"El peso del paquete es de {peso_paquete} kg.")

#Ejercicio 11
monto_depositado = input("Ingrese el importe depositado")
saldo_año1 = round(float(monto_depositado)*1.04,2)
saldo_año2 = round(saldo_año1*1.04,2)
saldo_año3 = round(saldo_año2*1.04,2)
print(f"El saldo al final del primer año es de $ {saldo_año1}"
      f"\nEl saldo al final del segundo año sera de $ {saldo_año2}"
      f"\nEl saldo al final del tercer año sera de $ {saldo_año3}")

#ejercicio 12
pan_dia_anterior = input("Ingrese cantidad de barras de pan del dia anterior vendida durante el dia de hoy")
costo_pan_viejo = round(3.69*0.4,2)
ingresos_pan_viejo = round(float(pan_dia_anterior)*costo_pan_viejo,2)
perdida_pan = round(float(pan_dia_anterior)*3.69*0.6,2)
print(f"El costo de una barra de pan preparada el dia de hoy es de $3.69, mientras que el costo de una barra de pan del dia anterior es de {costo_pan_viejo}"
      f"\nEl descuento aplicado sobre una barra de pan del dia anterior es de 60%"
      f"\nLos ingresos por venta de {pan_dia_anterior} barras de pan del dia anterior ascienden a $ {ingresos_pan_viejo}"
      f"\nLas perdidas por no haber vendido el pan durante el mismo dia de produccion ascienden a $ {perdida_pan}")