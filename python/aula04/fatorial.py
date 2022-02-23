def factorial(n):
    assert isinstance(n, int), "n should be an int"
    assert n >= 0            , "n should not be negative"
    fator=1
    for k in range(1,n+1):
        fator=fator*k
        
    return fator
def main():
    x=int(input('fatorial de ?'))
    fact=factorial(x)
    print('Fatorial de {}! : {}'.format(x,fact))

main()
