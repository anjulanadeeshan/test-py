from itertools import combinations

def two_char(s) :
    char = []

    max_v = 0

    for ch in s:
        if ch not in char:
            char.append(ch)

    for c1, c2 in combinations(char, 2):
        filtered = [ch for ch in s if ch == c1 or ch == c2]

        is_valid = True
        for i in range(len(filtered) -1) :
            if filtered[i] == filtered[i+1] :
                is_valid = False
                break

        if is_valid:
            max_v = max(max_v, len(filtered))

    return max_v
        
n = int(input().rstrip())

s = str(input())
print(two_char(s))