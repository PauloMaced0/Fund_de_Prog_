l=float(input('Litros?'))

if l<= 40:
    preco = 1.40*l
    print('Valor a pagar:{:5.2f}€'.format(preco))
else:
    preco = 1.40*l
    desconto = 0.10*preco
    precodes = preco - desconto
    print('Valor a pagar:{:5.2f}€'.format(precodes))

