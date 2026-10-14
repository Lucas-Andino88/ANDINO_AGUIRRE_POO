class Productos:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def Crear_Productos():
        Nombre = input("Como se llama: ")
        Precio = input("Cuanto vale: ")
        return (Nombre, Precio)

    def __str__(self):
        return f"{self.nombre}: {self.precio}"