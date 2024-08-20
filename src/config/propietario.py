from usuario import Usuario
import re
from config.usuario import Usuario
from datetime import datetime
from config.conexion10 import BaseDatos

class Propietario(Usuario):
    def __init__(self,
        barrio: str = None
    ):
        self.__barrio = barrio
    
    def set_barrio(self):
        while True:
            try:
                barrio=input('Ingrese la barrio del usuario: ')
                if len(barrio)>4 and len(barrio)<50 :
                    self.__barrio = barrio
                    break
                else:
                    print('El barrio no cumple con los requisitos (deve tener una longitud mayor a 4 y menor a 50)')
            except KeyboardInterrupt:
                print('Operación cancelada por el usuario')

    def get_barrio(self):
        return self._barrio

    def capturar_datos_propietarios(self):
        self.capturar_datos(),
        self.set_barrio()

    def insertar_propietario(self):
        self.capturar_datosV()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('InsertarPropietario', [
                self.get_codigo(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_email(),
                self.get_contrasenna(),
                self.get_barrio()
            ])
            conexion.commit()
        print("Propietario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()

    def actualizar_propietario(self):
        self.capturar_datosV()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('ActualizarPropietario', [
                self.get_codigo(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_email(),
                self.get_contrasenna(),
                self.get_barrio()
            ])
            conexion.commit()
            print("Propietario actualizado correctamente")
        if conexion:
            BaseDatos.desconectar()

    def eliminar_propietario(self):
        conexion = BaseDatos.conectar()
        id_usuario=int(input('ingrese el id del propietario que desea eliminar: '))
        try:
                cursor_propietario= conexion.cursor()
                cursor_propietario.callproc('EliminarPropietario', [id_usuario])
                conexion.commit()
                cursor_propietario.close()
                print('propietario eliminado')
        except Exception as error:
                print(f'Error al eliminar el propietario: {error}. Intente de nuevo')
        finally:
                BaseDatos.desconectar()

    def buscar_propietario(self):
        conexion = BaseDatos.conectar()
        id_usuario=int(input('ingrese el id del veterianrio a buscar: '))
        if conexion:
            try:
                cursor_propietario_encontrada = False
                cursor_propietario = conexion.cursor()
                print(f'Buscando al propietario {id_usuario}...')
                cursor_propietario.callproc('BuscarPropietarioID', [id_usuario])
                for busqueda in cursor_propietario.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cursor_propietario_encontrada = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return cursor_propietario_encontrada
                    else:
                        print('propietariocursor_propietario no encontrada. Intente de nuevo.')
                        print(cursor_propietario_encontrada)
                        return cursor_propietario_encontrada
            except Exception as e:
                print(f'Error al buscar la propietario: {e}')
            finally:
                if conexion:
                    cursor_propietario.close()
                    BaseDatos.desconectar()