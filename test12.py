def count_max(ar) :
    max_val = max(ar)
    tot = ar.count(max_val)

    return tot


n = int(input().rstrip())

ar = list(map(int, input().rstrip().split()))

num_max = count_max(ar)

print(num_max)