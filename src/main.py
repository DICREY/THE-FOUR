from config.propietario import Propietario
from config.veterinario import Veterinario
from config.administrador import Administrador
from config.mascota import Mascota
from config.historial_m import HistorialMedico
from config.producto import Productos
from config.citas import Cita
from config.servicios import Servicios
from time import sleep
from sys import stdout
from os import system
from menus import historial_m

def main():
    name_menu=["No deberias estar aqui :)","Propietarios","Veterinarios","Administradores","Mascotas",
            "Historial Medico","Productos","Citas Medicas","Servicios","Gracias por usar nuestro programa"]
    def menu(opcion):
        diccionario = {
            "Propietarios":[ Propietario.insertar_propietario, Propietario.buscar_propietario,Propietario.buscar_propietario_nombre, Propietario.actualizar_propietario, Propietario.eliminar_propietario],
            "Veterinarios":[ Veterinario.insertar_veterinario, Veterinario.buscar_veterinario_id, Veterinario.buscar_veterinario_nombre, Veterinario.actualizar_veterinario, Veterinario.eliminar_veterinario ],
            "Administradores": [ Administrador.insertar_administrador , Administrador.buscar_administrador_id, Administrador.buscar_administrador_nombre, Administrador.actualizar_administrador, Administrador.eliminar_administrador ],
            "Mascotas":[Mascota.insertar_mascota, Mascota.buscar_mascota_id, Mascota.buscar_mascota_nombre, Mascota.actualizar_mascota, Mascota.eliminar_mascota],
            "Historial Medico":[HistorialMedico.insertar_historial_medico, HistorialMedico.buscar_historial_id, HistorialMedico.buscar_historiales_medicos, HistorialMedico.actualizar_historial_medico, HistorialMedico.eliminar_historial_medico],
            "Productos":[Productos.insertar_producto, Productos.buscar_producto_id, Productos.buscar_producto_nombre, Productos.actualizar_producto, Productos.eliminar_producto],
            "Citas Medicas":[Cita.insertar_cita, Cita.buscar_cita_mascota, Cita.buscar_cita_fecha, Cita, Cita.eliminar_cita],
            "Servicios":[Servicios.insertar_servicio, Servicios.buscar_servicio_id, Servicios.buscar_servicio_nombre, Servicios.actualizar_servicio, Servicios.eliminar_servicio],
        }
        try:
            if name_menu[5]:
                historial_m.main()
            else:
                while True:
                    system("cls")
                    print(f"-------------------- Menu {name_menu[opcion]} ------------------")
                    print(f"1. Regitrar {name_menu[opcion]}")
                    print(f"2. Buscar {name_menu[opcion]} por id")
                    print(f"3. Buscar {name_menu[opcion]} por nombre")
                    print(f"4. Actualizar {name_menu[opcion]}")
                    print(f"5. Eliminar {name_menu[opcion]}")
                    print("6. Salir")
                    print("--------------------------------------------------------") 
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
                        diccionario[name_menu[opcion]][2](name)
                        system('pause')
                        system('cls')

                    elif opcion1 == 4:
                        system("cls")
                        codigo = input("Ingrese el id a actualizar: ")
                        diccionario[name_menu[opcion]][3](codigo)
                        system('pause')
                        system('cls')

                    elif opcion1 == 5:
                        system("cls")
                        codigo = input("Ingrese el id a eliminar: ")
                        diccionario[name_menu[opcion]][4](codigo)
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
            if opcion <= 0:
                system("cls")
                system("color 04")
                print("Escribe una opcion valida")
                sleep(0.5)
                system("cls")
            elif opcion != 9:
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