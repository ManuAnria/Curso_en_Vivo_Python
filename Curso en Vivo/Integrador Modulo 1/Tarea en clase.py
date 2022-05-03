#Tarea en clase
gaseosas = {
    "Lima": {"precio":78,"stock":50},
    "Cola": {"precio":90,"stock":70},
    "Naranja": {"precio":52,"stock":50},
    "Manzana": {"precio":44,"stock":90}
}
ingresos_totales = 0
egresos_totales = 0

#ingreso
def procesar_ingreso() -> None:
    nombre = ""
    while nombre != "fin":
        print("------INGRESO------")
        nombre = input("Ingresar el nombre de la gaseosa: ")
        if nombre != "fin":
            try:
                cantidad = int(input("Ingresar la cantidad: "))
                incrementar_stock(cantidad, nombre)
            except ValueError:
                print("No ingresaste una cantidad correcta. Se esperaba un numero entero")


def incrementar_stock(cantidad: int, nombre:str) -> None:
    try:
        gaseosas[nombre]["stock"] = gaseosas[nombre]["stock"] + cantidad
        global ingresos_totales
        ingresos_totales += 1
    except KeyError:
        print("La gaseosa no existe. Intenta de nuevo.")




#Egreso
def procesar_egreso() -> None:
    nombre = ""
    while nombre != "fin":
        print("-----EGRESO------")
        nombre = input("Ingresar el nombre de la gaseosa: ")
        if nombre != "fin":
            try:
                cantidad = int(input("Ingresar la cantidad: "))
                decrementar_stock(cantidad, nombre)
            except ValueError:
                print("No ingresaste una cantidad correcta. Se esperaba un numero entero")


def decrementar_stock(cantidad: int, nombre: str) -> None:
    try:
        if gaseosas[nombre]["stock"] < cantidad:
            print(f"No hay stock suficiente de {nombre}, solo hay {gaseosas[nombre]['stock']}")
        else:
            gaseosas[nombre]["stock"] = gaseosas[nombre]["stock"] - cantidad
            global egresos_totales
            egresos_totales += 1
    except KeyError:
        print("La gaseosa no existe. Intenta de nuevo.")


#Cierre mensual
def procesar_cierre_mensual() -> None:
    mostrar_stock_final()
    mostrar_balance_viajes()
    mostrar_valuacion_inventario()


def mostrar_valuacion_inventario():
    for gaseosa in gaseosas:
        valuacion_inventario = gaseosas[gaseosa]["stock"] * gaseosas[gaseosa]["precio"]
        print(f"La valuacion de inventario para {gaseosa} es {valuacion_inventario}")


def mostrar_balance_viajes():
    print(f"La cantidad de egresos totales es {egresos_totales}")
    print(f"La cantidad de ingresos totales es {ingresos_totales}")
    print(f"El balance total de viajes es: {egresos_totales - ingresos_totales}")


def mostrar_stock_final():
    for gaseosa in gaseosas:
        print(f"El stock para {gaseosa} es: {gaseosas[gaseosa]['stock']}")


def main() -> None:
    comando = ""
    while comando != "fin":
        comando = input("Ingrese la accion que desea realizar (Ingreso/Egreso/Cierre Mensual): ")
        if comando == "ingreso":
            procesar_ingreso()
        elif comando == "egreso":
            procesar_egreso()
        elif comando == "cierre mensual":
            procesar_cierre_mensual()
        else:
            print("El comando es invalido, los disponibles son [ingreso, egreso, cierre mensual]")
    print("FIN")


main()