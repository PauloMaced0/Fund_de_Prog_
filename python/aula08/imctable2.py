
# Devolve o IMC para uma pessoa com peso w e altura h.
def imc(w, h):
    return w/h**2


def main():
    # Lista de pessoas com nome, peso em kg, altura em metro.
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    print("People:", people)

    # Esta comprehension define uma lista dos nomes das pessoas em people
    names = [n for n,w,h in people]
        # = [p[0] for p in people]  # equivalente
    print("Names:", names)
    
    # Usando list comprehensions, obtenha: 
    # a) Uma lista com os valores de imc de todas as pessoas.
    imcs = [imc(people[n][1],people[n][2]) for n in range(len(people))]
    print(f"IMCs:", imcs)

    # b) Uma lista dos tuplos de pessoas com altura superior a 1.7m.
    tallpeople = [people[n] for n in range(len(people)) if people[n][2] > 1.7]
    print("Tall people:", tallpeople)    

    # c) Uma lista de nomes das pessoas com IMC entre 18 e 25.
    midimc = [people[n][0] for n in range(len(people)) if 18 < imcs[n] < 25]
    print("Mid-IMC:", midimc)


# O programa começa aqui
main()

