s = input()

count = 1
for ch in s:
    if ch.isupper() :
        count+=1
    
print(count)