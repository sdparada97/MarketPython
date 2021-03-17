import Clases.Empleados
import Clases.Productos

# CLASE -----------> SUPERMERCADO
class Supermercado:

    totalVentas = 0;
    empleados=[]
    productos=[]
    facturas=[]

    #Constructor -----> SUPERMERCADO
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    #Metodos -----> SUPERMERCADO
    def AgregarCajero(self,cajero):
        self.empleados.append(cajero)
    
    def AgregarProducto(self,producto):
        self.productos.append(producto)
    
    def VenderProducto(self,idProducto,cantidadProductoVendido):
        valorVenta = 0
        for prod in self.productos:
            if(prod.id == idProducto):
                if(prod.cantidad == 0):
                    print("NO HAY STACK DEL PRODUCTO")
                elif(prod.cantidad >= cantidadProductoVendido):
                    #LOGICA DE CANTIDAD DE PRODUCTO VENDIDO
                    prod.cantidad = prod.cantidad - cantidadProductoVendido

                    #LOGICA DE VENTA PRODUCTO 
                    if(prod.precioDescuento == 0):
                        valorVenta = cantidadProductoVendido * prod.precio_valor
                    else:
                        valorVenta = cantidadProductoVendido * prod.precioDescuento

                else:
                    print("LA CANTIDAD EXCEDE A LA QUE HAY. STACK(\t{})".format(prod.cantidad))
        return valorVenta
        

    
    def AgregarAdministrador(self,administrador):
        flatAdmin = False
        for emp in self.empleados:
            if(type(emp) == 'Clases.Empleados.Administrador'):
                flatAdmin = True
                print("YA EXISTE UN ADMINISTRADOR DENTRO DEL SUPERMERCADO")
        
        if(flatAdmin == False):
            self.empleados.append(administrador)

    def __str__(self):
        return """ 
        NOMBRE:         \t{}
        DIRECCION:      \t{}
        TELEFONO:       \t{}""".format(self.nombre,self.direccion,self.telefono)