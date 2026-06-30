n = int(input().strip());
# n = 4
for i in range(n): # 0,1,2,3
    for j in range(n-i-1):
        print(" ",end="")
    
    for k in range(i+1):
        print("#",end="")

    print()