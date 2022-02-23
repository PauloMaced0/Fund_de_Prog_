def isPrime(n):
    print(n)
    for k in range(2,n,1):
        print(k)
        if n % k == 0:
            return False
       
    return True

def main():
    x = int(input('???'))
    isPrime(x)
    if isPrime(x):
        print(x,'é número primo')
    else:
        print(x,'não é número primo')
main()