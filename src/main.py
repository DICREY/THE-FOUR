from config.propietario import Propietario
from config.veterinario import Veterinario
from config.administrador import Administrador
from time import sleep
from sys import stdout
from os import system

def main():
    name_menu=["No deberias estar aqui :)","Propietarios","Veterinarios","Administradores","Mascotas",
            "Historial Medico","Productos","Citas Medicas","Servicios","Gracias por usar nuestro programa"]
    print("-------------------- Menu Veterinaria ------------------",
        "\n1. Propietarios\n2. Veterinarios\n3. Administradores\n4. Mascotas\n5. Historial Medico",
        "\n6. Productos\n7. Citas Medicas\n8. Servicios\n9. Salir",
        "\n--------------------------------------------------------")
    def menu(opcion):
        diccionario = {
            "Propietarios":[ Propietario().buscar_propietario],
            "Veterinarios":[],
            "Administradores": [ Administrador().InsertarAdministrador , Administrador().BuscarAdministradorID ],
            "Mascotas":[],
            "HistorialMedico":[],
            "Productos":[],
            "CitasMedicas":[],
            "Servicios":[],
        }
        try:
            system("cls")
            print(f"-------------------- Menu {name_menu[opcion]} ------------------")
            print(f"1. Regitrar nueva {name_menu[opcion]}")
            print(f"2. Buscar {name_menu[opcion]}")
            print(f"3. Actualizar {name_menu[opcion]}")
            print(f"4. Eliminar {name_menu[opcion]}")
            print("5. Salir") 

            while True:
                while True:
                    try:
                        opcion1 = int(input("Seleccione una opcion: "))
                        break
                    except ValueError:
                        print("Opción no válida")
                        
                if opcion1 == 5: 
                    system("cls")
                    break
                
                elif opcion1 == 2:
                    system("cls")
                    diccionario[name_menu[opcion][1]]()
                    system('pause')
                    system('cls')
                
                else:
                    system("cls")
                    print("Opcion no valida intente de nuevo")
        except KeyboardInterrupt:
            print('El usuario ha cancelado la ejecución, por favor continue')
        except Exception as error:
            print(f'Ha ocurrido error no codificado {error}')
            
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion != 9:
                menu(opcion) 
            elif opcion == 9:
                system("cls")
                for i in name_menu[9]:
                    print(i,end="")
                    stdout.flush()
                    sleep(0.1)
                break
        except ValueError:
            print("Opcion Incorrecta")
            continue
    
main()