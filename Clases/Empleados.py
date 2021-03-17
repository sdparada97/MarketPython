from abc import ABC, abstractmethod

# CLASE ABSTARCTA -----------> EMPLEADO
class Empleado(ABC):
    # Constructor -------> EMPLEADO abstracta
    def __init__(self, nombre, cedula, telefono, tipo_contrato, sueldo):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.tipo_contrato = tipo_contrato
        self.sueldo = sueldo
        super().__init__()

    # Metodos -------> EMPLEADO abstracta
    @abstractmethod
    def CalcularSueldo(self):
        pass

# CLASE -----------> CAJERO
class Cajero(Empleado):

    total_ventas = 0

    #Constructor -----> PRODUCTO
    def __init__(self,nombre, cedula, telefono, tipo_contrato, sueldo):
        super().__init__(nombre, cedula, telefono, tipo_contrato, sueldo)

    #Metodos -----> PRODUCTO
    def CalcularSueldo(self):
        return self.sueldo + (self.totalVentas*0.10)
    
    def __str__(self):
        return """
        NOMBRE:             \t{}
        CEDULA:             \t{}
        TELEFONO:           \t{}
        TIPO_CONTRATO:      \t{}
        SUELDO:             \t{}
        NUMERO DE VENTAS:   \t{}""".format(self.nombre,self.cedula,self.telefono,self.tipo_contrato,self.sueldo,self.numero_ventas)

# CLASE -----------> CAJERO
class Administrador(Empleado):

    empleadosACargo = []

    #Constructor -----> PRODUCTO
    def __init__(self,nombre, cedula, telefono, tipo_contrato, sueldo):
        super().__init__(nombre, cedula, telefono, tipo_contrato, sueldo)
        

    #Metodos -----> PRODUCTO
    def CalcularSueldo(self):
        return self.sueldo
    
    def AgregarEmpleadoACargo(self,Empleado):
        self.empleadosACargo.append(Empleado)
    
    def __str__(self):
        return """
        NOMBRE:             \t{}
        CEDULA:             \t{}
        TELEFONO:           \t{}
        TIPO_CONTRATO:      \t{}
        SUELDO:             \t{}
        NUMERO DE VENTAS:   \t{}""".format(self.nombre,self.cedula,self.telefono,self.tipo_contrato,self.sueldo,self.numero_ventas)
