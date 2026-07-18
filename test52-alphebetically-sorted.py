def is_alpha(ar):
   
    sorted_rows = [''.join(sorted(row)) for row in ar]

    for col in zip(*sorted_rows):
        if list(col) != sorted(col):
            return 'NO'

    return 'YES'


t = int(input())
for _ in range(t):
    n = int(input())
    ar = [input() for _ in range(n)]
    print(is_alpha(ar))