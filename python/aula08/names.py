lst = []

with open('names.txt', "r") as file:
    file.readline()
    for line in file:
        line = line.strip()
        name = line.split()
        
        lst.append(name)
        
dic_name = {}
for n in lst:
    if n[-1] not in dic_name:
        dic_name[n[-1]] = {n[0]}
    else:
        dic_name[n[-1]].add(n[0]) 

for key,value in dic_name.items():    
    print(f'{key} : {value}')
    