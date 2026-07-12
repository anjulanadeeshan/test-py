n = int(input().rstrip())

ranked = list(map(int, input().rstrip().split()))

m = int(input().rstrip())

player = list(map(int, input().rstrip().split()))

new_rankes = []
seted = list(sorted(set(ranked), reverse=True))

for j in player:
    test = seted.copy()
    seted.append(j)
    seted.sort(reverse=True)
    new_rankes.append(seted.index(j)+1)

    
for i in new_rankes:
    print(i, end=" ") 