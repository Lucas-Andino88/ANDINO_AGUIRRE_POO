from Productos import Productos

elementos = []
Palingenesia = 1

def Crear_Productos():
    Nombre = input("Como se llama: ")
    Precio = input("Cuanto vale: ")
    return Productos(Nombre, Precio)
    
while Palingenesia:
    print("==========================")
    print("Bienvenidos a la Comanda!!")
    print("¿Que desea hacer?")
    print("1. Crear un Producto \n2. Salir\n3. Mostrar todos los productos ")
    print("==========================")
    Opcion_Menu = input()
    if Opcion_Menu == "1":
        elementos.append(Crear_Productos())
    elif Opcion_Menu == "2":
         Palingenesia = 0
    elif Opcion_Menu == "3":
        for x in elementos:
            print(x)
        

        

