from os import system
from config.historial_m import HistorialMedico

def main():
    try:
        while True:
            system("cls")
            print("-------------------- Menu Historial medico------------------")
            print("1. Regitrar historial medico")
            print("2. Buscar historial medico por id")
            print("3. Actualizar historial medico")
            print("4. Eliminar historial medico")
            print("5. Salir")
            print("--------------------------------------------------------") 
            while True:
                try:
                    opcion1 = int(input("Seleccione una opcion: "))
                    break
                except ValueError:
                    print("Opción no válida")
                    
            if opcion1 == 5: 
                system("cls")
                break
            
            elif opcion1 == 1:
                system("cls")
                HistorialMedico.insertar_historial_medico()
                system('pause')
                system('cls')

            elif opcion1 == 2:
                system("cls")
                id = input("Ingrese el id a buscar: ")
                HistorialMedico.buscar_historial_id(id)
                system('pause')
                system('cls')
            
            elif opcion1 == 3:
                system("cls")
                id = input("Ingrese el id para actualizar: ")
                HistorialMedico.actualizar_historial_medico(id)
                system('pause')
                system('cls')

            elif opcion1 == 4:
                system("cls")
                codigo = input("Ingrese el id a eliminar: ")
                HistorialMedico.eliminar_historial_medico(codigo)
                system('pause')
                system('cls')

            else:
                system("cls")
                print("Opcion no valida intente de nuevo")
    except KeyboardInterrupt:
        print('El usuario ha cancelado la ejecución, por favor continúe.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')