def cat(ar1) :
    x = ar1[0]
    y = ar1[1]
    z = ar1[2]
    if abs(x-z) == abs(y-z):
        return "Mouse C"
    elif abs(x-z) < abs(y-z):
        return "Cat A"
    else :
        return "Cat B"

n = int(input())
ar = []
for i in range(n):
    l1 = list(map(int, input().rstrip().split()))
    ar.append(l1)

for i in range(len(ar)):
    print(cat(ar[i]))