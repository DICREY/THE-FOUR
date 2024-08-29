import menus.menu_admi
from time import sleep
from sys import stdout

def main():
    name_menu = None
    print("-------------------- Menu Veterinaria ------------------",
        "\n1. Propietarios\n2. Veterinarios\n3. Administradores\n4. Mascotas\n5. Historial Medico",
        "\n6. Productos\n7. Citas Medicas\n8. Servicios\n9. Salir",
        "\n--------------------------------------------------------")
    def menu(name_menu):
        print(f"-------------------- Menu {name_menu} ------------------")
        print(f"1. Regitrar nueva {name_menu}")
        print(f"2. Buscar {name_menu}")
        print(f"3. Actualizar {name_menu}")
        print(f"4. Eliminar {name_menu}")
        print("5. Salir") 

    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                name_menu = "Propietarios"
                menu(name_menu)
            if opcion == 2:
                name_menu = "Veterinarios"
                menu(name_menu)
            if opcion == 3:
                name_menu = "Administradores"
                menu(name_menu)
            if opcion == 4:
                name_menu = "Mascotas"
                menu(name_menu)
            if opcion == 5:
                name_menu = "Historial Medico"
                menu(name_menu)
            if opcion == 6:
                name_menu = "Productos"
                menu(name_menu)
            if opcion == 7:
                name_menu = "Citas Medicas"
                menu(name_menu)
            if opcion == 8:
                name_menu = "Servicios"
                menu(name_menu)
            if opcion == 9:
                for i in "Gracias por usar nuestro programa":
                    print(i,end="")
                    stdout.flush()
                    sleep(0.1)
                
        except ValueError:
            print("Opcion Incorrecta")
            continue
        

    
main()