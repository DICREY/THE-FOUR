from config.veterinario import Veterinario
from os import system
from sys import stdout
from time import sleep
system("cls")

def main():
    try:
        while True:
            print("-------------------- Menu Veterinaria ------------------")
            print("1. Regitrar nuevo veterinario")
            print("2. Buscar veterinario")
            print("3. Actualizar veterinario")
            print("4. Eliminar veterinario")
            print("5. Salir")

            inser_veterinario = Veterinario()

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
                print("1. Registrar veterinario")
                inser_veterinario.insertar_veterinario()
                system('pause')
                system('cls')
            
            elif opcion == 2:
                system("cls")
                id = int(input("Id del veterinario a buscar: "))
                inser_veterinario.buscar_veterinario(id)
                system('pause')
                system('cls')
            
            elif opcion == 3:
                system("cls")
                id = int(input("Id del veterinario a actualizar : "))
                inser_veterinario.actualizar_veterinario(id)
                system('pause')
                system('cls')
            elif opcion == 4:
                system("cls")
                id = int(input('Ingrese el id del veterinario que desea eliminar: '))
                inser_veterinario.eliminar_veterinario(id)
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
main()