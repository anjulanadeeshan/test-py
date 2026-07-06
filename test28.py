from collections import Counter

def subarr(ar) :
    counts = Counter(ar)
    max_len = 0
    for v in counts:
        length = counts[v] + counts[v+1]
        max_len = max(max_len, length)

    return(max_len)
        
        

n = int(input())
ar = list(map(int, input().split()))

print(subarr(ar))
