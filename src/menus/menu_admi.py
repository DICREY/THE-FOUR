from config.administrador import Administrador
from os import system
from sys import stdout
from time import sleep
system("cls")

def main():
    try:
        while True:
            print("-------------------- Menu Administradores ------------------")
            print("1. Regitrar nuevo administrador")
            print("2. Buscar administrador")
            print("3. Actualizar administrador")
            print("4. Eliminar administrador")
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
                print("1. Registrar administrador")
                inser_admin = Administrador()
                inser_admin.InsertarAdministrador()
                system('pause')
                system('cls')
            
            elif opcion == 2:
                system("cls")
                inser_admin = Administrador()
                id = int(input("Id del administrador buscar: "))
                inser_admin.BuscarAdministradorID(id)
                system('pause')
                system('cls')
            
            elif opcion == 3:
                system("cls")
                inser_admin = Administrador()
                id = int(input("Id del administrador a actualizar : "))
                inser_admin.ActualizarAdministrador(id)
                system('pause')
                system('cls')
            elif opcion == 4:
                system("cls")
                inser_admin = Administrador()
                id = int(input('Ingrese el id del administrador que desea eliminar: '))
                inser_admin.EliminarAdministrador(id)
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
            