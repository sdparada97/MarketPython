import Clases.Empleados
import Clases.Productos
import Clases.Supermercado



def main():
    opcion = 0
    while(opcion < 8):
        opcion = int(input(
            """
            ###############################################################
            ##                                                           ##
            ##   ###   ###    ###    #####   ##    # ######  ##########  ##
            ##   ##  #  ##  ##   ##  ##   #  ##  #   ##          ##      ##
            ##   ##     ##  ## # ##  ##   #  ###     ## ##       ##      ##
            ##   ##     ##  ##   ##  ## ##   ## #    ##          ##      ##
            ##   ##     ##  ##   ##  ##  ##  ##   #  ######      ##      ##
            ##                                                           ##
            ###############################################################

            ELIJA UNA DE LAS SIGUIENTES OPCIONES:
            1) Agregar Empleado
            2) Agregar Producto
            3) Realizar una venta con su Factura
            4) Conocer el total de ventas
            5) Conocer lista de los empleados
            6) Conocer los productos
            7) Conocer el sueldo de los empleados actual
            8) Salir

            """))

        if(opcion == 1):
            # Agregar Empleado
            pass
        elif(opcion == 2):
            # Agregar Producto
            pass
        elif(opcion == 3):
            # Realizar una venta con su Factura
            pass
        elif(opcion == 4):
            # Conocer el total de ventas
            pass
        elif(opcion == 5):
            # Conocer lista de los empleados
            pass
        elif(opcion == 6):
            # Conocer los productosConocer los productos
            pass
        elif(opcion == 7):
            # Conocer el sueldo de los empleados actual
            pass




if __name__ == "__main__":
    main()
"""
cajero1 = Clases.Empleados.Cajero("SERGIO","1016095700","3057752461","INDEFINIDO",1500000,0)
print(cajero1)
print("\n TIPO DE EMPELADO: ", type(cajero1))-
producto1.AgregarDescuento(10)
print(producto1)
"""