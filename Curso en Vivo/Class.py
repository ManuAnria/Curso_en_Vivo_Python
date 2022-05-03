class perro:
    cantidad_patas = 4          #Atributo de clase (STATIC). Comun para todas las instancias de clase
    especie = "Mamifero"        #Atributo de clase (STATIC). Comun para todas las instancias de clase

    def __init__(self, name , age,color): #init = Constructor
        self.name = name #Atributo de instancia. Propio de cada instancia
        self.age = age
        self.color = color

boby = perro("Boby", 7, "white")    #Instanciando objetos con diferentes estados


class Factura:
    iva = 1.21

    def __init__(self, numero: str, items: dict, codigo_cliente: str):
        self.numero = numero
        self.items = items
        self.codigo_cliente = codigo_cliente

    def calcular_precio_item(self, codigo_item: int) -> float:
        try:
            item = self.items[codigo_item]
            return Calculadora.multiplicar(item["precio"], item["cantidad"])
        except KeyError:
            print(f"El item con codigo {codigo_item} no existe.")

    @staticmethod
    def obtener_iva():
        return Factura.iva

factura = Factura("000-123-452", {
    1:{"codigo": "01", "cantidad": 12,"precio": 150},
    2:{"codigo": "02", "cantidad": 10,"precio": 15.50},
    }, "0048")

factura.listar_items()
print(f"El precio del item 1 es {factura.calcular_precio_item(1)}")
print(Factura.obtener_iva())