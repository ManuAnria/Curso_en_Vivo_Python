#Ejercicio 1
monedas = {"Euro":"€","Dollar":"$","Yen":"¥"}
pregunta = input("Ingrese el nombre de una divisa: ").capitalize()
if pregunta in monedas:
    print(monedas.get(pregunta))
else:
    print("La divisa no está.")

#Ejercicio 2
columnas = ["Nombre","edad","direccion","telefono"]
respuestas = []
for columna in columnas:
    respuesta = input(f"Ingrese su {columna}")
    respuestas.append(respuesta)
dicc = dict(zip(columnas,respuestas))
print(f"{dicc['Nombre']} tiene {dicc['edad']} años, vive en {dicc['direccion']} y su telefono es {dicc['telefono']}")

#Ejercicio 3
lista = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
fruta = input("Ingrese la fruta que desea comprar: ").capitalize()
if fruta not in lista:
    print("La fruta no está disponible.")
else:
    kilos = float(input("Ingrese los kilos que desea: "))
    total = lista[fruta]*kilos
    print(f"Los {kilos} kilos de {fruta} valen $ {total}")

#Ejercicio 4
meses = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre"}
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
dia = int(fecha[0:2])
mes = int(fecha[3:5])
año = int(fecha[6:10])
print(f"La fecha ingresada es el {dia} de {meses.get(mes)} del año {año}")

#Ejercicio 5
materias = {'Matemáticas':6,'Física':4,'Química':5}
total_creditos = 0
for materia in materias:
    print(f"{materia} tiene {materias[materia]} créditos")
    total_creditos += materias[materia] #si queda fuera del for solo suma el último
print(f"El total de créditos es de {total_creditos}")

#Ejercicio 6
#solucion 1
columnas = ["Nombre","edad","direccion","telefono"]
respuestas = []
for columna in columnas:
    respuesta = input(f"Ingrese su {columna}")
    respuestas.append(respuesta)
    dicc = dict(zip(columnas,respuestas))
    print(dicc)
print("Diccionario finalizado")

#solucion con más background
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ').capitalize()
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ').upper() == "SI"
print("Proceso finalizado")

#Ejercicio 7
lista = {}
continuar = True
while continuar:
    articulo = input("Que articulo desea comprar? ").capitalize()
    precio = float(input(f"Cual es el precio de {articulo}? "))
    lista[articulo] = precio
    continuar = input("Quiere agregar mas articulos a la lista (Si/No)? ").upper() == "SI"
print("Lista de articulos: ")
precio_total = 0
for articulo in lista:
    print(f"{articulo}: ${lista[articulo]}")
    precio_total += lista[articulo]
print(f"Total = {precio_total}")

#Ejercicio 8
dicc_bi = {}
palabras = input("Introduce palabras en español y su traduccion en ingles, siguiendo el siguiente ejemplo: palabra:traduccion,palabra:traduccion,")
for palabra in palabras.split(","):
    esp,ing = palabra.split(":")
    dicc_bi[esp] = ing
frase = input("Introduce una frase en español: ")
for i in frase.split(): #si no se pone nada separa por espacios
    if i in dicc_bi:
        print(dicc_bi[i], end= " ")
    else:
        print(i, end= " ")

#Ejercicio 9
facturas = {}
cobrado = 0
pendiente = 0
continuar = True
while continuar:
    pregunta = input("Que operacion desea realizar (Agregar/Cobrar)? ").upper()
    if pregunta.upper() == "AGREGAR":
        factura = input("Ingrese el numero de la factura: ")
        monto = float(input(f"Cual es el monto de la factura {factura}? "))
        facturas[factura] = monto
        pendiente += facturas[factura]
    elif pregunta.upper() == "COBRAR":
        factura = input("Que factura se cancelara? ")
        monto = facturas.pop(factura,0)
        cobrado += monto
        pendiente -= monto
    else:
        print("Comando invalido")
    print(facturas)
    print(f"Cobrado: {cobrado}")
    print(f"Pendiente: {pendiente}")
    continuar = input("Desea realizar otra operacion (Si/No)? ").upper() == "SI"
print("FIN")

#Ejercicio 10
clientes = {}
opcion = ""
while opcion != "6":
    if opcion == "1":
        id = input("Introduce el ID del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce el telefono del cliente: ")
        correo = input("Introduce el correo del cliente: ")
        preferente = input("Es un cliente preferente (S/N): ").upper()
        cliente = {"Nombre": nombre, "Dirección": direccion, "Teléfono": telefono, "Correo": correo, "Preferente": preferente == "S"}
        clientes[id] = cliente
    if opcion == "2":
        id = input("Seleccione el ID del cliente a eliminar: ")
        if id in clientes:
            clientes.pop(id)
            print(f"El cliente {cliente['Nombre']} ha sido eliminado de la base de datos")
        else:
            print("El ID ingresado no se encuentra en la base de datos.")
    if opcion == "3":
        id = input("Seleccione el ID del cliente que desea consultar: ")
        if id in clientes:
            print(clientes[id])
        else:
            print("El ID ingresado no se encuentra en la base de datos.")
    if opcion == "4":
        print(clientes)
    if opcion == "5":
        for clave,valor in clientes.items():
            if valor['Preferente']:
                print(clientes[id])
    opcion = input("Ingrese la acción a realizar:\n1: Agregar cliente\n2: Eliminar cliente\n3: Mostrar cliente\n4: Listar clientes\n5: Listar clientes preferentes\n6: Terminar")
print("FIN")
