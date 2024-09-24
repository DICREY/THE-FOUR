from config.usuario import Usuario
from datetime import datetime
from config.conexion10 import BaseDatos

class Propietario(Usuario):
    @classmethod
    def __init__(cls,
        barrio: str = None
    ):
        cls.__barrio = barrio
    
    @classmethod
    def set_barrio(cls):
        while True:
            try:
                barrio=input('Ingrese el barrio del usuario: ')
                if len(barrio) > 4 and len(barrio) < 50 :
                    cls.__barrio = barrio
                    break
                else:
                    print('El barrio no cumple con los requisitos')
            except KeyboardInterrupt:
                print('Operación cancelada por el usuario')

    @classmethod
    def get_barrio(cls):
        return cls.__barrio

    @classmethod
    def capturar_datos_propietarios(cls):
        cls.capturar_datos(),
        cls.set_barrio()

    @classmethod
    def insertar_propietario(cls):
        cls.capturar_datos_propietarios()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('InsertarPropietario', [
                cls.get_codigo(),
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_email(),
                cls.get_contrasenna(),
                cls.get_barrio()
            ])
            conexion.commit()
        print("Propietario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()

    @classmethod
    def actualizar_propietario(cls,name = None):
        cls.capturar_datos_propietarios()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('ActualizarPropietario', [
                name,
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_email(),
                cls.get_contrasenna(),
                cls.get_barrio()
            ])
            conexion.commit()
            print("Propietario actualizado correctamente")
        if conexion:
            BaseDatos.desconectar()

    @classmethod
    def eliminar_propietario(cls,codigo = None):
        conexion = BaseDatos.conectar()
        try:
                cursor_propietario= conexion.cursor()
                cursor_propietario.callproc('EliminarPropietario', [codigo])
                conexion.commit()
                cursor_propietario.close()
                print('propietario eliminado')
        except Exception as error:
                print(f'Error al eliminar el propietario: {error}. Intente de nuevo')
        finally:
                BaseDatos.desconectar()

    @classmethod
    def buscar_propietario(cls,codigo = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario_encontrada = False
                cursor_propietario = conexion.cursor()
                print(f'Buscando al propietario {codigo}...')
                cursor_propietario.callproc('BuscarPropietarioID', [codigo])
                for busqueda in cursor_propietario.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cursor_propietario_encontrada = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return cursor_propietario_encontrada
                    else:
                        print('propietario no encontrada. Intente de nuevo.')
                        print(cursor_propietario_encontrada)
                        return cursor_propietario_encontrada
            except Exception as e:
                print(f'Error al buscar la propietario: {e}')
            finally:
                if conexion:
                    cursor_propietario.close()
                    BaseDatos.desconectar()
    
    @classmethod
    def buscar_propietario_nombre(cls,name = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                propietario_encontrado = False
                cursor_propietario = conexion.cursor()
                print(f'Buscando propietario...')
                cursor_propietario.callproc('BuscarPropietarioNombre',[name])
                for busqueda in cursor_propietario.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return propietario_encontrado
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(propietario_encontrado)
                        return propietario_encontrado
            except Exception as e:
                print(f'Error al buscar propietario: {e}')
            finally:
                if conexion:
                    cursor_propietario.close()
                    BaseDatos.desconectar()
    
    
    