def divisores(n):
    assert n>0
    divisor = 0
    if n==1:
        print(n,'é número perfeito')
    else:
        for k in range(1,n):
            if n % k == 0:
                soma = divisor + k
                divisor = soma
                print(k)
        if soma == n:
            print(n,'é número perfeito')
        elif soma < n:
            print(n,'é número deficiente')
        else:
            print(n,'é número abundante')
def main():
    x = int(input('???'))
    divisores(x)

main()




