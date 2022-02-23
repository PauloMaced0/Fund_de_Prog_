def max2(x,y):
    print(x, y)
    if x>y:
        return x
    else:
        return y

def max3(x, y, z):
    return max2(x, max2(y, z))

def main():
    valorx = float(input('x = ?'))
    valory = float(input('y = ?'))
    valorz = float(input('z = ?'))

    valormax=max2(valorx,valory)
    print('Valor máximo: ',valormax)

    print("Valor máximo entre 3:", max3(valorx, valory, valorz))

    
main()