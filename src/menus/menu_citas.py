from config.citas import Cita 
from os import system
from sys import stdout
from time import sleep

system("cls")

def main():
    try:
        while True:
            print("-------------------- Menu Citas------------------")
            print("1. Registrar nueva cita")
            print("2. Buscar cita por fecha")
            print("3. Buscar cita por mascota")
            print("4. Eliminar cita")
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
                print("1. Registrar nueva cita")
                # Invocamos el método de la clase Cita
                Cita.insertar_cita()  
                system('pause')
                system('cls')
            
            elif opcion == 2:
                system("cls")
                print("2. Buscar cita por fecha")
                Cita.buscar_cita_fecha()  # Método para buscar cita por fecha
                system('pause')
                system('cls')

            elif opcion == 3:
                system("cls")
                print("3. Buscar cita por mascota")
                Cita.buscar_cita_mascota()  # Método para buscar cita por mascota
                system('pause')
                system('cls')
            
            elif opcion == 4:
                system("cls")
                print("4. Eliminar cita")
                Cita.eliminar_cita()  # Método para eliminar la cita
                system('pause')
                system('cls')

            else:
                system("cls")
                print("Opción no válida, intente de nuevo")   
    except KeyboardInterrupt:
        print('El usuario ha cancelado la ejecución, por favor continúe.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')
    finally:
        end = 'Gracias por usar nuestro programa'
        for i in end:
            print(i, end="")
            stdout.flush()
            sleep(0.1)
