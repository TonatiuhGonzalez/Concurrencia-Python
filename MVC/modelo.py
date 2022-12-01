import json

class Person(object):

    def __init__(self, first_name = None, last_name = None):
        self.first_name = first_name
        self.last_name = last_name

    #Retorna el nombre de la persona
    def name(self):
        return ("%s %s" % (self.first_name,self.last_name))

    @classmethod
    #Retorna todos los nombres dentro de db.txt como una lista de objetos tipo Persona
    def getAll(self):
        database = open(r'C:\Users\Tonatiuh\Desktop\Python\MVC\db.txt')
        data = json.load(database)
        result = []
        #Por cada elemento en el json, se almacena en el arreglo result
        for item in data:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result