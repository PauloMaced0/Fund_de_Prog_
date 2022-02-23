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
    

dictionary_keys = list(letter_dictionary.keys())
dictionary_keys.sort()

for letter in dictionary_keys:
    print(f"{letter} {letter_dictionary[letter]}")
