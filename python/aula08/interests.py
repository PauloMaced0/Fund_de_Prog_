def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    # without comprehesion --->
    #
    #  names = list(interests.keys())
    # for i in range(len(names)):
    #     for j in range(i+1,len(names)):
    #             print((names[i], names[j]))

    names = list(interests.keys())
    combinations = {(names[i], names[j]): interests[names[i]] & interests[names[j]] for i in range(len(names)) for j in range(i+1, len(names))}
    print(combinations)
    
    print("b) Maximum number of common interests:")
    # maxCI = max ({len(item[1]):item[0] for item in combinations.items()})

    maximum = max(len(value) for value in combinations.values())
    print(maximum)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [item[0] for item in combinations.items() if len(item[1]) == maximum]
    print(maxmatches)

    print("d) Pairs with low similarity:")
    # without comprehension ---> 
    # 
    #  for item in combinations.items():
    #     intersection = len(item[1])
    #     union = len(interests[item[0][0]]) + len(interests[item[0][1]]) - intersection
    #     jaccard_index = (intersection / union) * 100          
    #     if jaccard_index < 25:
    #         print(item[0]) 

    low_jaccard = [
        item[0] for item in combinations.items()
        if len(item[1])/ ((len(interests[item[0][0]]) + len(interests[item[0][1]]) - len(item[1]))) < 0.25
    ]
    print(low_jaccard)


# Start program:
main()