from mysql import connector
import os
import re
import mysql.connector.errors as errs
from config.conexion10 import BaseDatos


class Servicios:
    @classmethod
    def __init__(cls,
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
    def get_id(cls):
        return cls._id
    @classmethod
    def get_nombre(cls):
        return cls._nombre
    @classmethod
    def get_descripcion(cls):
        return cls._descripcion
    @classmethod
    def get_precio(cls):
        return cls._precio
    @classmethod
    def set_id(cls):
            while True:
                try:
                    id = input('Escriba el id del servicio: ')
                    if (1 <= len(id) <= 1000000000):
                        cls._id = id
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El servicio ha cancelado la entrada de datos.')
                continue
    @classmethod
    def set_nombre(cls):
        while True:
            try:
                nombre = input("Ingrese el nombre del servicio: ")
                cls._nombre = nombre 
                break
            except KeyboardInterrupt:
                print('El servicio ha cancelado la entrada de datos.')
                continue
    @classmethod
    def set_descripcion(cls):
        while True:
            try:
                descripcion = input("Ingrese la descripcion del servicio: ")
                cls._descripcion = descripcion
                break
            except KeyboardInterrupt:
                print('El servicio ha cancelado la entrada de datos.')
                continue
    @classmethod
    def set_precio(cls):
        while True:
            try:
                precio = int(input("Ingrese el precio del servicio: "))
                if (1 <= precio <= 1000000000):
                    cls._precio = precio
                    break
                else:
                    print('Error inserte nuevamente')
            except KeyboardInterrupt:
                print('El servicio ha cancelado la entrada de datos.')
                continue
    
           
    @classmethod
    def captura_datos(cls, omitir_id=False):
        if not omitir_id:
            cls.set_id()
        cls.set_nombre()
        cls.set_descripcion()
        cls.set_precio()
        
    @classmethod
    def insertar_servicio(cls):
        cls.captura_datos()
        conexion = BaseDatos.conectar()
        
        if conexion: 
            cursor_servicios = conexion.cursor()
            cursor_servicios.callproc("InsertarServicio", [
                cls.get_id(),
                cls.get_nombre(),
                cls.get_descripcion(),
                cls.get_precio(),
            ])
            conexion.commit()
        print("Servicio registrado correctamente...")
        if conexion:
            BaseDatos.desconectar()
            
    @classmethod
    def actualizar_servicio(cls,id):
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cls.captura_datos(omitir_id=True)
            cursor.callproc('ActualizarServicio', [
                id,
                cls.get_nombre(),
                cls.get_descripcion(),
                cls.get_precio(),
            ])
            conexion.commit()
            print("servicio actualizado correctamente")
        if conexion:
            BaseDatos.desconectar()
    
    @classmethod
    def eliminar_servicio(cls, id = None):
        if id is None:
            while True:
                id=input('que id quiere buscar: ')
                if len(id) >= 1:
                    break
                else:
                    print("Escribe un id valido")
        conexion = BaseDatos.conectar()
        try:
                cursor_servicio= conexion.cursor()
                cursor_servicio.callproc('EliminarServicio', [id])
                conexion.commit()
                cursor_servicio.close()
                print('servicio eliminado')
        except Exception as error:
                print(f'Error al eliminar el servicio: {error}. Intente de nuevo')
        finally:
                BaseDatos.desconectar()
    
    @classmethod
    def buscar_servicio_id(cls, id=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try: 
                if id is None:
                    while True:
                        id=int(input('que id quiere buscar: '))
                        if id >= 1:
                            break
                        else:
                            print("Escribe un id valido")
                servicio_encontrado = False
                cursor_servicios = conexion.cursor()
                print(f"Buscando el servicio {id}...")
                cursor_servicios.callproc("BuscarServicioID", [id])
                for busqueda in cursor_servicios.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        servicio_encontrado = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return servicio_encontrado
                    else:
                        print("servicio no encontrado. intente de nuevo")
                        print(servicio_encontrado)
                        return servicio_encontrado
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                if conexion:
                    cursor_servicios.close()
                    BaseDatos.desconectar()
    
    @classmethod
    def buscar_servicio_nombre(cls, nombre = None):
        if nombre is None:
            while True:
                nombre = input("Escribe el nombre del servicio que desea buscar: ")
                if len(nombre) > 3:
                    break
                else:
                    print("Porfavor escriba un nombre valido")
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                print(f'Buscando el servicio {nombre}...')
                cursor_servicio.callproc('BuscarServicioNombre', [nombre])
                for busqueda in cursor_servicio.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print('sercursor_servicio_encontrado')
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                if conexion:
                    cursor_servicio.close()
                    BaseDatos.desconectar()
        
                    

