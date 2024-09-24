import os 
import re
from config.usuario import Usuario
from datetime import datetime
from config.conexion10 import BaseDatos
from os import system

os.system("cls")

class Administrador(Usuario):
    @classmethod
    def __init__(cls,
                 cargo: str = None,
                 fecha: datetime = None
                 ):
        #super().__init__(id_usuario, nombre, apellido, ciudad, direccion, telefono,
                         #es_propietario, es_veterinario, es_administrador,
                         #email, contrasenna)
        cls.__fecha = fecha
        cls.__cargo = cargo
        
    @classmethod
    def set_cargo(cls):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                cargo = input("Ingrese el cargo del administrador: ")
                if len(cargo) >= 3 and re.match(patron, cargo):
                    cls.__cargo = cargo
                    break
                else:
                    print("Error, intente nuevamente")
                
            except ValueError:
                print('El cargo solo debe tener letras.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    @classmethod
    def get_cargo(cls):
        return cls.__cargo
    
    @classmethod
    def set_fecha_in(cls):
        while True:
            try:
                patron = r'^\d{4}-\d{2}-\d{2}$'
                fecha = input("Ingrese la fecha de ingreso en formato YYYY-MM-DD: ")
                
                if re.match(patron, fecha):
                    try:
                        datetime.strptime(fecha, '%Y-%m-%d')
                        cls.__fecha = fecha
                        break
                    except ValueError:
                        print("Fecha inválida, intente nuevamente.")
                else:
                    print("Formato de fecha incorrecto, intente nuevamente.")
                
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                break

    @classmethod
    def get_fecha (cls):
        return cls.__fecha
    
    
    @classmethod
    def capturar_datos_administrador(cls):
        cls.capturar_datos()
        cls.set_cargo()
        cls.set_fecha_in()
    
    @classmethod
    def insertar_administrador(cls):
        cls.capturar_datos_administrador()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_admin = conexion.cursor()
            cursor_admin.callproc('InsertarAdministrador', [
                cls.get_codigo(),
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_email(),
                cls.get_contrasenna(),
                cls.get_cargo(),
                cls.get_fecha()
            ])
            conexion.commit()
            print('Administrador registrado correctamente...')
            if conexion:
                BaseDatos.desconectar()
    @classmethod
    def actualizar_administrador(cls,codigo = None):
        conexion = BaseDatos.conectar()
        mostrar_usuario = cls.buscar_administrador_id(codigo)
        if mostrar_usuario:
            try:
                    os.system("pause")
                    os.system("cls")
                    print('--------------- Escriba los nuevos datos del administrador ---------------')
                    cls.capturar_datos_administrador()

                    print(f'Nuevo nombre: {cls.get_nombre()}')
                    print(f'Nueva apellido: {cls.get_apellido()}')
                    print(f'Nueva ciudad: {cls.get_ciudad()}')
                    print(f'Nueva direccion: {cls.get_direccion()}')
                    print(f'Nuevo telefono: {cls.get_telefono()}')
                    print(f'Nuevo email: {cls.get_email()}')
                    print(f'Nueva contraseña: {cls.get_contrasenna()}')
                    print(f'Nuevo cargo: {cls.get_cargo()}')
                    print(f'Nuevo fecha de ingreso: {cls.get_fecha()}')
                    
                    cursor_admin = conexion.cursor()
                    cursor_admin.callproc('ActualizarAdministrador', [
                                    codigo,
                                    cls.get_nombre(),
                                    cls.get_apellido(),
                                    cls.get_ciudad(),
                                    cls.get_direccion(),
                                    cls.get_telefono(),
                                    cls.get_email(),
                                    cls.get_contrasenna(),
                                    cls.get_cargo(),
                                    cls.get_fecha()
                                ])
                    conexion.commit()
                    cursor_admin.close()
                    print('Administrador actualizado')
            except Exception as error:
                print(f'Error al actualizar el administrador: {error}. Intente de nuevo')
            finally:
                    BaseDatos.desconectar()
        else:
            print('Administrador no encontrada. Intente otra vez')
    
    @classmethod
    def buscar_administrador_id(cls, codigo=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                system('cls')
                mostrar_usuario = False
                cursor_admin = conexion.cursor()
                print(f'Buscando administrador {codigo}...')
                cursor_admin.callproc('BuscarAdministradorID', [codigo])
                for busqueda in cursor_admin.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        mostrar_usuario = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return mostrar_usuario
                    else:
                        print('Admin no encontrada. Intente de nuevo.')
                        print(mostrar_usuario)
                        return mostrar_usuario
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                if conexion:
                    cursor_admin.close()
                    BaseDatos.desconectar()
         
    @classmethod
    def eliminar_administrador(cls, codigo = None):
        conexion = BaseDatos.conectar()
        mostrar_usuario = cls.buscar_administrador_id(codigo)
        if mostrar_usuario:
            try:
                cursor_admin = conexion.cursor()
                cursor_admin.callproc('EliminarAdministrador', [codigo])
                conexion.commit()
                cursor_admin.close()
                print('Administrador eliminado')
            except Exception as error:
                print(f'Error al eliminar el administrador: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()       
    
    @classmethod
    def buscar_administrador_nombre(cls,name = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                admin_encontrado = False
                cursor_admin = conexion.cursor()
                print(f'Buscando el administrador...')
                cursor_admin.callproc('BuscarAdministradorNombre',[name])
                for busqueda in cursor_admin.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return admin_encontrado
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(admin_encontrado)
                        return admin_encontrado
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                if conexion:
                    cursor_admin.close()
                    BaseDatos.desconectar()             

