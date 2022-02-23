def inputFloatList():
    numlist = []
    while True:
        s = input('?')
        if s== '': break
        v = float(s)
        numlist.append(v)
    return numlist

def countLower(numlist):
    valor = float(input('valor???'))
    n = 0
    for k in numlist:
        if valor>k:
            n += 1
            print('O valor',k,'é inferior ao introduzido')
    print('Existem',n,'valores inferiores ao introduzido')

def minmax(lista):
    higest_number=lista[0]
    lowest_number=lista[0]
    for number in lista:
        if number > higest_number:
            higest_number = number
        elif number < lowest_number:
            lowest_number = number
    print('Máximo:',higest_number,'Mínimo:',lowest_number)
    return lowest_number,higest_number

def valmedio(maximo_minimo,lista):
    media_maximo_minimo = (maximo_minimo[0] +maximo_minimo[1] )/2
    print('Média entre o máximo e o mínimo:',media_maximo_minimo)
    lower_than_average = 0
    for x in lista:
        if media_maximo_minimo > x:
            lower_than_average +=1
    print('Quantidade de números inferiores á média:',lower_than_average)
    

def  main():
    lista = inputFloatList()
    print(lista)
    countLower(lista)
    maximo_minimo = minmax(lista)
    valmedio(maximo_minimo,lista)

main()
