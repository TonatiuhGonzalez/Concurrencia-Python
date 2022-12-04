import tkinter as tk
import tkinter.messagebox as mb

class ContactosForm(tk.LabelFrame):
    campos = ("Last name", "First name", "Email", "Phone")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Contacts",padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.campos = list(map(self.create_campo, enumerate(self.campos)))
        self.button_save

    def create_campo(self,campo):
        posicion, texto = campo
        label = tk.Label(self.frame, text=texto)
        entry = tk.Entry(self.frame)
        label.grid(row = posicion, column = 0, pady = 10)
        entry.grid(row = posicion, column = 1, pady = 10)
        return entry

class ContactNew(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.form = ContactosForm(self)
        self.form.pack(padx = 10, pady = 10)
        self.button_add = tk.Button(self, text = "Agregar Contacto", command=self.confirm)
        self.button_add.pack()

    def show(self):
        self.grab_set()
        self.wait_window()

    def confirm(self):
        print('Contacto confirmado!')

class ContactsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LISTA DE CONTACTOS")
        self.geometry('500x500')
        self.button_new = tk.Button(self, text="New Contact")
        self.button_new.pack(side=tk.BOTTOM, pady=5)

    def set_controller(self,controller):
        self.button_new.config(command = controller.create_contact)