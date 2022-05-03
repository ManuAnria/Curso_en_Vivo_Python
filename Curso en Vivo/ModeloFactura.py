class ModeloFactura:

    def __int__(self, items: dict)
        self.items = items


    def listar_items(self) -> None:
        for item in self.items:
            valores = self.items[item]
            cantidad = valores["cantidad"]
            importe = Calculadora.multiplicar(cantidad, valores["precio"])
            print(f"{valores['codigo']}: cantidad: {cantidad}; precio: {importe}")