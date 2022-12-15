class Empleado:
    def __init__(self,nombre, apellido, salario, horario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.horario = horario
      

    def get_nombre_completo(self):
        return f'{self.nombre}, {self.apellido}'

class Gerente(Empleado):
    puesto = "Gerente General"

class Tecnico(Empleado):
    puesto = "Tecnico"

class Gestora(Empleado):
    puesto = "Gestora de Cobranza"

class Administrador(Empleado):
    puesto = "Administrador de Servicios de Cable"
