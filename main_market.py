import Clases.Empleados
import Clases.Productos
import Clases.Supermercado



def main():
    supermercadoDonSergio = Clases.Supermercado.Supermercado("Don Sergio", "Cr 96 I # 16 F 17", "3057752461")
    opcion = 0
    incrementalIdProducto = 0
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
            opcion1 = int(input("""
            INGRESE EL TIPO DE EMPLEADO QUE DESEA AGREGAR: 
            1) CAJERO
            2) ADMINISTRADOR
            """))

            if(opcion1 == 1):
                # Agregar Cajero
                nombreCajero = input("INGRESE NOMBRE DEL CAJERO: ")
                cedulaCajero = input("INGRESE CEDULA DEL CAJERO: ")
                telefonoCajero = input("INGRESE TELEFONO DEL CAJERO: ")
                tipoContratoCajero = input("INGRESE TIPO DE CONTRATO DEL CAJERO: ")
                sueldoCajero = int(input("INGRESE SUELDO DEL CAJERO: "))

                cajero = Clases.Empleados.Cajero(nombreCajero, cedulaCajero, telefonoCajero, tipoContratoCajero, sueldoCajero)

                supermercadoDonSergio.AgregarCajero(cajero)
            elif(opcion1 == 2):
                # Agregar Administrador
                nombreAdmin = input("INGRESE NOMBRE DEL ADMINISTRADOR: ")
                cedulaAdmin = input("INGRESE CEDULA DEL ADMINISTRADOR: ")
                telefonoAdmin = input("INGRESE TELEFONO DEL ADMINISTRADOR: ")
                tipoContratoAdmin = input("INGRESE TIPO DE CONTRATO DEL ADMINISTRADOR: ")
                sueldoAdmin = int(input("INGRESE SUELDO DEL ADMINISTRADOR: "))

                administrador = Clases.Empleados.Administrador(nombreAdmin, cedulaAdmin, telefonoAdmin, tipoContratoAdmin, sueldoAdmin)

                supermercadoDonSergio.AgregarCajero(administrador)
            else:
                print("OPCION INCORRECTA VUELVA !!")
        elif(opcion == 2):
            # Agregar Producto
            incrementalIdProducto += 1

            idProducto = incrementalIdProducto
            nombreProducto = input("""INGRESE EL NOMBRE DEL PRODUCTO: """)
            precioProducto = int(input("""INGRESE EL PRECIO DEL PRODUCTO: """))
            cantidadProducto = int(input("""INGRESE LA CANTIDAD DEL PRODUCTO: """))
            banderaDescuento = int(input("""SI QUIERE AGREGAR DIGITE 1 (SI) Y 0 (NO): """))
            
            nuevoProducto = Clases.Productos.Producto(idProducto, nombreProducto, precioProducto, cantidadProducto)

            if(banderaDescuento == 1):
                descuentoProducto = int(input("""INGRESE EL DESCUENTO DEL PRODUCTO: """))
                nuevoProducto.AgregarDescuento(descuentoProducto)

            supermercadoDonSergio.AgregarProducto(nuevoProducto)
            print(nuevoProducto)
        elif(opcion == 3):
            # Realizar una venta con su Factura
            pass
        elif(opcion == 4):
            # Conocer el total de ventas
            pass
        elif(opcion == 5):
            # Conocer lista de los empleados
            print("""
            ###################### LISTA DE EMPLEADOS ######################
            """)
            for empleado in supermercadoDonSergio.empleados:
                print(empleado)
            print("\n\n")
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