from conexion10 import BaseDatos
import re
from usuario import Usuario

class Veterinario(Usuario):
    def __init__(
        self,
        especialidad: str = None,
        horarios: str = None        
    ):
        self.__especialidad=especialidad
        self.__horarios=horarios
        
    def get_especialidad(self):
        return self.__especialidad
    
    def set_especialidad(self):
        while True:
            try:
                espe=input('Ingrese la especialidad del usuario: ')
                if len(espe)>4 and len(espe)<50 :
                    self.__especialidad = espe
                    print('La especialidad del usuario se ha insertado exitosamente')
                    break
                else:
                    print('La especilidad no cumple con los requisitos (deve tener una longitud mayor a 4 y menor a 50)')
            except KeyboardInterrupt:
                print('Operación cancelada por el usuario')
                continue
    
    def get_horarios(self):
        return self.__horarios
    
    def set_horarios(self):
        while True:
            try:
                hor=input('Ingrese los horarios de atención del usuario: ')
                if len(hor)>5 and len(hor)<100 :
                    self.__horarios = hor
                    print('Los horarios de atención del usuario se han insertado exitosamente')
                    break
                else:
                    print('Los horarios no cumplen con los requisitos (deve tener una longitud mayor a 10 y menor a 100)')
            except KeyboardInterrupt:
                print('Operación cancelada por el usuario')
                continue
    
    def capturar_datosV(self):
        self.capturar_datos(),
        self.set_especialidad(),
        self.set_horarios()
        
    
    def registrarV(self):
        self.capturar_datosV()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('InsertarVeterinario', [
                self.get_codigo(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_email(),
                self.get_contrasenna(),
                self.get_especialidad(),
                self.get_horarios()
            ])
            conexion.commit()
        print("Usuario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()

    def actualizarV(self):
        self.capturar_datosV()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('ActualizarVeterinario', [
                self.get_codigo(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_email(),
                self.get_contrasenna(),
                self.get_especialidad(),
                self.get_horarios()
            ])
            conexion.commit()
            print("Usuario actualizado correctamente")
        if conexion:
            BaseDatos.desconectar()

    def eliminarV(self):
        conexion = BaseDatos.conectar()
        id_usuario=int(input('ingrese el veterinario que desea eliminar: '))
        try:
                cursor_veterinario= conexion.cursor()
                cursor_veterinario.callproc('EliminarVeterinario', [id_usuario])
                conexion.commit()
                cursor_veterinario.close()
                print('veterinario eliminado')
        except Exception as error:
                print(f'Error al eliminar el veterinario: {error}. Intente de nuevo')
        finally:
                BaseDatos.desconectar()




veterinario1=Veterinario()
#Veterinario1.capturar_datosV()
#Veterinario1.actualizarV()
veterinario1.eliminarV()