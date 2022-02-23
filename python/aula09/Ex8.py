'''**A funçãof(x) = x + sin(10x)(ver gráfico abaixo) tem uma raiz (um zero) no
intervalo [0.2, 0.4]. Sabemos isso porque é uma função contínua e muda de sinal entre os
extremos desse intervalo, já que f(0. 2) > 0 ∧ f(0. 4) < 0(teorema de Bolzano).'''

'''Implemente uma função findZero(func, a, b, tol) que ache um zero de uma
função func usando o método da bissecção. Trata-se de um método de aproximações
sucessivas que, em cada iteração, vai reduzindo o intervalo [a, b] que contém a raiz
para metade. Quando a amplitude do intervalo for inferior à tolerância pretendida, tol,
paramos e devolvemos [a, b]. Isto é uma forma de pesquisa binária, mas em vez de
pesquisar uma lista, tem de “pesquisar” uma função real de variável real.'''

from cmath import sin
import math


def findZero(func,a,b,tol):
    if (func(a) * func(b))>0:
        print("\n\nNão existe uma raíz real nos intervalos dados")
    else:
        while abs(a-b) > tol:
            mid = (a + b) / 2
            funcMid = func(mid)
            if funcMid==0:
                return mid
            elif (func(a) * funcMid) < 0:
                b = mid
            else:
                a = mid
        return (a+b)/2


funct = lambda x: x+ math.sin(10*x)
a = float(input("\nExtremo esquerdo do intervalo: "))
b = float(input("Extremo direito do invervalo: "))
print ('\n', findZero(funct, a, b, 0.001), '\n')
        