imc = float(input('IMC?'))

if imc<18.5:
    cat='Magro'
elif 18.5<=imc<25:
    cat='Saudável'
elif 25<=imc<30:
    cat='Forte'
elif imc>=30:
    cat='Obeso'
    print('Vai correr gordo!!!')
print('Category:',cat)
