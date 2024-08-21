from mysql import connector
import mysql.connector.errors as errs

class Servicios:
    def __init__(
            self,
            id: int = None,
            nombre: str = None,
            descripcion: str = None,
            precio: float = None
            ):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
    
    def set_id(self):
        while True:
            try:
                id = int(input('Escriba el id del producto: '))
                if (1 <= id <= 1000000000):
                    self._id = id
                    break
                else:
                    print('El número debe estar entre 3 y 100000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_id(self):
        return self._id