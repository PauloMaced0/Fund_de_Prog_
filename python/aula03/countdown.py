def countdown(N):
    print(N)
    if N>0:
        N -= 1
        return countdown(N)
    else:
        exit(1)
def main():
    n =int(input('número?'))
    
    num = countdown(n)
    print(num)

main()

