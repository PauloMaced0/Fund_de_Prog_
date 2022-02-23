def compare_files():
    with open('filesize.py','rb') as f1:
        with open('turtledraw.py','rb') as f2:
            read_1 = f1.read(1024) 
            read_2 = f2.read(1024)

    if read_1 == read_2:
        print('Same!')
    else:
        print('Different!')

def main():
    compare_files()

main()