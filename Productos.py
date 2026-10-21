class Productos:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    alimentos = [
        ("Sandwich", 3000),
        ("Quepi", 5000)
        ]

    def Crear_Productos():
        nombre = input("Como se llama: ")
        precio = input("Cuanto vale: ")
        Productos.alimentos.append((nombre, precio))

    def Mostrar_Alimentos():
        for x in Productos.alimentos:
            print(x)

    def __str__(self):
        return f"{self.nombre}: {self.precio}"