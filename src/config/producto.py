import os 
import re
from datetime import datetime
from config.conexion10 import BaseDatos

os.system("cls")

class Productos():
    def __init__(self,
                 id: int = None,
                 nombre: str = None,
                 descripcion: str = None,
                 precio: float = None,
                 stock: int = None
                ):
        
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock
        
    def set_id(self):
        while True:
                try:
                    id = int(input('Escriba el id del producto: '))
                    if (1 <= id <= 1000000000):
                        self._id = id
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
                nombre = input("Ingrese el nombre del producto: ")
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
    
    def set_descripcion(self):
        while True:
            try:
                patron = r'^[a-zA-Z ]+$'
                descripcion = input("Ingrese la descripcion del producto: ")
                if len(descripcion) > 10 and re.match(patron, descripcion):
                    self._descripcion = descripcion
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
    
    def get_descripcion(self):
        return self._descripcion
    
    def set_precio(self):
        while True:
            try:
                precio = input("Ingrese el precio del producto: ")
                if (1 <= precio <= 1000000000):
                    self._precio = precio
                    break
                else:
                    print('Error inserte nuevamente')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
            
    def get_precio(self):
        return self._precio
    
    def set_stock(self):
        while True:
            try:
                stock = input("Inserte la cantidad de productos que hay: ")
                self._stock = stock
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
    
    def get_stock(self):
        return self._stock
    
    def InsertarProducto(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        
        if conexion: 
            cursor_productos = conexion.cursor()
            cursor_productos.callproc("InsertarProducto", [
                self.get_id(),
                self.get_nombre(),
                self.get_descripcion(),
                self.get_precio(),
                self.get_stock()
            ])
            conexion.commit()
        print("Producto registrado correctamente...")
        if conexion:
            BaseDatos.desconectar()
            
    def captura_datos(self):
        self.set_id()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()
        self.set_stock()
    
    def BuscarProductoID(self, id = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try: 
                producto_encontrado = False
                cursor_productos = conexion.cursor()
                print(f"Buscando el producto {id}...")
                cursor_productos.callproc("BuscarProductoID", [id])
                for busqueda in cursor_productos.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        producto_encontrado = True
                        print('\nResultado:\n',
                        f'************************************************\n{resultado}\n',
                        '************************************************')
                        return producto_encontrado
                    else:
                        print("Producto no encontrado. intente de nuevo")
                        print(producto_encontrado)
                        return producto_encontrado
            except Exception as e:
                print(f'Error al buscar el producto: {e}')
            finally:
                if conexion:
                    cursor_productos.close()
                    BaseDatos.desconectar()        
    
    def ActualizarProducto(self , id):
        conexion = BaseDatos.conectar()
        producto_encontrado = self.BuscarProductoID(id)
        if producto_encontrado:
            try:
                print('--------------- Escriba los nuevos datos del producto ---------------')
                self.set_id()
                self.set_nombre()
                self.set_descripcion()
                self.set_precio()
                self.set_stock()
                
                nuevo_id = self.get_id()
                nuevo_nombre = self.get_nombre()
                nuevo_descripcion = self.get_descripcion()
                nuevo_precio = self.get_precio()
                nuevo_stock = self.get_stock()
                
                print(f"id: {nuevo_id}")
                print(f"nombre: {nuevo_nombre}")
                print(f"Nueva descripcion: {nuevo_descripcion}")
                print(f"Nuevo precio: {nuevo_precio}")
                print(f"Nuevo stock: {nuevo_stock}")
                
                cursor_producto = conexion.cursor()
                cursor_producto.callproc("ActualizarProducto", [
                    nuevo_id,
                    nuevo_nombre,
                    nuevo_descripcion,
                    nuevo_precio,
                    nuevo_stock
                ])
                conexion.commit()
                cursor_producto.close()
                print("Producto actualizado")
            except Exception as error:
                print(f"Error al actualiza el producto: {error}. Intente de nuevo")
            finally:
                BaseDatos.desconectar()
        else:
            print("Producto no encontrado. intente otra vez")        
    
    def EliminarProducto (self, id):
        conexion = BaseDatos.conectar()
        producto_encontrado = self.BuscarProductoID(id)
        if producto_encontrado:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc("EliminarProducto", [id])
                conexion.commit()
                cursor_producto.close()
                print("Producto eliminado")
            except Exception as error:
                print(f"Error al eliminar producto: {error}. intente de nuevo")
            finally:
                BaseDatos.desconectar()

    @classmethod
    def BuscarProductoNombre(cls):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                producto_encontrado = False
                cursor_producto = conexion.cursor()
                print(f'Buscando producto...')
                cursor_producto.callproc('BuscarProductoNombre')
                for busqueda in cursor_producto.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return producto_encontrado
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(producto_encontrado)
                        return producto_encontrado
            except Exception as e:
                print(f'Error al buscar producto: {e}')
            finally:
                if conexion:
                    cursor_producto.close()
                    BaseDatos.desconectar()
    
    