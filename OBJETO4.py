class ComidasEspeciales(Productos):

    def __init__(self, nombre, precio, tipo_comida):
        super().__init__(nombre, precio)
        self.tipo_comida = tipo_comida

    def Lista_Comidas(self):
        comidas = [
            "Comidas celíacas",
            "Comidas vegetarianas",
            "Comidas sin gluten"
        ]
        return comidas