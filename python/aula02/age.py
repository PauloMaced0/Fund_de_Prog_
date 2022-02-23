age = int(input('Age?'))

if age < 0:
    print('ERROR: invalid age!')
    exit(1) # termina a execução do programa
print('Age:',age)
if age <= 13:
    cat = 'child'
elif 13<age<20:
    cat = 'teenager'
else:
    cat= 'adult'

print('Category:',cat)


    