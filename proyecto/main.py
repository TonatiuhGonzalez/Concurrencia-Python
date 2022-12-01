from empleado import Gerente
from empleado import Tecnico
from empleado import Gestora
from empleado import Administrador
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from reportes import ReporteProgramacion
from progamación import Matutino
from progamación import Vespertino

empleados = [
    Gerente("Roberto", "Pérez", "$20,000.00",Matutino()),
    Gestora("Alejandra", "Ruíz", "$8,000.00",Matutino()),
    Gestora("Selene",  "Rodríguez", "$8,000.00",Matutino()),
    Tecnico("Artemio", "López", "$9,000.00",Vespertino()),
    Tecnico("Salvador",  "Juárez",  "$9,000.00",Vespertino()),
    Tecnico("Rolando", "Jiménez",  "$9,000.00",Matutino()),
    Administrador("Marco", "Sánchez",  "$15,000.00",Matutino())
]

reporte=[
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]

for r in reporte:
    r.print_reporte()