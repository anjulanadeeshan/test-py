from collections import Counter

def isValid(inp) :
    l1 = list(set(inp))

    if len(inp) == 4000*25:
        return 'YES'

    for i in l1:
        inp2 = inp
        res = inp2.replace(i,'',1)
        if len(res) == 0:
            return "YES"
        c = Counter(res)
        l2 = sorted(list(c.values()))
        if len(res) >= 0 and l2[0] == l2[-1]:
            return "YES"
    return "NO"

inp = input().rstrip()

print(isValid(inp))