from modelo import Person
import view

def start():
    #Llamado al método de la vista
    view.startView()
    seleccion = input()
    if seleccion == 'y':
        #Llama al método dentro del mismo controlador
        return showAll()
    #Llama la despedida en la vista
    elif seleccion =='n':
        return view.endView()

def showAll():
    #Obtiene la lista de todos los objetos de tipo persona llamando al modelo
    people_in_db = Person.getAll()
    #Llama a la vista para mostrar los nombres
    return view.showAllView(people_in_db)

if __name__ == "__main__":
    #Función para correr el controlador
    start()