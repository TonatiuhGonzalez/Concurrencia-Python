import sqlite3
from contactsView import ContactsView
from contactos_controller import ContactsController
from contactos_repository import ContactsRepository

def main():
    with sqlite3.connect("contactos.db") as conn:
        c = conn.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = 'CONTACTS' ''')

        if c.fetchone()[0]==1:
            print("Tabla existe!")
            repo = ContactsRepository(conn)
            view = ContactsView()
            controller = ContactsController(repo,view)
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