import math

def primesUpTo(n):
    set_numbers = set({})
    for  number in range(2,n+1):    
        set_numbers.add(number) 
    

    for number in range(2,math.ceil(math.sqrt(n))):

        for i in range(number*number, n+1, number):
            if i in set_numbers:    
                set_numbers.remove(i)

    return set_numbers

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)
    
    # Do some checks:
    assert primesUpTo(30) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

