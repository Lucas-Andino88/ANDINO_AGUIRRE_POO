from Productos import Productos
from OBJETO4 import ComidasEspeciales
from OBJETO5 import Bebidas
from Pedidos import Pedidos 
producto = [("Sandwich", 3000), ("Quepi", 5000)]
Palingenesia = 1
Precio_Total = 0

while Palingenesia:
    print("==========================")
    print("Bienvenidos a la Comanda!!")
    print("¿Que desea hacer?")
    print("1. Crear un Producto \n2. Mostrar todos los productos \n3. Crear un pedido \n4. Salir ")
    print("==========================")
    Opcion_Menu = input()
    if Opcion_Menu == "1":
        producto.append(Productos.Crear_Productos())
    elif Opcion_Menu == "2":
        for x in producto:
            print(x)
    elif Opcion_Menu == "3":
         print(Pedidos.Crear_Pedido())

         
         for x in producto: 
          Precio_Total += producto[1]
         print(Precio_Total)
    elif Opcion_Menu == "4": 
         Palingenesia = 0


 

        

