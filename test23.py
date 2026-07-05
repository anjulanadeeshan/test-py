from collections import Counter

def sales_by_match(ar1) :
    c = 0
    counts = Counter(ar1)
    for value in counts.values() :
        inc = 0
        if value%2 == 0 or int(value/2)>=1:
            inc = int(value/2)
            c+= inc
    return c 
    
n = int(input()) 

ar1 = list(map(int, input().rstrip().split()))

res = sales_by_match(ar1)
print(res)