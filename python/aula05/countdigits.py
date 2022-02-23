
def countdigits(digits):
    number_digits = 0
    for digit in digits:
        if digit.isdigit():
            number_digits += 1
    return number_digits

def main():
    x = str(input('?'))
    tuplestring = tuple(x)
    print(tuplestring) 
    print(countdigits(tuplestring))
main()