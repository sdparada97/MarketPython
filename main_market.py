import Clases.Empleados
import Clases.Productos

cajero1 = Clases.Empleados.Cajero("SERGIO","1016095700","3057752461","INDEFINIDO",1500000,0)
print(cajero1)

producto1 = Clases.Productos.Producto("LIBRO: EL PRINCIPITO", 45000, 20)
producto1.AgregarDescuento(10)
print(producto1)