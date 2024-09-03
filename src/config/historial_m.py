import os 
import re
from config.conexion10 import BaseDatos
from datetime import datetime
from os import system

class HistorialMedico():
    
    @classmethod
    def __init__(cls,
                 id: int = None,
                 fecha: datetime = None,
                 descripcion: str = None,
                 tratamiento: str = None,
                 id_veterinario: int = None,
                 id_mascota: int = None
                 ):
        
        cls.__id = id
        cls.__fecha = fecha
        cls.__descripcion = descripcion
        cls.__tratemiento = tratamiento
        cls.__id_veterinario = id_veterinario
        cls.__id_mascota = id_mascota
        
    @classmethod
    def set_id(cls):
             while True:
                try:
                    id = int(input('Escriba el id del historial: '))
                    if (1 <= id<= 1000000000):
                        cls.__id = id
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El himostrar_historial ha cancelado la entrada de datos.')
                continue
    @classmethod        
    def get_id(cls):
        return cls.__id
    
    @classmethod
    def set_fecha(cls):
        while True:
            try:
                patron = r'^\d{4}-\d{2}-\d{2}$'
                fecha = input("Ingrese la fecha en formato YYYY-MM-DD: ")
                
                if re.match(patron, fecha):
                    try:
                        datetime.strptime(fecha, '%Y-%m-%d')
                        cls.fecha = fecha
                        break
                    except ValueError:
                        print("Fecha inválida, intente nuevamente.")
                else:
                    print("Formato de fecha incorrecto, intente nuevamente.")
                
            except KeyboardInterrupt:
                print('El himostrar_historial ha cancelado la entrada de datos.')
                break
    @classmethod        
    def get_fecha(cls):
        return cls.__fecha
    
    
    @classmethod
    def set_descripcion(cls):
        try:
            input("Ingrese la descripcion de la mascota")
        except KeyboardInterrupt:
            print("El himostrar_historial ha cancelado la entrada de texto ")
    @classmethod       
    def get_descripcion(cls):
        return cls.__descripcion
    
    @classmethod
    def set_tratamiento(cls):
        try:
            input("Ingreseel tratamiento de la mascota")
        except KeyboardInterrupt:
            print("El himostrar_historial ha cancelado la entrada de texto ")
    @classmethod        
    def get_tratamiento(cls):
        return cls.__tratemiento
    
    def set_id_veteerinario(cls):
             while True:
                try:
                    id = int(input('Escriba el id del historial: '))
                    if (1 <= id<= 1000000000):
                        cls.__id = id
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El himostrar_historial ha cancelado la entrada de datos.')
                continue
    @classmethod        
    def get_id_veterinario(cls):
        return cls.__id_veterinario
    
    def set_id_mascota(cls):
             while True:
                try:
                    id = int(input('Escriba el id del historial: '))
                    if (1 <= id<= 1000000000):
                        cls.__id = id
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El himostrar_historial ha cancelado la entrada de datos.')
                continue
    @classmethod        
    def get_id_mascota(cls):
        return cls.__id_mascota
    
    @classmethod
    def captura_datos(cls):
        cls.set_id()
        cls.set_fecha()
        cls.set_descripcion()
        cls.set_tratamiento()
        cls.set_id_veteerinario()
        cls.set_id_mascota()
    
    @classmethod
    def InsertarHistorialMedico(cls):
        cls.captura_datos()
        conexion = BaseDatos.conectar()
        
        if conexion:
            cursor_historial = conexion.cursor
            cursor_historial.callproc( 'InsertarHistorialMedico', [
                cls.get_id(),
                cls.get_fecha(),
                cls.get_descripcion(),
                cls.get_tratamiento(),
                cls.get_id_veterinario(),
                cls.get_id_mascota()
            ])
            conexion.commit()
            print('Historial registrado correctamente...')
            if conexion:
                BaseDatos.desconectar()
        
    @classmethod
    def ActualizarHistorialMedico(cls):
        codigo = input('Ingrese el id del historial a actualiza: ')
        conexion = BaseDatos.conectar
        mostrar_historial = cls.BuscarHistorialMedicoID(codigo)
        
        if mostrar_historial:
            try:
                print('--------------- Escriba los nuevos datos del historial ---------------')
                cls.set_id()
                cls.set_fecha()
                cls.set_descripcion()
                cls.set_tratamiento()
                cls.set_id_veteerinario()
                cls.set_id_mascota()
                
                nuevo_id = cls.get_id(),
                nueva_fecha = cls.get_fecha(),
                nueva_descripcion = cls.get_descripcion(),
                nuevo_tratamiento = cls.get_tratamiento(),
                nuevo_id_vet = cls.get_id_veterinario(),
                nuevo_id_mas = cls.get_id_mascota()
                
                print(f'ID: {codigo}')
                print(f'Nuevo id: {nuevo_id}')
                print(f'Nueva gecha: {nueva_fecha}')
                print(f'Nueva descripcion: {nueva_descripcion}')
                print(f'Nuevo tratamiento: {nuevo_tratamiento}')
                print(f'Nuevo id veterinario: {nuevo_id_vet}')
                print(f'Nuevo id mascota: {nuevo_id_mas}')

                cursor_historial = conexion.cursor ()
                cursor_historial.callproc('ActualizarHistorialMedico', [
                    codigo,
                    nuevo_id,
                    nueva_fecha,
                    nueva_descripcion,
                    nuevo_tratamiento,
                    nuevo_id_vet,
                    nuevo_id_mas
                ])
                
                conexion.commit()
                cursor_historial.closed()
                print('Historial actualizado')
                
            except Exception as error:
                print(f'Error al actualizar el historial: {error}. Intente de nuevo')
            finally:
                    BaseDatos.desconectar()
        else:
            print('Historial no encontrado. Intente otra vez')

        
    @classmethod
    def buscar_historial_id(cls, codigo = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                system("cls")
                if codigo is None:
                    while True:
                        codigo = int(input("Id del historial a buscar: "))
                        if codigo >= 1:
                            break
                        else:
                            print("Escribe un codigo valido")
                system('cls')
                mostrar_historial = False
                cursor_historial = conexion.cursor()
                print(f'Buscando el historial {codigo}...')
                cursor_historial.callproc('BuscarHistorialMedicoID', [codigo])
                for busqueda in cursor_historial.stored_results():
                    resultado = busqueda.fetchall()
                    if resultado:
                        mostrar_historial = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return mostrar_historial
                    else:
                        print('HIstorial no encontrada. Intente de nuevo.')
                        print(mostrar_historial)
                        return mostrar_historial
            except Exception as e:
                print(f'Error al buscar historial: {e}')
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()
    
    @classmethod
    def EliminarHistorialMedico(cls,codigo):
        conexion = BaseDatos.conectar()
        mostrar_historial= cls.BuscarMascotaID(codigo)
        if mostrar_historial:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('EliminarHistorialMedico', [codigo])
                conexion.commit()
                cursor_historial.close()
                print('Historial eliminado')
            except Exception as error:
                print(f'Error al eliminar el historial: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
    
    @classmethod
    def BuscarHistorialesMedicos(cls):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                historial_encontrado = False
                cursor_historial = conexion.cursor()
                print(f'Buscando el historial...')
                cursor_historial.callproc('BuscarHistorialesMedicos')
                for busqueda in cursor_historial.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return historial_encontrado
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(historial_encontrado)
                        return historial_encontrado
            except Exception as e:
                print(f'Error al buscar el historial: {e}')
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()  
                    
    