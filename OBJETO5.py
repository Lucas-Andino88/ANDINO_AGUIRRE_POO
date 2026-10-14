class Bebidas(Productos):

    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def Lista_Bebidas(self):
        bebidas = [
            ("Agua", ["500 ml", "1 litro", "2 litros"]),
            ("Gaseosa", ["500 ml", "1 litro", "2 litros"]),
            ("Jugo", ["500 ml", "1 litro"])
        ]
        return bebidas