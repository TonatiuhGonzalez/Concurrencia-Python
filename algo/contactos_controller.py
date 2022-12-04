from contactsView import ContactsView, ContactNew

class ContactsController(object):
    def __init__(self,view):
        self.view = view

    def create_contact(self):
        print("sí jala")
        nuevo_contacto = ContactNew(self.view).show()
    
    def start(self):
        self.view.mainloop()