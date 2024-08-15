from mascota import Mascota
from os import system

def main():
    try:
        while True:
            print("-------------------- Menu Veterinaria ------------------")
            
            print("1. Regitrar nueva mascota")
            print("2. Buscar mascota")
            print("3. Actualiza mascota")
            print("4. Eliminar mascota")
            print("5. Salir")            

            while True:
                try:
                    opcion = int ("Seleccione una opcion: ")
                    break
                except ValueError:
                    print("Opción no válida")
                    
            if opcion == 5: 
                print("")
                break
            
            elif opcion == 1:
                system("cls")
                print("1. Registrar Mascota")
                
                inser_mascota = Mascota()
                inser_mascota.registrar_mascota
            
            elif opcion == 2:
                system("cls")
                inser_mascota = Mascota()
                codigo_mascota = int(input("Codigo de mascota a buscar"))
                inser_mascota.buscar_mascota(codigo_mascota)
            
            elif opcion == 3:
                system("cls")
                inser_mascota = Mascota()
                codigo_mascota = int(input("Codigo de mascota a actualiza"))
            
            elif opcion == 4:
                system("cls")
                print("")
                
            else:
                system("cls")
                print("Opcion no valida intente de nuevo")   
    except KeyboardInterrupt:
        print('El usuario ha cancelado la ejecución, por favor continue')
    except Exception as error:
        print(f'Ha ocurrido error no codificado {error}')
    finally:
        print('Intente de nuevo')

if __name__ == "__main__":
    main()       