import bisect

def listword():
    list_words = []
    with open('wordlist.txt','r') as words_file:
        for word in words_file:
            word = word.strip()
            list_words.append(word)

    return list_words

def binary_search(lst,s): 
    i = bisect.bisect_left(lst,s)
    next_string = 'eb'
    j = bisect.bisect_left(lst,next_string )
    print(i)

def wordsearch(string,lst):
    return lst[bisect.bisect_left(lst,string):bisect.bisect_right(lst,string+'~')]
    
    
def main():

    string_to_search = 'ea'

    list = listword()
    binary_search(list,string_to_search)
    wordsearch(string_to_search,list)
    
main()
    
    
    
    