from Productos import Productos

class Pedidos:
    
    def __init__(self):
        pass
        
    def Crear_Pedido(self):
        Orden = []
        print("===============================") 
        print("   ¿Que le gustaría ordenar?")  
        print("===============================") 
        print(Productos.Mostrar_Alimentos())
    
        def Calcular_Precio_Total():
            Precio_Final = [0]
            for x in Productos.alimentos: 
                Precio_Final[0] += Productos.alimentos[1]
            if Precio_Final[0] <= "0":
              print("El precio final no puede ser negativo")
            else:
              print(Precio_Final[0])

        


        
