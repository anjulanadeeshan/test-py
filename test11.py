ar = list(map(int, input().rstrip().split()))

min_val = sum(ar)-max(ar)
max_val = sum(ar)-min(ar)

print(min_val, max_val)