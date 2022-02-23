import random

def hilo(rand_num):
    n = -1
    number_of_attempts = 0
    while n != rand_num:
        n = int(input('?'))
        number_of_attempts += 1
        if n > rand_num:
            print('Try Lower')
        elif n< rand_num:
            print('Try Higher')
        else:
            print('You Won! Attempted', number_of_attempts, 'times.')
        
def main():
    rand=random.randrange(1,101)
    hilo(rand)
       
main()