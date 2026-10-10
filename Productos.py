class Productos:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

#    "Menú" == {
 #       "Ñoquis" : "$10.000",
  #      "Spaghetti" : "$12.000",
   #     "Pollo al horno con papas" : "$17.000",
    #    "Shawarma" : "$15.000",
     #       } 
    def Crear_Productos(self):
        Nombre = input()
        Precio = input()
        Menu = Nombre, Precio

    def __str__(self):
        return f"{self.nombre}: {self.precio}"