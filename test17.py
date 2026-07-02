def count_min(ar) :
    res = [0,0] #res[max_c,min_c]

    min = ar[0]
    max = ar[0]

    for i in range(len(ar)-1):
        if ar[i+1] > max:
            res[0] += 1
            max=ar[i+1]
        elif ar[i+1] < min:
            res[1] += 1
            min=ar[i+1]

    return res
        
        

n = int(input().rstrip())

ar = list(map(int, input().rstrip().split()))

res = count_min(ar)

print(f"{res[0]} {res[1]}")

