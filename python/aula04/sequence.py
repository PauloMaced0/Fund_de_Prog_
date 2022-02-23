def inputTotal():
    tot = 0.0
    number_inputs = 0
    while True:
        s = input("valor? ")
        if s == "": break   # if empty line, stop repeating!
        number_inputs += 1
        v = float(s)
        tot = tot + v        
        media = tot/number_inputs
    return media

# MAIN PROGRAM
tot = inputTotal()
print(tot)