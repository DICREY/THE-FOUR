#from historial_medico import HistorialMedico
from conexion10 import BaseDatos
import re

class Usuario:

    def __init__(
            self,
            id_usuario: int = None,
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
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._apellido = apellido
        self._ciudad = ciudad
        self._direccion = direccion
        self._telefono = telefono
        self._es_propietario = es_propietario
        self._es_veterinario = es_veterinario
        self._es_administrador = es_administrador
        self._email = email
        self._contrasenna = contrasenna

    # GET y SET

    def get_codigo(self):
        return self.__id_usuario
    
    def set_codigo(self):
            while True:
                try:
                    codigo = int(input('Escriba el código del usuario: '))
                    if (1 <= codigo <= 1000000000):
                        self.__id_usuario = codigo
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
 

    def get_nombre(self):
        return self.__nombre
    

    def set_nombre(self):
        while True:
            try:
                nombre = input('Nombre del usuario: ')
                if len(nombre)>3:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    def get_apellido(self):
        return self.__apellido

    
    def set_apellido(self):
        while True:
            try:
                apellido = input('apellido del usuario: ')
                if 3 < len(apellido) <= 50:
                    self.__apellido = apellido
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    def get_ciudad(self):
        return self.__ciudad
    

    def set_ciudad(self):
        while True:
            try:
                ciudad = input('ciudad del usuario: ')
                # Verificar que solo contenga letras y espacios y que la longitud esté entre 2 y 30 caracteres
                if re.match(r'^[A-Za-z\s]{3,30}$', ciudad):
                    self.__ciudad = ciudad
                    break
                else:
                    print('Datos de ciudad incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    
    def get_direccion(self):
        return self.__direccion
    

    def set_direccion(self):
        while True:
            try:
                direccion = input('direccion del usuario: ')
                self.__direccion = direccion
                break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                


    def get_telefono(self):
        return self.__telefono
    

    def set_telefono(self):
        while True:
            try:
                telefono = input('Escribe el telefono del usuario: ')
                self.__telefono = telefono
                break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                 


    def get_es_propietario(self):
        return self.__es_propietario
    

    def get_es_veterinario(self):
        return self.__es_veterinario
    

    def get_es_administrador(self):
        return self.__es_administrador
    

    def get_email(self):
        return self.__email
    

    def set_email(self):
        while True:
            try:
                email = input('Email del usuario : ')
                if "@" in email:
                    self.__email = email
                    break  
                else:
                    print("Escribe un correo valido")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue    


    def get_contrasenna(self):
        return self.__contrasenna
    

    def set_contrasenna(self):
        while True:
            try:
                contra = input('Contraseña del usuario: ')
                self.__contrasenna = contra
                break
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue   


    def capturar_datos(self):
            self.set_codigo()
            self.set_nombre()
            self.set_apellido()
            self.set_ciudad()
            self.set_direccion()
            self.set_telefono()
            self.set_email()
            self.set_contrasenna()


    def registrar(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('InsertarUsuario', [
                self.get_codigo(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_es_propietario(),
                self.get_es_veterinario(),
                self.get_es_administrador(),
                self.get_email(),
                self.get_contrasenna()
            ])
            conexion.commit()
        print("Usuario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()


