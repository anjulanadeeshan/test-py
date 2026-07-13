ar = [3,1,4,1,5,9,2,6]

prefix = [0]*(len(ar)+1)

for i in range(len(ar)):
    prefix[i+1] = prefix[i] + ar[i]

for i in prefix:
    print(i, end=" ")
    
print()

print(sum(ar[1:5]))