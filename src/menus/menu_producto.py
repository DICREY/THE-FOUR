from config.producto import Productos
from os import system
from sys import stdout
from time import sleep
system("cls")

def main():
    try:
        while True:
            print("-------------------- Menu Productos------------------")
            print("1. Regitrar nueva producto")
            print("2. Buscar producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Salir")            

            while True:
                try:
                    opcion = int(input("Seleccione una opcion: "))
                    break
                except ValueError:
                    print("Opción no válida")
                    
            if opcion == 5: 
                system("cls")
                break
            
        
            elif opcion == 1:
                system("cls")
                print("1. Registrar producto")
                inser_Productos = Productos()
                inser_Productos.InsertarProducto()
                system('pause')
                system('cls')
            
            elif opcion == 2:
                system("cls")
                inser_Productos = Productos()
                id = int(input("Id del producto a buscar: "))
                inser_Productos.BuscarProductoID(id)
                system('pause')
                system('cls')
            
            elif opcion == 3:
                system("cls")
                inser_Productos = Productos()
                id = int(input("Id del producto a actualizar : "))
                inser_Productos.ActualizarProducto(id)
                system('pause')
                system('cls')
            elif opcion == 4:
                system("cls")
                inser_Productos = Productos()
                id = int(input('Ingrese el id del producto que desea eliminar: '))
                inser_Productos.EliminarProducto(id)
                system('pause')
                system('cls')
            else:
                system("cls")
                print("Opcion no valida intente de nuevo")   
    except KeyboardInterrupt:
        print('El usuario ha cancelado la ejecución, por favor continue')
    except Exception as error:
        print(f'Ha ocurrido error no codificado {error}')
    finally:
        end = 'Gracias por usar nuestro programa'
        for i in end:
            print(i,end="")
            stdout.flush()
            sleep(0.1)
            
