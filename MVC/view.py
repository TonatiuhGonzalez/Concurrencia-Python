#Bienvenida
def startView():
    print ('Ejemplo MVC de lectura de un txt')
    print ('¿Quiére leer los datos del txt?[y/n]')

#Resultado
def showAllView(list):
    print ('En la pseudo base de datos hay %i personas. Los nombres son:' % len(list))
    for item in list:
        print (item.name())

#En caso de negación
def endView():
    print ('¡Adios!')