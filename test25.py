steps = int(input())

ar = input()
lev = 0
valleys = 0

for c in ar:
    
    if c == 'D' :
        lev += -1
    elif c == 'U':
        lev += +1
        if lev == 0:
            valleys+=1
    

print(valleys)
