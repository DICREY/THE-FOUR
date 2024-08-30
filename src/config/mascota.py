import re
import os 
from config.conexion10 import BaseDatos
#from usuario import Usuario


class Mascota():
    @classmethod
    def __init__(cls,
                 id: str = None ,
                 nombre : str = None,
                 especie: str = None,
                 raza : str = None,
                 edad : float = None,
                 peso :float = None,
                 sexo : str = None,
                 id_propietario: str = None,
                 #historial_medico= None
                 ):
        
        cls._id = id
        cls._nombre = nombre
        cls._especie = especie
        cls._raza = raza
        cls._edad = edad
        cls._peso = peso
        cls._sexo = sexo
        cls._id_propietario = id_propietario
        #cls._historial_medico = historial_medico if historial_medico is not None else []
        
    
    #get y set
    @classmethod
    def set_id(cls):
             while True:
                try:
                    id_mascota = input('Escriba el código de la mascota: ')
                    if (1 <= len(id_mascota) <= 1000000000):
                        cls._id = id_mascota
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
            
    @classmethod
    def get_id(cls):
        return cls._id
    
    
    @classmethod
    def set_nombre(cls):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                nombre = input("Ingrese el nombre de la mascota nombre: ")
                if len(nombre) >= 3 and re.match(patron, nombre):
                    cls._nombre = nombre 
                    break
                else:
                    print("El nombre debe tener almenos 3 caracteres. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
            
    @classmethod
    def get_nombre(cls):
        return cls._nombre
        
    @classmethod
    def set_especie(cls):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                especie = input("Ingrese la especie de la mascota: ")
                if len(especie) >= 3 and re.match(patron, especie):
                    cls._especie = especie
                    break
                else:
                    print("La especie debe tener almenos 3 caracteres. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
            
    @classmethod
    def get_especie(cls):
        return cls._especie
        
    @classmethod
    def set_raza(cls):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                raza = input("Ingrese la raza de la mascota: ")
                if len(raza) >= 3 and re.match(patron, raza):
                    cls._raza = raza
                    break
                else:
                    print("La raza debe tener almenos 3 caracteres. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
        
    @classmethod
    def get_raza(cls):
        return cls._raza
    
        
    @classmethod
    def set_edad(cls):
           while True:
            try:
                edad = float(input('Edad de la mascota (años): '))
                if 0 < edad <= 80.0:
                    cls._edad = edad
                    break
                else:
                    print('Edad no válida')
            except ValueError:
                print('Edad acepta solo números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                

    
    @classmethod
    def get_edad(cls):
        return cls._edad
        
    @classmethod
    def set_peso(cls):
        while True:
            try:
                peso = float(input('Peso en kg: '))
                if (0.1 < peso <= 1000.0):
                    cls._peso = peso
                    break
                else:
                    print('Peso no válido')
            except ValueError:
                print('El peso acepta solo números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue        
    
    @classmethod
    def get_peso(cls):
        return cls._peso
    
    @classmethod
    def set_sexo(cls):
        while True:
            try:
                list_sexo = ["F","M"]
                sexo = input("Ingrese el genero de la mascota: ").upper()
                if sexo in list_sexo:
                    cls._sexo = sexo
                    break
                else:
                    print("Error. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
        
    @classmethod
    def get_sexo(cls):
        return cls._sexo
    
    @classmethod
    def set_id_propietario(cls):
        while True:
            try:
                id_propietario = input('Id Propietario: ')
                if (0 < len(id_propietario) <= 1000000000):
                    cls._id_propietario = id_propietario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue       
    
    @classmethod
    def get_id_propietario(cls):
        return cls._id_propietario
    
    #@classmethod
    # def get_historial(cls):
       # return cls.__historial


    #@classmethod
    # def agregar_historial_medico(cls, entrada: str):
       # cls.__historial_medico.append(entrada)
        
#Metodos

    @classmethod
    def InsertarMascota(cls):
            cls.capturar_datos()
            conexion = BaseDatos.conectar()
            if conexion:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('InsertarMascota', [
                    cls.get_id(),
                    cls.get_nombre(),
                    cls.get_especie(),
                    cls.get_raza(),
                    cls.get_edad(),
                    cls.get_peso(),
                    cls.get_id_propietario(),
                    cls.get_sexo()
                ])
                conexion.commit()
            print('Mascota registrada correctamente...')
            if conexion:
                BaseDatos.desconectar()
    
    @classmethod
    def capturar_datos(cls):
            cls.set_id()
            cls.set_nombre()
            cls.set_especie()
            cls.set_raza()
            cls.set_edad()
            cls.set_peso()
            cls.set_sexo()
            cls.set_id_propietario()
            
    @classmethod
    def BuscarMascotaID(cls, id_mascota=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                mascota_encontrada = False
                cursor_mascota = conexion.cursor()
                print(f'Buscando la mascota {id_mascota}...')
                cursor_mascota.callproc('BuscarMascotaID', [id_mascota])
                for busqueda in cursor_mascota.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        mascota_encontrada = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return mascota_encontrada
                    else:
                        print('Mascota no encontrada. Intente de nuevo.')
                        print(mascota_encontrada)
                        return mascota_encontrada
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()



    @classmethod
    def ActualizarMascota(cls, id_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = cls.BuscarMascotaID(id_mascota)
        if mascota_encontrada:
            try:
                print('--------------- Escriba los nuevos datos de la mascota ---------------')
                cls.set_nombre()
                cls.set_especie()
                cls.set_raza()
                cls.set_edad()
                cls.set_peso()
                cls.set_sexo()
                cls.set_id_propietario()
                
                nuevo_nombre = cls.get_nombre()
                nueva_especie = cls.get_especie()
                nueva_raza = cls.get_raza()
                nueva_edad = cls.get_edad()
                nuevo_peso = cls.get_peso()
                nuevo_sexo = cls.get_sexo()
                nuevo_id_propietario = cls.get_id_propietario()
                
                print(f'Código: {id_mascota}')
                print(f'Nuevo nombre: {nuevo_nombre}')
                print(f'Nueva especie: {nueva_especie}')
                print(f'Nueva raza: {nueva_raza}')
                print(f'Nueva edad: {nueva_edad}')
                print(f'Nuevo peso: {nuevo_peso}')
                print(f'Nuevo sexo: {nuevo_sexo}')
                print(f'Nuevo propietario: {nuevo_id_propietario}')
                
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ActualizarMascota', [
                    id_mascota,
                    nuevo_nombre,
                    nueva_especie,
                    nueva_raza,
                    nueva_edad,
                    nuevo_peso,
                    nuevo_id_propietario,
                    nuevo_sexo

                ])
                conexion.commit()
                cursor_mascota.close()
                print('Mascota actualizada')
            except Exception as error:
                print(f'Error al actualizar la mascota: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Mascota no encontrada. Intente otra vez')
             

    @classmethod
    def EliminarMascota(cls, id_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = cls.BuscarMascotaID(id_mascota)
        if mascota_encontrada:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarMascota', [id_mascota])
                conexion.commit()
                cursor_mascota.close()
                print('Mascota eliminada')
            except Exception as error:
                print(f'Error al eliminar la mascota: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()

    @classmethod
    def BuscarMascotaNombre(cls):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                mascota_encontrado = False
                cursor_mascota = conexion.cursor()
                print(f'Buscando la mascotas...')
                cursor_mascota.callproc('BuscarMascotaNombre')
                for busqueda in cursor_mascota.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return mascota_encontrado
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(mascota_encontrado)
                        return mascota_encontrado
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()