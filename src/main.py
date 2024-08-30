from config.propietario import Propietario
from config.veterinario import Veterinario
from config.administrador import Administrador
from time import sleep
from sys import stdout
from os import system

def main():
    name_menu=["No deberias estar aqui :)","Propietarios","Veterinarios","Administradores","Mascotas",
            "Historial Medico","Productos","Citas Medicas","Servicios","Gracias por usar nuestro programa"]
    def menu(opcion):
        diccionario = {
            "Propietarios":[ Propietario().insertar_propietario, Propietario().buscar_propietario, Propietario.actualizar_propietario, Propietario.eliminar_propietario, Propietario.buscar_propietario_nombre],
            "Veterinarios":[ Veterinario.insertar_veterinario, Veterinario.buscar_veterinario_id, Veterinario.actualizar_veterinario, Veterinario.eliminar_veterinario, Veterinario.buscar_veterinario_nombre ],
            "Administradores": [ Administrador().insertar_administrador , Administrador().buscar_administrador_id, Administrador.actualizar_administrador, Administrador.eliminar_administrador,Administrador.buscar_administrador_nombre ],
            "Mascotas":[],
            "HistorialMedico":[],
            "Productos":[],
            "CitasMedicas":[],
            "Servicios":[],
        }
        try:
            while True:
                system("cls")
                print(f"-------------------- Menu {name_menu[opcion]} ------------------")
                print(f"1. Regitrar {name_menu[opcion]}")
                print(f"2. Buscar {name_menu[opcion]} por id")
                print(f"3. Buscar {name_menu[opcion]} por nombre")
                print(f"4. Actualizar {name_menu[opcion]}")
                print(f"5. Eliminar {name_menu[opcion]}")
                print("6. Salir") 

                while True:
                    try:
                        opcion1 = int(input("Seleccione una opcion: "))
                        break
                    except ValueError:
                        print("Opción no válida")
                        
                if opcion1 == 6: 
                    system("cls")
                    break
                
                elif opcion1 == 1:
                    system("cls")
                    diccionario[name_menu[opcion]][0]()
                    system('pause')
                    system('cls')

                elif opcion1 == 2:
                    system("cls")
                    codigo = input("Ingrese el id a buscar: ")
                    diccionario[name_menu[opcion]][1](codigo)
                    system('pause')
                    system('cls')
                
                elif opcion1 == 3:
                    system("cls")
                    name = input("Ingrese el nombre para buscar: ")
                    diccionario[name_menu[opcion]][4](name)
                    system('pause')
                    system('cls')

                elif opcion1 == 4:
                    system("cls")
                    codigo = input("Ingrese el id a buscar: ")
                    diccionario[name_menu[opcion]][2](codigo)
                    system('pause')
                    system('cls')

                elif opcion1 == 5:
                    system("cls")
                    codigo = input("Ingrese el id a eliminar: ")
                    diccionario[name_menu[opcion]][3](codigo)
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
            print("-------------------- Menu Veterinaria ------------------",
            "\n1. Propietarios\n2. Veterinarios\n3. Administradores\n4. Mascotas\n5. Historial Medico",
            "\n6. Productos\n7. Citas Medicas\n8. Servicios\n9. Salir",
            "\n--------------------------------------------------------")
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