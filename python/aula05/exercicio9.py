def evenThenOdd(string):
    ret_vals = string[1::2] + string[::2]
    return "".join(ret_vals)
        
def duplica_caractere(stringduplic):

    ret_list = ""
    for i in range(len(stringduplic) - 1):
        if stringduplic[i] != stringduplic[i+1]:
            ret_list += stringduplic[i]
        
    ret_list += stringduplic[-1]
    
    return ret_list

def repeatnumber(n):
    ret_list = []

    for i in range(n + 1):
        for repetitions in range(i):
            ret_list.append(str(i))

    return ", ".join(ret_list)

def maxindex(number_list):
    index_max = 0
    max = -1000000

    for i in range(len(number_list)):
        if number_list[i] > max:
            index_max = i
            max = number_list[i]

    return index_max, max

def main():
    string = 'mississippi'
    x = 6
    liststring = list(string)
    print(evenThenOdd(liststring))
    print(duplica_caractere(liststring))
    print(repeatnumber(x))

    max_list = [1, 2, 3, 6, 6, 3, 7, 1, 7]
    print(maxindex(max_list))
main()