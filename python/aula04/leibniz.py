import math

def seq(n):
    #print(n)
    sequencia = 1
    for k in range(1,n+1):
        #print(k)
        sequencia += math.pow(-1,k) / (2*k+1)
        #print(sequencia)
    return sequencia    
       

def main():
    x = int(input('???'))
    seque=seq(x)
    print(seque)

main()