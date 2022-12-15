from contactsView import ContactsView, ContactNew

class ContactsController(object):
    def __init__(self,repo,view):
        self.view = view
        self.repo = repo
        self.contacts = list(repo.get_contacts())

    def create_contact(self):
        print("sí jala")
        nuevo_contacto = ContactNew(self.view).show()
        if nuevo_contacto:
            print("contacto nuevo")
            contact = self.repo.add_contact(nuevo_contacto)
            self.contacts.append(contact)
            self.view.add_contact(contact)
    
    def start(self):
        self.view.mainloop()
        for c in self.contacts:
            self.view.add_contact(c)
        self.view.mainloop()

    def select_contact(self, index):
        self.selection = index
        contact = self.contacts[index]
        self.view.load_details(contact)

    def update_contact(self):
        print("Función update_contact")
        if not self.selection:
            return
        rowid = self.contacts[self.selection].rowid
        update_contact = self.view.get_data()
        update_contact.rowid=rowid

        contact = self.repo.update_contact(update_contact)
        self.contacts[self.selection]=contact
        self.view.update_contact(contact,self.selection)

    def delete_contact(self):
        print("Función delete_contact")
        if not self.selection:
            return
        contact = self.contacts[self.selection]
        self.repo.delete_contact(contact)
        self.view.remove_contact(self.selection)