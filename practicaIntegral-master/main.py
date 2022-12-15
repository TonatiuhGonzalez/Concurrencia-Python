from empleado import Gerente
from empleado import Tecnico
from empleado import Gestora
from empleado import Administrador
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from programacion import Matutino
from programacion import Vespertino
from reportes import ReporteProgramacion

empleados = [
    Gerente("Roberto", "perez", "$20,000.00", Matutino()),
    Gestora("Alejandra", "ruiz", "$8,000.00", Matutino()),
    Gestora("Selene",  "rodriguez", "$8,000.00", Matutino()),
    Tecnico("Artemio", "lopez", "$9,000.00", Vespertino()),
    Tecnico("Salvador",  "Juarez",  "$9,000.00", Vespertino()),
    Tecnico("Rolando", "Jimenez",  "$9,000.00", Matutino()),
    Administrador("Marco", "Sanchez",  "$15,000.00", Matutino())
]

reportes=[
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]

for r in reportes:
    r.print_reporte()

    