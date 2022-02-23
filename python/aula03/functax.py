def tax(r):
    if r<=1000:
        ram=0.1*r
        return ram
    elif 1000<r<=2000:
        ram=0.2*r-100
        return ram
    else:
        ram=0.3*r-300
        return ram
def main():
    valor = float(input('r= ?'))

    res = tax(valor)
    print('Resultado:',res)

main()