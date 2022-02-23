def short(string):
    for letter in string:
        if letter.isupper():
            print(letter, end='')
    
    print()

def main():
    x= str(input('?'))
    tuplestring = tuple(x)
    short(tuplestring)
main()