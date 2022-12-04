import sqlite3
from contactsView import ContactsView
from contactos_controller import ContactsController

def main():
    with sqlite3.connect("contactos.db") as conn:
        c = conn.cursor()
        c.execute(''' SELECT COUNT(NAME) FROM SQLITE_MASTER WHERE TYPE = 'TABLE' AND NAME = 'CONTACTS' ''')
        if c.fetchone()[0]==1:
            print("Tabla existe!")
            view = ContactsView()
            controller = ContactsController(view)
            view.set_controller(controller)
            controller.start()
        else:
            c.execute(''' CREATE TABLE CONTACTS(
                LAST_NAME TEXT,
                FIRST_NAME TEXT,
                EMAIL TEXT,
                PHONE TEXT
            ) ''')
if __name__ == "__main__":
    main()