from config.conexion10 import BaseDatos
from config.usuario import Usuario

class Veterinario(Usuario):
    @classmethod
    def __init__(cls,
        especialidad: str = None,
        horarios: str = None
    ):
        cls.__especialidad = especialidad,
        cls.__horarios = horarios
        
    @classmethod
    def get_especialidad(cls):
        return cls.__especialidad
    
    @classmethod
    def set_especialidad(cls):
        while True:
            try:
                espe=input('Ingrese la especialidad del usuario: ')
                if len(espe)>4 and len(espe)<50 :
                    cls.__especialidad = espe
                    break
                else:
                    print('La especilidad no cumple con los requisitos (deve tener una longitud mayor a 4 y menor a 50)')
            except KeyboardInterrupt:
                print('Operación cancelada por el usuario')
                continue
    
    @classmethod
    def get_horarios(cls):
        return cls.__horarios
    
    @classmethod
    def set_horarios(cls):
        while True:
            try:
                hor=input('Ingrese los horarios de atención del usuario: ')
                if len(hor)>5 and len(hor)<100 :
                    cls.__horarios = hor
                    break
                else:
                    print('Los horarios no cumplen con los requisitos (deve tener una longitud mayor a 10 y menor a 100)')
            except KeyboardInterrupt:
                print('Operación cancelada por el usuario')
                continue
    
    @classmethod
    def capturar_datos_veterinario(cls):
        cls.capturar_datos(),
        cls.set_especialidad(),
        cls.set_horarios()
        
    
    @classmethod
    def insertar_veterinario(cls):
        cls.capturar_datos_veterinario()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('InsertarVeterinario', [
                cls.get_codigo(),
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_email(),
                cls.get_contrasenna(),
                cls.get_especialidad(),
                cls.get_horarios()
            ])
            conexion.commit()
        print("Veterinario registrado correctamente")
        if conexion:
            BaseDatos.desconectar()

    @classmethod
    def actualizar_veterinario(cls,codigo = None):
        cls.capturar_datos_veterinario()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.callproc('ActualizarVeterinario', [
                codigo,
                cls.get_nombre(),
                cls.get_apellido(),
                cls.get_ciudad(),
                cls.get_direccion(),
                cls.get_telefono(),
                cls.get_email(),
                cls.get_contrasenna(),
                cls.get_especialidad(),
                cls.get_horarios()
            ])
            conexion.commit()
            print("Veterinario actualizado correctamente")
        if conexion:
            BaseDatos.desconectar()

    @classmethod
    def eliminar_veterinario(cls,codigo = None):
        conexion = BaseDatos.conectar()
        try:
                cursor_veterinario= conexion.cursor()
                cursor_veterinario.callproc('EliminarVeterinarios', [codigo])
                conexion.commit()
                cursor_veterinario.close()
                print('veterinario eliminado')
        except Exception as error:
                print(f'Error al eliminar el veterinario: {error}. Intente de nuevo')
        finally:
                BaseDatos.desconectar()

    @classmethod
    def buscar_veterinario_id(cls, id_usuario = None):
        conexion = BaseDatos.conectar()
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
    
    
    @classmethod
    def buscar_veterinario_nombre(cls,name = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                veterinario_encontrado = False
                cursor_veterinario = conexion.cursor()
                print(f'Buscando veterinario...')
                cursor_veterinario.callproc('BuscarVeterinarioNombre',[name])
                for busqueda in cursor_veterinario.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return veterinario_encontrado
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(veterinario_encontrado)
                        return veterinario_encontrado
            except Exception as e:
                print(f'Error al buscar veterinario: {e}')
            finally:
                if conexion:
                    cursor_veterinario.close()
                    BaseDatos.desconectar()
    
    
    