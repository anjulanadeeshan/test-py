s = input().rstrip()

m = 'SOS'
c = 0

for i in range(0,len(s),3):
    word = s[i]+s[i+1]+s[i+2]
    
    for j in range(3):
        if word[j] != m[j]:
            c+=1
        
print(c)