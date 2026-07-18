def mars_cupcakes(ar):
    ar1 = sorted(ar,reverse=True)
    c = 0
    for i in range(len(ar1)):
        ca = (2**i)*ar1[i]
        c += ca

    return c

n = int(input())
ar = list(map(int, input().split()))

print(mars_cupcakes(ar))