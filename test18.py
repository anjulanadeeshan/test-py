def caL_subarry_div(ar1, ar2) :
    d = ar2[0]
    m = ar2[1]

    count = 0
    for i in range(len(ar1)) :
        sum = 0
        for j in range(m):
            if i+j < len(ar1) :
                sum += ar1[i+j]

        if sum == d:
            count+= 1
        
    return count

n = int(input())

ar1 = list(map(int, input().rstrip().split()))

ar2 = list(map(int, input().rstrip().split()))

res = caL_subarry_div(ar1, ar2)

print(res)