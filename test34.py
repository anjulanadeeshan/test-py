t = int(input().rstrip())

cyc = []
for i in range(t):
    cyc.append(int(input().rstrip()))


for i in range(len(cyc)):
    height = 1
    for j in range(1,cyc[i]+1):
        if j%2 == 0 :
            height+=1
        else :
            height = height*2
        

    print(height)