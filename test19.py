def div_sum_pairs(ar,k) :
    c = 0
    for i in range(len(ar)-1) :
        for j in range(i+1, len(ar), 1) :
            tot = ar[i]+ar[j]
            if tot%k == 0 :
                c += 1
    return c

f_inp = input().rstrip().split()

n = int(f_inp[0])
k = int(f_inp[1])

ar = list(map(int, input().strip().split()))

res = div_sum_pairs(ar,k)
print(res)