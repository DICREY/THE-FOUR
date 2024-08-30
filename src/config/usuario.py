#from historial_medico import HistorialMedico
from config.conexion10 import BaseDatos
import re

class Usuario:
    @classmethod
    def __init__(
            cls,
            id_usuario: str = None,
            nombre: str= None,
            apellido: str= None,
            ciudad: str= None,
            direccion: str= None,
            telefono: str= None,
            es_propietario: bool = True,
            es_veterinario: bool = False,
            es_administrador: bool = False,
            email: str = None,
            contrasenna: str = None
            ):
        cls._id_usuario = id_usuario
        cls._nombre = nombre
        cls._apellido = apellido
        cls._ciudad = ciudad
        cls._direccion = direccion
        cls._telefono = telefono
        cls._es_propietario = es_propietario
        cls._es_veterinario = es_veterinario
        cls._es_administrador = es_administrador
        cls._email = email
        cls._contrasenna = contrasenna

    # GET y SET

    @classmethod
    def get_codigo(cls):
        return cls.__id_usuario
    
    @classmethod
    def set_codigo(cls):
            while True:
                try:
                    codigo = input('Escriba el código del usuario: ')
                    if (1 <= codigo <= 1000000000):
                        cls.__id_usuario = codigo
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
 

    @classmethod
    def get_nombre(cls):
        return cls.__nombre
    

    @classmethod
    def set_nombre(cls):
        while True:
            try:
                nombre = input('Nombre del usuario: ')
                if len(nombre)>3:
                    cls.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    @classmethod
    def get_apellido(cls):
        return cls.__apellido

    
    @classmethod
    def set_apellido(cls):
        while True:
            try:
                apellido = input('apellido del usuario: ')
                if 3 < len(apellido) <= 50:
                    cls.__apellido = apellido
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    @classmethod
    def get_ciudad(cls):
        return cls.__ciudad
    

    @classmethod
    def set_ciudad(cls):
        while True:
            try:
                ciudad = input('ciudad del usuario: ')
                # Verificar que solo contenga letras y espacios y que la longitud esté entre 2 y 30 caracteres
                if re.match(r'^[A-Za-z\s]{3,30}$', ciudad):
                    cls.__ciudad = ciudad
                    break
                else:
                    print('Datos de ciudad incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    
    @classmethod
    def get_direccion(cls):
        return cls.__direccion
    

    @classmethod
    def set_direccion(cls):
        while True:
            try:
                direccion = input('direccion del usuario: ')
                cls.__direccion = direccion
                break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                


    @classmethod
    def get_telefono(cls):
        return cls.__telefono
    

    @classmethod
    def set_telefono(cls):
        while True:
            try:
                telefono = input('Escribe el telefono del usuario: ')
                cls.__telefono = telefono
                break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                 


    @classmethod
    def get_es_propietario(cls):
        return cls.__es_propietario
    

    @classmethod
    def get_es_veterinario(cls):
        return cls.__es_veterinario
    

    @classmethod
    def get_es_administrador(cls):
        return cls.__es_administrador
    

    @classmethod
    def get_email(cls):
        return cls.__email
    

    @classmethod
    def set_email(cls):
        while True:
            try:
                email = input('Email del usuario : ')
                if "@" in email:
                    cls.__email = email
                    break  
                else:
                    print("Escribe un correo valido")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue    


    @classmethod
    def get_contrasenna(cls):
        return cls.__contrasenna
    

    @classmethod
    def set_contrasenna(cls):
        while True:
            try:
                contra = input('Contraseña del usuario: ')
                cls.__contrasenna = contra
                break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue   


    @classmethod
    def capturar_datos(cls):
            cls.set_codigo()
            cls.set_nombre()
            cls.set_apellido()
            cls.set_ciudad()
            cls.set_direccion()
            cls.set_telefono()
            cls.set_email()
            cls.set_contrasenna()


    @classmethod
    def registrar(cls):
        cls.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('InsertarUsuario', [
                cls.get_codigo(),
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_es_propietario(),
                cls.get_es_veterinario(),
                cls.get_es_administrador(),
                cls.get_email(),
                cls.get_contrasenna()
            ])
            conexion.commit()
        print("Usuario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()


