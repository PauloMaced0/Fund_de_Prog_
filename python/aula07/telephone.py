# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def add_contact(dic):
    name = str(input('Name?'))
    number = int(input('Phone Number?'))

    dic[str(number)] = name
    print('ADDED!!!')
    return dic

def remove_contact(dic):
    number = int(input('Number to remove?'))

    if str(number) in dic.keys():
        dic.pop(str(number))
        print('REMOVED!!!')
    else:
        print('Not a number on the list of contacts')

    return dic
def find_number(dic):
    number = int(input('Find contact name by number:'))

    if str(number) in dic.keys():
        print('Nome:')
        return dic[str(number)]
    else:
        print('Could not find the number')


def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    ret_dictionary = {}
    for contact, name in contacts.items():
        if partName in name:
            ret_dictionary[contact] = name

    return ret_dictionary


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    partname = 'Mar'

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print('Contactos:')
            listContacts(contactos)
        elif op == 'A':
            add_contact(contactos)
        elif op == 'R':
            remove_contact(contactos)
        elif op == 'N':
            print(find_number(contactos))
        elif op == 'P':
            print('Contactos:')
            print(filterPartName(contactos,partname))
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()
