def ispalidrome(tuplestring):
    half_string = int(len(tuplestring)/2)
    if tuplestring[:half_string] == tuplestring[len(tuplestring):half_string:-1] :
        return True
    else:
        return False

def main():
    string = str(input('?'))
    tuplestring = tuple(string.lower())
    print(tuplestring)
    print(ispalidrome(tuplestring))

main()