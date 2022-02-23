'''*No programa polynomial.py pretendemos definir uma função que crie um
polinómio de segundo grau arbitrário. Ou seja, p=polynomial2(2,-1,3) deve
colocar em p uma função tal que p(x) calcule o valor p(x) =
2x^2 - x + 3
para qualquer valor x que lhe seja passado. Note que sempre que polynomial2 é
executada, terá de definir uma nova função para devolver. Essa definição poderá ser feita
com uma instrução def ou com uma expressão lambda.'''

# COMPLETE a função abaixo.
# Veja os exemplos de utilização e resultados esperados.

# polynomial2(a,b,c) deve devolver uma função f tal que
# f(x) seja o polinómio de segundo grau ax²+bx+c.
import string


def polynomial2(a, b, c):
    return lambda x: a*(x**2) + b*x + c


# DESAFIO EXTRA:
# Crie uma versão generalizada que cria polinómios de qualquer grau.
# (Não é tão fácil com expressões lambda.)

# polynomial(a), onde a=[a0, a1, ..., an], deve devolver uma função f tal que
# f(x) seja o polinómio a0*x**n + a1*x**(n-1) + ... + an.
def polynomial(coefs):
    def f(x):
        sum = 0
        n = len(coefs) - 1
        i = 0
        while n >= 0:
            sum += coefs[i]*(x**n)
            n-=1
            i+=1
        return sum
    return f    

        

def main():
    xx = [0, 1, 2, 3]   # Valores de x a testar

    print("\nTestes à função polynomial2:")
    p = polynomial2(1, 2, 3)    # creates p(x)=x²+2x+3
    print([p(x) for x in xx])   # [3, 6, 11, 18]

    q = polynomial2(2, 0, -2)   # creates q(x)=2x²-2
    print([q(x) for x in xx])   # [-2, 0, 6, 16]

    print("\nTestes à função polynomial:")
    r = polynomial([1, 2, 3])   # same as p(x)
    print([r(x) for x in xx])   # [3, 6, 11, 18]

    s = polynomial([1, -1, 0, 100])     # creates s(x)=x³-x²+100
    print([s(x) for x in xx])           # [100, 100, 104, 118]

if __name__ == "__main__":
    main()

