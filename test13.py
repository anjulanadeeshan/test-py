ar = list(input().rstrip().split(":"))

if ar[2][2] == 'P' and ar[0] != '12':
    ar[0] = int(ar[0])
    ar[0] += 12
elif ar[2][2] == 'A' and ar[0] == '12':
    ar[0] = '00'

print(f"{ar[0]}:{ar[1]}:{ar[2][0:2]}")
