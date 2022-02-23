import os

def file_size():
    for file in os.listdir():
        filesize = os.stat(file).st_size
        print((file),'=',(filesize),'bytes')
        
def main():
    file_size()
main()