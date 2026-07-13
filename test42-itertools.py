from itertools import combinations,permutations,combinations_with_replacement,product,accumulate,groupby
from math import comb

ar = [1,2,3,4]

print(list(combinations(ar, 2)))
print(comb(4,2))

print(list(permutations(ar, 2)))

print(list(combinations_with_replacement(ar,2)))

ar1 = [1,2]
ar2 = ['a', 'b']
print(list(product(ar1,ar2)))

for i, j, k in product(range(3), repeat=3):
    print(i, j, k)

print(list(accumulate(ar)))
print(list(accumulate(ar,max)))


ar2 = [1,1,2,2,3,1,1]
for key,group in groupby(ar2):
    print(key, list(group))

