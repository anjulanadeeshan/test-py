h = list(map(int, input().rstrip().split()))

word = str(input())

max_v = 0
for ch in word:
    v = ord(ch) - 97
    xh = h[v]
    max_v = max(xh,max_v)

print(max_v*len(word))

#ord function give the unicode value of a char