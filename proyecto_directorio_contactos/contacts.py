from contactBook import ContactBook
import csv

def run():

    contactBook = ContactBook()

    try:
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue;

                contactBook.addContact( row[0], row[1], row[2] )


    except FileNotFoundError:
        f = open('contacts.csv', 'w')
        f.close()

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str( input("Nombre del contacto: ") )
            phone = str( input("Celular del contacto: ") )
            email = str( input("Email del contacto: ") )

            contactBook.addContact(name, phone, email)

        elif command == 'ac':
            name = str( input("Nombre del contacto: ") )
            phone = str( input("Nuevo celular del contacto: ") )
            email = str( input("Nuevo email del contacto: ") )

            contactBook.updateContact(name, phone, email)

        elif command == 'b':
            name = str( input("Nombre del contacto: ") )

            contactBook.searchContact(name)

        elif command == 'e':
            nameToDelete = str( input("Nombre del contacto: ") )
            contactBook.deleteContact(nameToDelete)

        elif command == 'l':
            contactBook.showAllContacts()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
