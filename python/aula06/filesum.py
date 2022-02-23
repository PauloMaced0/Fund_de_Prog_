
from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    

    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    file_name = open(filename, 'r',)
    lines_to_sum = file_name.readlines()
    sum = 0
    for line in lines_to_sum:
        if line.isdigit:
            num_line = float(line)
            sum += num_line
    file_name.close()
    return sum  

if __name__ == "__main__":
    main()
