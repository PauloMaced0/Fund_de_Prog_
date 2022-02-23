def median(lst): 
    assert len(lst)>0
    orderedLst = sorted(lst)
    lstLen = len(orderedLst)
    lenDiv = lstLen//2 - 1
    if lstLen%2==1:
        return orderedLst[lenDiv+1]
    else:
        return (orderedLst[lenDiv] + orderedLst[lenDiv+1]) / 2 

def check(lst):
    backup = lst.copy()
    m = median(lst)
    return m, lst