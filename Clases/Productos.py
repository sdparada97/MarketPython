
# CLASE -----------> PRODUCTO
class Producto:

    descuento = 0
    precioDescuento = 0

    #Constructor -----> PRODUCTO
    def __init__(self,nombre, precio_valor, cantidad):
        self.nombre = nombre
        self.precio_valor = precio_valor
        self.cantidad = cantidad

    #Metodos -----> PRODUCTO
    def PrecioConDescuento(self,descuento):
        valorDescuento = self.precio_valor * self.descuento
        self.precioDescuento = self.precio_valor - valorDescuento
    
    def AgregarDescuento(self,descuento):
        if( descuento>=0 and descuento<=50):
            self.descuento = descuento/100
            self.PrecioConDescuento(descuento)
        else:
            print("ESE PORCENTAJE NO SE ENCUENTRA DENTRO DEL RANGO (0 % - 50 %)")

    def __str__(self):
        str_producto = ""
        if(self.descuento != 0):
            str_producto = """
        NOMBRE:                 \t{}
        PRECIO:                 \t{}
        CANTIDAD:               \t{}
        DESCUENTO:              \t{}%
        PRECIO CON DESCUENTO:   \t{}""".format(self.nombre,self.precio_valor,self.cantidad,self.descuento*100,self.precioDescuento)
        else:
            str_producto = """
        NOMBRE:               \t{}
        PRECIO:               \t{}
        CANTIDAD:             \t{}""".format(self.nombre,self.precio_valor,self.cantidad)
        
        return str_producto

