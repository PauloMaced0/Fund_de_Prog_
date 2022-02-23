# Complete o programa!
# ler o conteudo e acrescentar um tuplo por cada aluno 
# á lista lst. cada tuplo deve ter os campos (número,nome
# ,nota1,nota2,nota3) 
# a)
def loadFile(fname, lst):
    with open(fname, "r") as file:
        file.readline()
        for line in file:
            line = line.strip()
            row_information = line.split("\t")
            
            lst.append((row_information[0], row_information[1], row_information[5], row_information[6], row_information[7]))

# b) Crie a função notaFinal aqui...
def notafinal(reg):
    return (float(reg[2]) + float(reg[3]) + float(reg[4])) / 3

def printpauta(lst):
    print("{:6} {:^50} {:4}".format("Numero", "Nome", "Nota"))
    for reg in lst:
        print("{:>6} {:^50} {:4.1f}".format(reg[0], reg[1], notafinal(reg)))

def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    
    # ordenar a lista
    compareFunction = lambda reg : int(reg[0])
    lst.sort(key=compareFunction)

    # mostrar a pauta
    printpauta(lst)

# Call main function
if __name__ == "__main__":
    main()

