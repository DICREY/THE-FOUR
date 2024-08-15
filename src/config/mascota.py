import re
import os 
from conexion10 import BaseDatos
#from usuario import Usuario


class Mascota():
    def __init__(self,
                 id: int = None ,
                 nombre : str = None,
                 especie: str = None,
                 raza : str = None,
                 edad : float = None,
                 peso :float = None,
                 sexo : str = None,
                 id_usuario: int = None,
                 #historial_medico= None
                 ):
        
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self._peso = peso
        self._sexo = sexo
        self._id_usuario = id_usuario
        #self._historial_medico = historial_medico if historial_medico is not None else []
        
    
    #get y set
    def set_id(self):
             while True:
                try:
                    id_mascota = int(input('Escriba el código de la mascota: '))
                    if (1 <= id_mascota <= 1000000000):
                        self._id = id_mascota
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
            
    def get_id(self):
        return self._id
    
    
    def set_nombre(self):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                nombre = input("Ingrese el nombre de la mascota nombre: ")
                if len(nombre) >= 3 and re.match(patron, nombre):
                    self._nombre = nombre 
                    break
                else:
                    print("El nombre debe tener almenos 3 caracteres. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
            
    def get_nombre(self):
        return self._nombre
        
    def set_especie(self):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                especie = input("Ingrese la especie de la mascota: ")
                if len(especie) >= 3 and re.match(patron, especie):
                    self._especie = especie
                    break
                else:
                    print("La especie debe tener almenos 3 caracteres. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
            
    def get_especie(self):
        return self._especie
        
    def set_raza(self):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                raza = input("Ingrese la raza de la mascota: ")
                if len(raza) >= 3 and re.match(patron, raza):
                    self._raza = raza
                    break
                else:
                    print("La raza debe tener almenos 3 caracteres. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
        
    def get_raza(self):
        return self._raza
    
        
    def set_edad(self):
           while True:
            try:
                edad = float(input('Edad de la mascota (años): '))
                if 0 < edad <= 80.0:
                    self._edad = edad
                    break
                else:
                    print('Edad no válida')
            except ValueError:
                print('Edad acepta solo números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                

    
    def get_edad(self):
        return self._edad
        
    def set_peso(self):
        while True:
            try:
                peso = float(input('Peso en kg: '))
                if (0.1 < peso <= 1000.0):
                    self._peso = peso
                    break
                else:
                    print('Peso no válido')
            except ValueError:
                print('El peso acepta solo números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue        
    
    def get_peso(self):
        return self._peso
    
    def set_sexo(self):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                sexo = input("Ingrese el genero de la mascota: ")
                if len(sexo) >= 10 and re.match(patron, sexo):
                    self._sexo = sexo.upper()
                    break
                else:
                    print("Error. Intente nuevamente.")
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
        
    def get_sexo(self):
        return self._sexo
    
    
    def set_id_usuario(self):
        while True:
            try:
                id_usuario = int(input('Id usuario: '))
                if (0 < id_usuario <= 1000000000):
                    self._id_usuario = id_usuario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue       
    
    def get_usuario(self):
        return self._usuario
    
    #def get_historial(self):
       # return self.__historial



    #def agregar_historial_medico(self, entrada: str):
       # self.__historial_medico.append(entrada)
        
#Metodos

    def InsertarMascota(self):
            self.capturar_datos()
            conexion = BaseDatos.conectar()
            if conexion:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('CrearMascota', [
                    self.get_id(),
                    self.get_nombre(),
                    self.get_especie(),
                    self.get_raza(),
                    self.get_edad(),
                    self.get_peso(),
                    self.get_sexo(),
                    self.get_id_usuario()
                ])
                conexion.commit()
            print('Mascota registrada correctamente...')
            if conexion:
                BaseDatos.desconectar()
    
    def capturar_datos(self):
            self.set_id()
            self.set_nombre()
            self.set_especie()
            self.set_raza()
            self.set_edad()
            self.set_peso()
            self.set_sexo()
            #self.set_id_usuario()
            
    def buscar_mascota(self, id_mascota=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                mascota_encontrada = False
                cursor_mascota = conexion.cursor()
                print(f'Buscando la mascota {id_mascota}...')
                cursor_mascota.callproc('BuscarMascota', [id_mascota])
                for busqueda in cursor_mascota.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        mascota_encontrada = True
                        print(mascota_encontrada)
                        print('Resultado:') # Si encontró  datos los imprime
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
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



    def ActualizarMascota(self, id_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = self.buscar_mascota(id_mascota)
        if mascota_encontrada:
            try:
                print('Escriba los nuevos datos de la mascota: ')
                self.set_nombre()
                self.set_especie()
                self.set_raza()
                self.set_edad()
                self.set_peso()
                self.set_sexo()
                
                nuevo_nombre = self.get_nombre()
                nueva_especie = self.get_especie()
                nueva_raza = self.get_raza()
                nueva_edad = self.get_edad()
                nuevo_peso = self.get_peso()
                nuevo_sexo = self.get_sexo()
                
                print(f'Código: {id_mascota}')
                print(f'Nuevo nombre: {nuevo_nombre}')
                print(f'Nueva especie: {nueva_especie}')
                print(f'Nueva raza: {nueva_raza}')
                print(f'Nueva edad: {nueva_edad}')
                print(f'Nuevo peso: {nuevo_peso}')
                print(f'Nuevo sexo: {nuevo_sexo}')

                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ActualizarMascota', [
                    id_mascota,
                    nuevo_nombre,
                    nueva_especie,
                    nueva_raza,
                    nueva_edad,
                    nuevo_peso,
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



    def BuscarMascotaID(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                mascota_encontrada = False
                cursor_mascota = conexion.cursor()
                print(f'Buscando la mascotas...')
                cursor_mascota.callproc('BuscarMascotas')
                for busqueda in cursor_mascota.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return mascota_encontrada
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(mascota_encontrada)
                        return mascota_encontrada
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()    


    def eliminar_mascota(self, id_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = self.buscar_mascota(id_mascota)
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
