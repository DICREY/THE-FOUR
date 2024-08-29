import menus.menu_admi
from time import sleep
from sys import stdout

def main():
    name_menu = None
    name_menu=["No deberias estar aqui :)","Propietarios","Veterinarios","Administradores","Mascotas",
            "Historial Medico","Productos","Citas Medicas","Servicios","Gracias por usar nuestro programa"]
    print("-------------------- Menu Veterinaria ------------------",
        "\n1. Propietarios\n2. Veterinarios\n3. Administradores\n4. Mascotas\n5. Historial Medico",
        "\n6. Productos\n7. Citas Medicas\n8. Servicios\n9. Salir",
        "\n--------------------------------------------------------")
    def menu(opcion):
        print(f"-------------------- Menu {name_menu[opcion]} ------------------")
        print(f"1. Regitrar nueva {name_menu[opcion]}")
        print(f"2. Buscar {name_menu[opcion]}")
        print(f"3. Actualizar {name_menu[opcion]}")
        print(f"4. Eliminar {name_menu[opcion]}")
        print("5. Salir") 

    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion != 9:
                menu(opcion) 
            elif opcion == 9:
                for i in name_menu[9]:
                    print(i,end="")
                    stdout.flush()
                    sleep(0.1)
                break
        except ValueError:
            print("Opcion Incorrecta")
            continue
        

    
main()