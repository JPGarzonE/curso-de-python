from contact import Contact
import csv

class ContactBook:

    def __init__(self):
        self._contacts = []

    def addContact(self, name, phone, email):
        contacto = Contact(name, phone, email)
        self._contacts.append(contacto)
        print("¡Contacto Agregado!")
        self._saveContacts()

    def showAllContacts(self):
        for contact in self._contacts:
            self._printContact(contact)

    def deleteContact(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact._name == name:
                del self._contacts[idx];
                print("¡Contacto Eliminado!")
                self._saveContacts()
                break
        else:
            print("Contacto NO encontrado :/")

    def searchContact(self, name):
        for contact in self._contacts:
            if contact._name == name:
                self._printContact(contact)
        else:
            print("Contacto NO encontrado :/")

    def updateContact(self, name, phone, email):
        contactToUpdate = None

        for contact in self._contacts:
            if contact._name == name:
                contactToUpdate = contact
                break

        if contactToUpdate == None:
            print("Contacto NO encontrado")
        else:
            contactToUpdate._phone = phone
            contactToUpdate._email = email
            print("¡Contacto Actualizado!")
            self._saveContacts()
            self._printContact(contactToUpdate)

    def _printContact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        #llamar a una variable con sintaxis privada _<nombre variable>
        #es una mala practica ya que aunque el lenguaje lo permite, no debería ser llamada
        print('Nombre: {}'.format(contact._name))
        print('Teléfono: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _saveContacts(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact._name, contact._phone, contact._email) )
