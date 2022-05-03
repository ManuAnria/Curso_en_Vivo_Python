# TP Integrador Modulo 1
productos = {
    "ESPONJA": {"precio": 70, "stock": 150},
    "BOLSA RESIDUOS": {"precio": 120, "stock": 70},
    "FOSFOROS": {"precio": 85, "stock": 50},
    "DETERGENTE": {"precio": 25, "stock": 90},
    "SERVILLETAS": {"precio": 33, "stock": 150}
}
IVA_total = 0
descuento_total = 0
total_facturado = 0
ventas_realizadas = 0




def procesar_ventas() -> None:
    producto = ""
    while producto != "FIN":
        print("-----SECCION VENTA-----")
        producto = input("Ingrese el producto que desea adquirir. Para salir, escriba 'fin': ").upper()
        if producto != "FIN":
            if producto in productos:
                try:
                    cantidad = int(input("Ingrese la cantidad que desea adquirir: "))
                    if productos[producto]["stock"] < cantidad:
                        print(
                            f"Para el producto {producto} solo hay disponibles {productos[producto]['stock']} unidades.")
                    else:
                        productos[producto]["stock"] -= cantidad
                        importe_neto = round(cantidad * productos[producto]["precio"], 2)
                        IVA = round(importe_neto * 0.21, 2)
                        bruto = importe_neto + IVA
                        if cantidad > 10:
                            descuento = round(bruto * 0.03, 2)
                            global descuento_total
                            descuento_total += descuento
                            bruto -= descuento
                        global total_facturado, IVA_total, ventas_realizadas
                        total_facturado += bruto
                        IVA_total += IVA
                        ventas_realizadas += 1
                except ValueError:
                    print("No ingresaste una cantidad correcta. Se esperaba un numero entero")
            else:
                print("El producto indicado no se encuentra disponible. Seleccione otro.")
    print("El proceso ha finalizado satisfactoriamente.")


def procesar_cierre() -> None:
    print("-----SECCION CIERRE MENSUAL-----")
    mostrar_ventas()
    mostrar_iva()
    mostrar_descuento()
    mostrar_stock()


def mostrar_ventas() -> None:
    print(f"Ventas realizadas: {ventas_realizadas}")


def mostrar_descuento() -> None:
    print(f"Descuento aplicado: $ {descuento_total}")


def mostrar_iva() -> None:
    print(f"IVA facturado: $ {IVA_total}")


def mostrar_stock() -> None:
    for item in productos:
        print(f"Producto {item}: stock = {productos[item]['stock']}")


def main():
    comando = ""
    while comando != 3:
        try:
            comando = int(input("Seleccione el numero del comando al que desea acceder: \n1.VENTA\n2.CIERRE MENSUAL\n3.SALIR"))
            if comando > 3:
                print("Comando no disponible. Los comandos disponibles son: 1.VENTA, 2.CIERRE MENSUAL y 3.SALIR")
            else:
                if comando == 1:
                    procesar_ventas()
                elif comando == 2:
                    procesar_cierre()
        except ValueError:
            print("No ingresaste un valor correcto. Se esperaba un numero entero.")
    print("Ha salido del sistema")

main()

