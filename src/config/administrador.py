import os 
import re
from usuario import Usuario
from datetime import datetime
from conexion10 import BaseDatos

class Administrador(Usuario):
    def __init__(self,
                 
                 cargo: str = None,
                 fecha: datetime = None
                 ):
        #super().__init__(id_usuario, nombre, apellido, ciudad, direccion, telefono,
                         #es_propietario, es_veterinario, es_administrador,
                         #email, contrasenna)
        self._fecha = fecha
        self._cargo = cargo
        
    def set_cargo(self):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                cargo = input("Ingrese el cargo del administrador: ")
                if len(cargo) >= 3 and re.match(patron, cargo):
                    self.set_cargo= cargo
                    break
                else:
                    print("Error, intente nuevamente")
                
            except ValueError:
                print('El cargo solo debe tener letras.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_cargo(self):
        return self.cargo
    
    def set_fecha_in(self):
        while True:
            try:
                patron = r'^\d{4}-\d{2}-\d{2}$'
                fecha = input("Ingrese la fecha en formato YYYY-MM-DD: ")
                
                if re.match(patron, fecha):
                    try:
                        datetime.strptime(fecha, '%Y-%m-%d')
                        self.fecha = fecha
                        break
                    except ValueError:
                        print("Fecha inválida, intente nuevamente.")
                else:
                    print("Formato de fecha incorrecto, intente nuevamente.")
                
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                break
    
    def capturar_datos(self):
        self.set_cargo()
        self.set_fecha_in ()
    
    def InsertarAdministrador(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        
        if conexion:
            cursor_admin = conexion.cursor
            cursor_admin.callproc('InsertarAdministrador', [
                self.get_id_usuario(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_es_propietario(),
                self.get_es_veterinario(),
                self.get_es_administrador(),
                self.get_email(),
                self.get_contrasenna(),
                self.get_cargo(),
                self.get_fecha_in()
            ])
            conexion.commit()
            print('Administrador registrado correctamente...')
            if conexion:
                BaseDatos.desconectar()
        
    def ActualizarAdministrador(self, codigo = None):
        conexion = BaseDatos.conectar()
        usuario_encontrado = self.""(codigo)
        if usuario_encontrado:
            try:
                    print('--------------- Escriba los nuevos del administrador ---------------')
                    self.get_id_usuario()
                    self.set_nombre()
                    self.set_apellido()
                    self.set_ciudad()
                    self.set_direccion()
                    self.set_telefono()
                    self.set_es_propietario()
                    self.set_es_veterinario()
                    self.set_es_administrador()
                    self.set_email()
                    self.set_contrasenna()
                    self.set_cargo()
                    self.set_fecha_in()
                
                
                    nuevo_nombre = self.get_nombre()
                    nuevo_apellido = self.get_apellido()
                    nueva_ciudad = self.get_ciudad()
                    nueva_direccion = self.get_direccion()
                    nuevo_telefono = self.get_telefono()
                    nuevo_es_propietario = self.get_es_propietario()
                    nuevo_es_veterinario =self.get_es_veterinario()
                    nuevo_es_administrador = self.get_es_administrador()
                    nuevo_email = self.get_email()
                    nueva_contrasenna = self.get_contrasenna()
                    nuevo_cargo = self.get_cargo()
                    
                    print(f'Id: {codigo}')
                    print(f'Nuevo nombre: {nuevo_nombre}')
                    print(f'Nueva apellido: {nuevo_apellido}')
                    print(f'Nueva ciudad: {nueva_ciudad}')
                    print(f'Nueva direccion: {nueva_direccion}')
                    print(f'Nuevo telefono: {nuevo_telefono}')
                    print(f'Es propietario: {nuevo_es_propietario}')
                    print(f'Es veterinario: {nuevo_es_veterinario}')
                    print(f'Es administrador: {nuevo_es_administrador}')
                    print(f'Nuevo email: {nuevo_email}')
                    print(f'Nueva contraseña: {nueva_contrasenna}')
                    print(f'Nuevo cargo: {nuevo_cargo}')
                    
                    cursor_mascota = conexion.cursor()
                    cursor_mascota.callproc('ActualizarAdministrador', [
                        codigo,
                        nuevo_nombre,
                        nuevo_apellido,
                        nueva_ciudad,
                        nueva_direccion,
                        nuevo_telefono,
                        nuevo_es_propietario,
                        nuevo_es_veterinario,
                        nuevo_es_administrador,
                        nuevo_email,
                        nueva_contrasenna
                    ])
                    conexion.commit()
                    cursor_mascota.close()
                    print('Administrador actualizada')
            except Exception as error:
                print(f'Error al actualizar el administrador: {error}. Intente de nuevo')
            finally:
                    BaseDatos.desconectar()
        else:
            print('Administrador no encontrada. Intente otra vez')
    


         
    def EliminarAdministrador(self, codigo):
        conexion = BaseDatos.conectar()
        mascota_encontrada = self.BuscarMascotaID(codigo)
        if mascota_encontrada:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarAdministrador', [codigo])
                conexion.commit()
                cursor_mascota.close()
                print('Mascota eliminada')
            except Exception as error:
                print(f'Error al eliminar el administrador: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()       
                
           