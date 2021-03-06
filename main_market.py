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
                print("\n\n")

                cajero = Clases.Empleados.Cajero(nombreCajero, cedulaCajero, telefonoCajero, tipoContratoCajero, sueldoCajero)

                supermercadoDonSergio.AgregarCajero(cajero)
            elif(opcion1 == 2):
                # Agregar Administrador
                nombreAdmin = input("INGRESE NOMBRE DEL ADMINISTRADOR: ")
                cedulaAdmin = input("INGRESE CEDULA DEL ADMINISTRADOR: ")
                telefonoAdmin = input("INGRESE TELEFONO DEL ADMINISTRADOR: ")
                tipoContratoAdmin = input("INGRESE TIPO DE CONTRATO DEL ADMINISTRADOR: ")
                sueldoAdmin = int(input("INGRESE SUELDO DEL ADMINISTRADOR: "))
                print("\n\n")

                administrador = Clases.Empleados.Administrador(nombreAdmin, cedulaAdmin, telefonoAdmin, tipoContratoAdmin, sueldoAdmin)

                supermercadoDonSergio.AgregarAdministrador(administrador)
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

            print("\n\n")
            supermercadoDonSergio.AgregarProducto(nuevoProducto)
            print(nuevoProducto)
            print("\n\n")
        elif(opcion == 3):
            # Realizar una venta con su Factura       
            productosVenta = []
            vender = 0
            totalVenta = 0 
            # LOGICA DE  VENTA DE PRODUCTOS
            while vender == 0:
                print("""
                ###################### LISTA DE PRODUCTOS #######################
                """)
                for producto in supermercadoDonSergio.productos:
                    print('\t\t'+str(producto.id) + ' - ' + producto.nombre)
                print("""
                #################################################################
                """)
                print("\n\n")
                idProductoVenta = int(input("INGRESE EL ID DEL PRODUCTO A COMPRAR: "))
                cantidadProductoVenta = int(input("INGRESE LA CANTIDAD DEL PRODUCTO A COMPRAR: "))
                
                valorProductoVenta = supermercadoDonSergio.VenderProducto(idProductoVenta, cantidadProductoVenta)

                nombreProductoVenta = ''
                for producto in supermercadoDonSergio.productos:
                    if(producto.id == idProductoVenta):
                        nombreProductoVenta = producto.nombre

                productoVenta = [nombreProductoVenta,cantidadProductoVenta,valorProductoVenta]
                productosVenta.append(productoVenta)
                totalVenta += valorProductoVenta

                vender = int(input("SI DESEA SEGUIR COMPRANDO DIGITE (0), DE LO CONTRARIO (1): "))
            
            print("""
            ###################### LISTA DE EMPLEADOS ######################
            """)

            for emp in supermercadoDonSergio.empleados:
                if(isinstance(emp, Clases.Empleados.Cajero)):
                    print(str(emp.cedula) + ' - ' + str(emp.nombre))

            print("""
            #################################################################
            """)
            
            cedulaCliente = input("INGRESE LA CEDULA DEL CLIENTE: ")
            cajeroVenta = input("INGRESE LA CEDULA DEL CAJERO QUE LO ATENDIO: ")

            for emp in supermercadoDonSergio.empleados:
                if(isinstance(emp,Clases.Empleados.Cajero)):
                    if(emp.cedula == cedulaCliente):
                        emp.total_ventas += totalVenta
            
            supermercadoDonSergio.totalVentas += totalVenta

            # FACTURA DE VENTA
            print("""
            ###################### FACTURA VENTA ############################
                CC :        \t{}
                CAJERO :    \t{}
            """.format(cedulaCliente,cajeroVenta))
            print("""
            ################### PRODUCTOS VENDIDOS ##########################
            """)
            print("""
                PRODUCTO - CANTIDAD - VALOR
            """)
            for producto in productosVenta:
                print(str(producto[0]) + ' - ' + str(producto[1]) + ' - ' + str(producto[2]))
            print("""
            #################################################################
            """)
            print("""
                TOTAL VENTA: \t{}
            #################################################################
            """.format(totalVenta))

        elif(opcion == 4):
            # Conocer el total de ventas
            if(supermercadoDonSergio.totalVentas == 0):
                print("NO SE HA REALIZADO NINGUNA VENTA")
            else:
                print("TOTAL DE VENTAS DEL SUPERMERCADO: " + str(supermercadoDonSergio.totalVentas))
        elif(opcion == 5):
            # Conocer lista de los empleados
            print("""
            ###################### LISTA DE EMPLEADOS ######################
            """)
            for empleado in supermercadoDonSergio.empleados:
                print(empleado)
            print("""
            #################################################################
            """)
            print("\n\n")
        elif(opcion == 6):
            # Conocer los productosConocer los productos
            print("""
            ###################### LISTA DE PRODUCTOS #######################
            """)
            for producto in supermercadoDonSergio.productos:
                print(producto)
            print("""
            #################################################################
            """)
            print("\n\n")
        elif(opcion == 7):
            # Conocer el sueldo de los empleados actual
            print("""
            ################# LISTA DE EMPLEADOS-SUELDOS ####################
            """)
            for emp in supermercadoDonSergio.empleados:
                sueldoEmp = emp.CalcularSueldo()
                print("\t\t" + emp.nombre + " - " + emp.cedula + " - $"+ str(sueldoEmp))
            print("""
            #################################################################
            """)




if __name__ == "__main__":
    main()