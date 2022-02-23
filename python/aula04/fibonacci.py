def fibonacci(x):
    a = 1
    b = 1
    if x == 1:
        print('0')
    elif x == 2:
        print('0')
        print('1')
    else:
        print('0')
        print(a)
        print(b)
        for k in range(x-3) :
            seq = a + b
            b = a
            a = seq 
            print(seq)

def main():
    m= int(input('???'))
    fibonacci(m)
   
main()