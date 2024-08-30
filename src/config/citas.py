from conexion10 import BaseDatos
from datetime import datetime
import re
from os import system

class Cita:

    @classmethod
    def __init__(cls,
                 id: str = None,
                 fecha: str = None,
                 hora: str = None,
                 id_servicio: str = None,
                 id_veterinario: str = None,
                 id_mascota: str = None,
                 estado: str = None):
        cls._id = id
        cls._fecha = fecha
        cls._hora = hora
        cls._id_veterinario = id_veterinario
        cls._id_servicio = id_servicio
        cls._id_mascota = id_mascota
        cls._estado = estado
    

    @classmethod
    def get_id(cls):
        return cls._id
    

    @classmethod
    def get_fecha(cls):
        return cls._fecha
    
    
    @classmethod
    def get_hora(cls):
        return cls._hora
    

    @classmethod
    def get_id_servicio(cls):
        return cls._id_servicio


    @classmethod
    def get_id_mascota(cls):
        return cls._id_mascota


    @classmethod
    def get_estado(cls):
        return cls._estado


    @classmethod
    def get_id_veterinario(cls):
        return cls._id_veterinario

    @classmethod
    def set_fecha(cls):
        while True:
            try:
                patron = r'^\d{4}-\d{2}-\d{2}$'
                fecha = input("Ingrese la fecha en formato YYYY-MM-DD: ")
                
                if re.match(patron, fecha):
                    try:
                        datetime.strptime(fecha, '%Y-%m-%d')
                        cls._fecha = fecha
                        break
                    except ValueError:
                        print("Fecha inválida, intente nuevamente.")
                else:
                    print("Formato de fecha incorrecto, intente nuevamente.")
                
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                break

    @classmethod
    def set_id(cls):
            while True:
                try:
                    codigo = input('Escriba el codigo de la cita: ')
                    if (1 <= len(codigo) <= 1000000000):
                        cls._id = codigo
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue

    
    @classmethod
    def set_hora(cls):
        while True:
            try:
                hora= input("Escribe la hora de la cita: ")
                if (1 < len(hora) <= 200):
                    cls._hora = hora
                    break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')


    @classmethod
    def set_id_servicio(cls):
        while True:
            try:
                id = input('Escriba el id del servicio: ')
                if (1 <= len(id) <= 1000000000):
                    cls._id_servicio = id
                    break
                else:
                    print('El número debe estar entre 3 y 100000000')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    @classmethod
    def set_id_veterinario(cls):
        while True:
            try:
                id = input('Escriba el id del veterinario: ')
                if (1 <= len(id) <= 1000000000):
                    cls._id_veterinario = id
                    break
                else:
                    print('El número debe estar entre 3 y 100000000')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue
    


    @classmethod
    def set_id_mascota(cls):
             while True:
                try:
                    id_mascota = input('Escriba el código de la mascota: ')
                    if (1 <= len(id_mascota) <= 1000000000):
                        cls._id_mascota = id_mascota
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
             
    @classmethod
    def set_estado(cls):
        while True:
            try:
                estados=("Pendiente","En espera","Cancelada","Rechazada","Realizada")
                usuario = input("Escribe el estado de la cita: ").capitalize()
                if usuario in estados:
                    cls._estado = usuario
                    break
                else:
                    print("Estado no valido")
            except KeyboardInterrupt:
                print("El usuario ha cancelado la entrada de datos")

    @classmethod
    def capturar_datos(cls):
        cls.set_id()
        cls.set_fecha()
        cls.set_hora()
        cls.set_id_servicio()
        cls.set_id_veterinario()
        cls.set_id_mascota()
        cls.set_estado()


    @classmethod
    def insertar_cita(cls):
        cls.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion: 
            cursor_productos = conexion.cursor()
            cursor_productos.callproc("InsertarCita", [
                cls.get_id(),
                cls.get_fecha(),
                cls.get_hora(),
                cls.get_id_servicio(),
                cls.get_id_veterinario(),
                cls.get_id_mascota(),
                cls.get_estado()
            ])
            conexion.commit()
        print("Cita registrada correctamente...")
        if conexion:
            BaseDatos.desconectar()
    
    @classmethod
    def buscar_cita_fecha(cls, fecha=None):
        if fecha is None:
            while True:
                try:
                    patron = r'^\d{4}-\d{2}-\d{2}$'
                    fecha = input("Ingrese la fecha a buscar en formato YYYY-MM-DD: ")
                    if re.match(patron, fecha):
                        try:
                            datetime.strptime(fecha, '%Y-%m-%d')
                            break
                        except ValueError:
                            print("Fecha inválida, intente nuevamente.")
                    else:
                        print("Formato de fecha incorrecto, intente nuevamente.")
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                    break 
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                system('cls')
                cursor_cita = conexion.cursor()
                print(f'Buscando Cita del {fecha}...')
                cursor_cita.callproc('BuscarCitaPorFecha', [fecha])
                for busqueda in cursor_cita.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                    else:
                        print('Cita no encontrada. Intente de nuevo.')
            except Exception as e:
                print(f'Error al buscar la cita: {e}')
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()

    @classmethod
    def buscar_cita_mascota(cls, id_mascota = None):
        if id_mascota is None:
            id_mascota = input("Escribe el id de la mascota para buscar sus citas: ")
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                system('cls')
                cursor_cita = conexion.cursor()
                print(f'Buscando Cita de la mascota {id_mascota}...')
                cursor_cita.callproc('BuscarCitaPorMascota', [id_mascota])
                for busqueda in cursor_cita.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                    else:
                        print('Cita no encontrada. Intente de nuevo.')
            except Exception as e:
                print(f'Error al buscar la cita: {e}')
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()
    

    @classmethod
    def eliminar_cita(cls, id = None):
        conexion = BaseDatos.conectar()
        if id is None:
            id = input("Escribe el id de la cita a eliminar: ")
        try:
            cursor_mascota = conexion.cursor()
            cursor_mascota.callproc('EliminarCitaPorCodigo', [id])
            conexion.commit()
            cursor_mascota.close()
            print('Cita eliminada')
        except Exception as error:
            print(f'Error al eliminar la cita: {error}. Intente de nuevo')
        finally:
            BaseDatos.desconectar()