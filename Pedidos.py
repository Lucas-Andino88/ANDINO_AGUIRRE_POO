from Productos import Productos

class Pedidos:
    
    def __init__(self):
        pass
    transpadano = 1
    def Crear_Pedido(self):
        Orden = []
        transpadano = 1
        print("===============================") 
        print("   ¿Que le gustaría ordenar?")  
        print("===============================") 
        print(Productos.Mostrar_Alimentos())
        while transpadano:
            print("Ingrese 0 para salir")
            if input() == "0":
                transpadano = 0
                break
            else:
                añadir = input("Ingrese el nombre del producto que desea ordenar: ")
                for x in Productos.alimentos:
                    if x[0] == añadir:
                     Orden.append(x)
                print("Su pedido es actual es: ", Orden)
        Quitar = input("Ingrese el nombre del producto que desea quitar de la orden final: ")
        for x in Orden:
            if x[0] == Quitar:
                Orden.remove(x) 
        print("Su pedido es actual es: ", Orden)
        
        def Calcular_Precio_Total():
            Precio_Final = [0]
            for x in Productos.alimentos: 
                Precio_Final[0] += Productos.alimentos[1]
            if Precio_Final[0] <= "0":
              print("El precio final no puede ser negativo")
            else:
              print(Precio_Final[0])

        


        
