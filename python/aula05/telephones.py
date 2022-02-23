##Complete a função telToName que, dado um número de telefone (e as duas listas),
#devolve o nome respetivo (ou o próprio número, se não estiver na lista). Isto é o que
#os telemóveis fazem quando recebem uma chamada.
def telToName(tel, telList, nameList):
    if tel in telList:
        tele = telList.index(tel)
        
        name = nameList[tele]
    else:
        name = tel
    
    return name


#Complete a função nameToTels que, dada parte de um nome, devolve a lista dos
#números correspondentes a nomes que incluem essa parte. (Como quando pesquisa na
#lista de contactos do telemóvel.)
def nameToTels(partName, telList, nameList):
    return_values = []

    for i in range(len(nameList)):
        if nameList[i][:len(partName)].lower() == partName.lower():
            return_values.append(telList[i])

    return return_values

def main():
    # Lists of telephone numbers and names
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    # Test telToName:
    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    print( telToName('234000111', telList, nameList) == "Brad" )
    print( telToName('222333444', telList, nameList) == "222333444" )

    # Test nameToTels:
    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    print( nameToTels('Clau', telList, nameList) == ['777888333'] )
    print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )


if __name__ == "__main__":
    main()