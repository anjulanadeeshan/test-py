def bonAppetit(ar2, k, b) :
    tot = (sum(ar2)-ar2[k])/2
    if tot == b:
        return "Bon Appetit"
    
    else :
        return int(b-(sum(ar2)-ar2[k])/2)



ar1 = list(map(int, input().rstrip().split()))

n = ar1[0]
k = ar1[1]

ar2 = list(map(int, input().rstrip().split()))

b = int(input().rstrip())

res = bonAppetit(ar2, k, b)

print(res)