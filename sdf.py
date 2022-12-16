from abc import ABCMeta, abstractmethod
class interfaz_silla(metaclass = ABCMeta):
  @staticmethid
  @abstractmethid
  def crear_silla():
    pass

class sillita(interfaz_silla):
  def __init__(self, ancho, alto, profundo):
    print("Sillita creada")
    self.ancho = ancho
    self.alto = alto
    self.profundo = profundo

  def crear_silla(self):
    return self
  
  def __str__(self):
    return "Ancho {}, alto {}, profundo{}".format(self.ancho, self.alto, self.profundo)

class silla(interfaz_silla):
  def __init__(self, ancho, alto, profundo):
    print("Silla creada")
    self.ancho = ancho
    self.alto = alto
    self.profundo = profundo

  def crear_silla(self):
    return self
  
  def __str__(self):
    return "Ancho {}, alto {}, profundo{}".format(self.ancho, self.alto, self.profundo)

class sillota(interfaz_silla):
  def __init__(self, ancho, alto, profundo):
    print("Sillota creada")
    self.ancho = ancho
    self.alto = alto
    self.profundo = profundo

  def crear_silla(self):
    return self
  
  def __str__(self):
    return "Ancho {}, alto {}, profundo{}".format(self.ancho, self.alto, self.profundo)
class fabrica_sillas:
  @staticmethod
  def crear_silla(alto,ancho,profundo):
    if alto < 400 and ancho < 400 and profundo < 400:
      return sillita(alto, andcho, profundo)
    elif  alto < 1000 and ancho < 1000 and profundo < 1000:
      return silla(alto, andcho, profundo)
    elif  alto < 1500 and ancho < 1500 and profundo < 1500:
      return silla(alto, andcho, profundo)
    else:
      raise Exception("Está muy grande esa silla")