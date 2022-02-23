'''*Usando o mesmo princípio, faça uma função que indique todas as letras que podem
suceder a um certo prefixo. Pode usar esta função num sistema de escrita inteligente que
vai apresentando as letras possíveis para completar um certo prefixo já introduzido.
Quando o utilizador introduz mais uma letra, é acrescentada ao prefixo anterior e
apresenta-se nova lista de possibilidades e assim sucessivamente.'''

import bisect

file = 'wordlist.txt'

def WordsAfterPrefix(prefix):
    with open(file, 'r') as f:
        wordlist = f.read().split()
        letterLst = []
        lettersSet = set()
        firstPosition = bisect.bisect_left(wordlist, prefix)
        
        if len(prefix) > len(max(wordlist)):
            return print("\nThere are no words with this prefix!")

        while prefix != wordlist[firstPosition]:

            k = firstPosition   
            prefixLen = len(prefix)                            

                   

            while prefix in wordlist[k]:
                k+=1
            
            
            for i in range(firstPosition, k):
                WordsAfterPre = wordlist[i]
                if len(WordsAfterPre) > prefixLen:
                    lettersSet.add(WordsAfterPre[prefixLen])
                else:
                    print("There are no words with this prefix")
                    
            for char in lettersSet:
                letterLst.append(char)
                letterLst = sorted(letterLst)

            charOptions = letterLst
            print(charOptions)

            charChoose = input("Choose a character from the list: ")
            if charChoose in charOptions:
                prefix += charChoose
                letterLst = []
                lettersSet = set()
                firstPosition = bisect.bisect_left(wordlist, prefix)

            else:
                print("Character chosen is not on the list:")
                letterLst = []
                lettersSet = set()

        return print("The word you got was:\n --> ", prefix)


def main():
    prefixo = input("\nWrite your prefix: \n-> ")
    print(WordsAfterPrefix(prefixo))
    


main()
