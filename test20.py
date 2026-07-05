from collections import Counter

def func_cal(ar) :
    c = Counter(ar)
    
    m = sorted(c.items(), key=lambda x: (-x[1],x[0]))
    return m[0][0]

n = int(input())
ar = list(map(int, input().rstrip().split()))

res = func_cal(ar)
print(res)