def cal_score(a, b) :
    res = [0, 0]
    for i in range(len(a)) :
        if a[i] > b[i] :
            res[0] += 1
        elif a[i] < b[i] :
            res[1] += 1
        
    return res


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

res = cal_score(a,b)


for i in res:
    print(i, end=" ")