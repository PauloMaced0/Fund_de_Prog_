def allmatches(lista_clube):
    all_matches = []

    for home_team in lista_clube:
        for team in lista_clube:
            if home_team != team:
                all_matches.append((home_team, team))
    
    return all_matches

def result(match):
    print("Result of game:", match)
    result_home_team = int(input('equipa de casa: '))
    result_guest_team = int(input('equipa de fora: '))

    return (result_home_team, result_guest_team)


def statistics(championship_table, match, result):

    # update goals
    championship_table[match[0]][3] += result[0]
    championship_table[match[0]][4] += result[1]

    # golos sofridos e marcados da  equipa que joga fora
    championship_table[match[1]][3] += result[1]
    championship_table[match[1]][4] += result[0]

    if result[0] == result[1]:
        # update draws
        championship_table[match[0]][1] += 1
        championship_table[match[1]][1] += 1

        # update point column
        championship_table[match[0]][5] += 1
        championship_table[match[1]][5] += 1

    elif result[0] > result[1]:
        # house team won
        championship_table[match[0]][0] += 1
        championship_table[match[1]][2] += 1

        # update point column
        championship_table[match[0]][5] += 3
    else:
        # house team lost
        championship_table[match[0]][2] += 1
        championship_table[match[1]][0] += 1

        # update point column
        championship_table[match[1]][5] += 3

def championship_simulation(results_dictionary, championsip_table, all_matches):
    for match in all_matches:
        res = result(match)

        results_dictionary[match] = res

        statistics(championsip_table, match, res)




def main():
    matches_result = {}
    lista_clube = ['Sporting','Porto','Benfica']
    all_matchesclubes = allmatches(lista_clube)

    # initialize dictionary with team table
    championship_table = {}
    for club in lista_clube:
        championship_table[club] = [0, 0, 0, 0, 0, 0]

    championship_simulation(matches_result, championship_table, all_matchesclubes)

    print(matches_result)

    print()
    
    print(championship_table)
    
    sort_order = sorted(championship_table.items(),key= lambda item_tuple : item_tuple[1][5], reverse=True)

    print(sort_order)
    
    for club, row in sort_order:
        print(f"{club} --> {row}")
    
    print('Winner:',sort_order[0][0],'!')


main()