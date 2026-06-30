def cal_diagonal_def(ar) :

    primary_diag = 0
    secondary_diag = 0

    length = len(ar[0])
    for i in range(len(ar[0])) :
        primary_diag += ar[i][i]
        secondary_diag += ar[i][length-i-1] 

    difference = primary_diag-secondary_diag
    if difference < 0: 
        difference = difference*(-1)
    return difference

ar = []

size = int(input())

for i in range(size) :
    ar.append(list(map(int, input().rstrip().split())))

res = cal_diagonal_def(ar)

print(res)