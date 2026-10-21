from Productos import Productos
from OBJETO4 import ComidasEspeciales
from OBJETO5 import Bebidas
from Pedidos import Pedidos 

Palingenesia = 1

while Palingenesia:
    print("==========================")
    print("Bienvenidos a la Comanda!!")
    print("¿Que desea hacer?")
    print("1. Crear un Producto \n2. Mostrar todos los productos \n3. Crear un pedido \n4. Salir ")
    print("==========================")
    Opcion_Menu = input()
    if Opcion_Menu == "1":
        Productos.Crear_Productos()
    elif Opcion_Menu == "2":
        for x in Productos.alimentos:
            print(x)
    elif Opcion_Menu == "3":
         pedido = Pedidos()
         pedido.Crear_Pedido()
    elif Opcion_Menu == "4": 
         Palingenesia = 0
 