def plusMinus(ar) :
    res = [0,0,0]
    for i in ar:
        if i > 0:
            res[0] += 1
        if i < 0:
            res[1] += 1
        if i == 0:
            res[2] += 1
        
    for i in range(3):
        res[i] = res[i]/len(ar)

    return res


n = int(input().rstrip())
ar = list(map(int, input().rstrip().split()))
res = plusMinus(ar)

for i in res:
    print(f"{i:.6f}")