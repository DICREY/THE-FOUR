import mysql.connector
from mysql.connector import errorcode

class BaseDatos:

    _HOST = '127.0.0.1'
    _USER = 'root'
    _PASSWORD = '12345678'
    _DATABASE = 'mascotas_db'
    _PORT = 3306
    _conexion = None
    _cursor = None
    
    @classmethod
    def conectar(cls):
        try:
            cls._conexion = mysql.connector.connect(
                host=cls._HOST,
                user=cls._USER,
                password=cls._PASSWORD,
                database=cls._DATABASE,
                port=cls._PORT
            )
            cls._cursor = cls._conexion.cursor()
            print('Conexión abierta...')
            return cls._conexion
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Verifique las credenciales de conexión')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Base de datos no existe')
            elif err.errno == errorcode.ER_BAD_HOST_ERROR:
                print('El nombre del host es incorrecto')
            elif err.errno == errorcode.ER_CONN_HOST_ERROR:
                print('Error al intentar conectar con el host')
            elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
                print('Acceso denegado a la base de datos')
            elif err.errno == errorcode.CR_CONN_HOST_ERROR:
                print('No se pudo conectar al servidor MySQL')
            else:
                print(f'Error desconocido: {err}')
        except Exception as ex:
            print(f'Error general: {ex}')

    @classmethod
    def ejecutar_query(cls, query, params=None):
        try:
            cls._cursor.execute(query, params)
            # Si la consulta es una SELECT, se deben recuperar los resultados
            if query.strip().lower().startswith('select'):           
                resultado = cls._cursor.fetchall()
                if resultado:
                    for fila in resultado:
                        print(fila)
                else:
                    print('No hay resultados...')
                    return None
                return resultado
            else:
                cls.conexion.commit()
                print('Query ejecutada con éxito')
        except mysql.connector.ProgrammingError as pe:
            print(f'Error en la query: {pe}')
        except mysql.connector.DataError as de:
            print(f'Error de datos: {de}')
        except mysql.connector.IntegrityError as ie:
            print(f'Error de integridad de datos: {ie}')
        except mysql.connector.OperationalError as oe:
            print(f'Error operacional: {oe}')
        except mysql.connector.InternalError as ie:
            print(f'Error interno del sistema: {ie}')
        except mysql.connector.NotSupportedError as nse:
            print(f'Error de operación no soportada: {nse}')
        except mysql.connector.InterfaceError as ie:
            print(f'Error de interfaz de conexión: {ie}')
        except Exception as ex:
            print(f'Error general: {ex}')
            
    @classmethod
    def desconectar(cls):
        try:
            if cls._cursor:
                cls._cursor.close()
            if cls._conexion == None:
                print('No hay una conexión abierta. Intente de nuevo')
            else:
                cls._conexion.close()
                print('Conexión cerrada...')
        except mysql.connector.Error as err:
            print(f'Error al cerrar la conexión: {err}')

BaseDatos.conectar()