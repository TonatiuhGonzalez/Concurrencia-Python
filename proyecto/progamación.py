import datetime
class Programacion:
    def get_programacion_info(self):
        return f'{self._hora_entrada:%H:%M} - {self._hora_salida:%H:%M}'

class Matutino(Programacion):
    _hora_entrada = datetime.time(8,00)
    _hora_salida = datetime.time(16,00)

class Vespertino(Programacion):
    _hora_entrada = datetime.time(12,00)
    _hora_salida = datetime.time(20,00)