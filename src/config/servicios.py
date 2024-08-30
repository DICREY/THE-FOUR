from mysql import connector
import mysql.connector.errors as errs

class Servicios:
    @classmethod
    def __init__(
            cls,
            id: str = None,
            nombre: str = None,
            descripcion: str = None,
            precio: float = None
            ):
        cls._id = id
        cls._nombre = nombre
        cls._descripcion = descripcion
        cls._precio = precio
    
    @classmethod
    def set_id(cls):
        while True:
            try:
                id = input('Escriba el id del producto: ')
                if (1 <= len(id) <= 1000000000):
                    cls._id = id
                    break
                else:
                    print('El número debe estar entre 3 y 100000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    @classmethod
    def get_id(cls):
        return cls._id