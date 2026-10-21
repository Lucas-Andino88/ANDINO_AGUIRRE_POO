from Productos import Productos

class Pedidos:
    
    def __init__(self):
        pass

    
    def Crear_Pedido(self):
        Orden = []
        transpadano = 1
        taxidermia = 1
        print("===============================") 
        print("   ¿Que le gustaría ordenar?")  
        print("===============================") 
        print(Productos.Mostrar_Alimentos())
        while transpadano:
            print("Ingrese exit para salir")
            if input() == "exit":
                transpadano = 0
                break
            elif input() != "exit":
                añadir = input("Ingrese el nombre del producto que desea ordenar: ")
                for x in Productos.alimentos:
                    if x[0] == añadir:
                     Orden.append(x)
                    print(Productos.Mostrar_Alimentos())
                    print("Su pedido es actual es: ", Orden)
        while taxidermia:
            Quitar = input("Ingrese el nombre del producto que desea quitar de la orden final: ")
            for x in Orden:
                if x[0] == Quitar:
                    Orden.remove(x) 
            print("Su pedido es actual es: ", Orden)
            
        print("Su pedido es actual es: ", Orden, "y cuesta: ", self.Calcular_Precio_Total())

    def Calcular_Precio_Total(self):
                Precio_Final = 0
                for x in Productos.alimentos: 
                    Precio_Final += x[1]
                if Precio_Final <= 0:
                    return "El precio final no puede ser negativo"
                else:
                    return Precio_Final   