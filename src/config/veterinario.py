from config.conexion10 import BaseDatos
from config.usuario import Usuario

class Veterinario(Usuario):
    def __init__(self,
        especialidad: str = None,
        horarios: str = None
    ):
        self.__especialidad = especialidad,
        self.__horarios = horarios
        
    def get_especialidad(self):
        return self.__especialidad
    
    def set_especialidad(self):
        while True:
            try:
                espe=input('Ingrese la especialidad del usuario: ')
                if len(espe)>4 and len(espe)<50 :
                    self.__especialidad = espe
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
        
    
    def insertar_veterinario(self):
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
        print("Veterinario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()

    def actualizar_veterinario(self):
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
            print("Veterinario actualizado correctamente")
        if conexion:
            BaseDatos.desconectar()

    def eliminar_veterinario(self):
        conexion = BaseDatos.conectar()
        id_usuario=int(input('ingrese el id del veterinario que desea eliminar: '))
        try:
                cursor_veterinario= conexion.cursor()
                cursor_veterinario.callproc('EliminarVeterinarios', [id_usuario])
                conexion.commit()
                cursor_veterinario.close()
                print('veterinario eliminado')
        except Exception as error:
                print(f'Error al eliminar el veterinario: {error}. Intente de nuevo')
        finally:
                BaseDatos.desconectar()

    def buscar_veterinario(self):
        conexion = BaseDatos.conectar()
        id_usuario=int(input('ingrese el id del veterianrio a buscar: '))
        if conexion:
            try:
                veterinariocursor_veterinario_encontrada = False
                cursor_veterinario = conexion.cursor()
                print(f'Buscando al veterinario {id_usuario}...')
                cursor_veterinario.callproc('BuscarVeterinarioID', [id_usuario])
                for busqueda in cursor_veterinario.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        veterinariocursor_veterinario_encontrada = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return veterinariocursor_veterinario_encontrada
                    else:
                        print('veterinariocursor_veterinario no encontrada. Intente de nuevo.')
                        print(veterinariocursor_veterinario_encontrada)
                        return veterinariocursor_veterinario_encontrada
            except Exception as e:
                print(f'Error al buscar la veterinariocursor_veterinario: {e}')
            finally:
                if conexion:
                    cursor_veterinario.close()
                    BaseDatos.desconectar()