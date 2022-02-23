def clubes():
    clube = []
    while True:
        x = input('?')
        if x == '': break
        clb = str(x.upper())
        clube.append(clb)
        
    return clube 

def allmatches(lista_clube):
    all_matches = []

    for home_team in lista_clube:
        for team in lista_clube:
            if home_team != team:
                all_matches.append((home_team, team))
    
    return all_matches

def main():
    lista_clube = clubes()
    print('All Matches',lista_clube,'->')
    print(allmatches(lista_clube))

main()
   
   
    #print([(home_team, team) for home_team in lista_clube for team in lista_clube if home_team != team])