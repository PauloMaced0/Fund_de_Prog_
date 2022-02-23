filelus = 'lusiadas.txt'
letter_dictionary = {}

with open(filelus, "r") as file:
    char = file.read(1)
    while char:
        if char.isalpha():
            char = char.lower()

            if char in letter_dictionary:
                letter_dictionary[char] += 1
            else:
                letter_dictionary[char] = 1
        
        char = file.read(1)
    
sorted_items = sorted(letter_dictionary.items(), key= lambda repetition : repetition[1], reverse=True)

for letter,repeat in sorted_items:
    print(f"{letter} {repeat}")