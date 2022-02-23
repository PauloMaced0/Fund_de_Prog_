nexemplares =int(input('Quantidade de exemplares?'))

preçoexemplares = 24.95*nexemplares
tax = 0.20*nexemplares
lucro = 0.12*nexemplares
impostos = (0.23*24.95)*nexemplares

print('Para {} exemplares houve lucro de {}€,coletado em impostos a quantia de {}€ e em taxas {}€'.format(nexemplares,lucro,impostos,tax))