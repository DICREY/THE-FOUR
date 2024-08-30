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
                fecha = input("Ingrese la fecha en formato YYYY-MM-DD: ")
                
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
    def capturar_datos(cls):
        cls.set_cargo()
        cls.set_fecha_in ()
    
    @classmethod
    def insertar_administrador(cls):
        cls.capturar_datos()
        conexion = BaseDatos.conectar()
        
        if conexion:
            cursor_admin = conexion.cursor
            cursor_admin.callproc('InsertarAdministrador', [
                cls.get_id_usuario(),
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_email(),
                cls.get_contrasenna(),
                cls.get_cargo(),
                cls.get_fecha_in()
            ])
            conexion.commit()
            print('Administrador registrado correctamente...')
            if conexion:
                BaseDatos.desconectar()
    @classmethod
    def actualizar_administrador(cls,codigo = None):
        conexion = BaseDatos.conectar()
        mostrar_usuario = cls.BuscarAdministradorID(codigo)
        if mostrar_usuario:
            try:
                    print('--------------- Escriba los nuevos datos del administrador ---------------')
                    cls.set_id_usuario()
                    cls.set_nombre()
                    cls.set_apellido()
                    cls.set_ciudad()
                    cls.set_direccion()
                    cls.set_telefono()
                    cls.set_email()
                    cls.set_contrasenna()
                    cls.set_cargo()
                    cls.set_fecha_in()
                
                
                    nuevo_nombre = cls.get_nombre()
                    nuevo_apellido = cls.get_apellido()
                    nueva_ciudad = cls.get_ciudad()
                    nueva_direccion = cls.get_direccion()
                    nuevo_telefono = cls.get_telefono()
                    nuevo_email = cls.get_email()
                    nueva_contrasenna = cls.get_contrasenna()
                    nuevo_cargo = cls.get_cargo()
                    nueva_fecha_in = cls.get_fecha_in()
                    
                    print(f'Id: {codigo}')
                    print(f'Nuevo nombre: {nuevo_nombre}')
                    print(f'Nueva apellido: {nuevo_apellido}')
                    print(f'Nueva ciudad: {nueva_ciudad}')
                    print(f'Nueva direccion: {nueva_direccion}')
                    print(f'Nuevo telefono: {nuevo_telefono}')
                    print(f'Nuevo email: {nuevo_email}')
                    print(f'Nueva contraseña: {nueva_contrasenna}')
                    print(f'Nuevo cargo: {nuevo_cargo}')
                    print(f'Nuevo fecha de ingreso: {nueva_fecha_in}')
                    
                    cursor_admin = conexion.cursor()
                    cursor_admin.callproc('ActualizarAdministrador', [
                                    codigo,
                                    nuevo_nombre,
                                    nuevo_apellido,
                                    nueva_ciudad,
                                    nueva_direccion,
                                    nuevo_telefono,
                                    nuevo_email,
                                    nueva_contrasenna,
                                    nueva_fecha_in
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
    def eliminar_administrador(cls, codigo):
        conexion = BaseDatos.conectar()
        mostrar_usuario = cls.BuscarMascotaID(codigo)
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
    def buscar_administrador_nombre(cls):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                admin_encontrado = False
                cursor_admin = conexion.cursor()
                print(f'Buscando el administrador...')
                cursor_admin.callproc('BuscarAdministradorNombre')
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

