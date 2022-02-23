# *O ficheiro wordlist.txt contém uma lista de palavras
# de língua inglesa, por ordem. Leia essas palavras para 
# uma lista e, usando uma função de pesquisa binária 
# (do módulo bisect), descubra quantas palavras começam
# por “ea”, sem ter de percorrer tudo.
# Sugestão: procure a primeira palavra com “ea” e 
# a primeira com “eb” e subtraia os índices. E quantas 
# palavras começam por “tb”? Nenhuma? Então qual é 
# primeira letra,maior que ‘b’, que ocorre após um “t”,
# nas palavras inglesas?

import bisect   #bisect.bisect_left(lst, valor)

file = 'wordlist.txt'

with open(file, 'r') as f:
    wordlist = f.read().split()
    firstWord = bisect.bisect_left(wordlist, 'ea')
    lastWord = bisect.bisect_left(wordlist, 'eb')
    tbwords = bisect.bisect_left(wordlist, 'tb')
    tbwords2 = bisect.bisect_left(wordlist, 'tc')
    word = wordlist[tbwords]

print("ea - eb: ",-(firstWord - lastWord), '\n')
print("Amount of 'tb' words:", tbwords - tbwords2, '\n')
print("1st letter after higher than b that occurs after 't' :", word[1], '\n')

print(wordlist[firstWord])


