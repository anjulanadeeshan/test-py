def kang(x1, v1, x2, v2) :
    if ((x1 < x2) and (v1 < v2)) or ((x1>x2)and(v1>v2)) :
        return "NO"
    
    for i in range(10000):
        if x1+v1*i == x2+v2*i :
            return "YES"
        
    return "NO"

         
inp = list(map(int, input().rstrip().split()))
x1 = inp[0]
v1 = inp[1]
x2 = inp[2]
v2 = inp[3]

res = kang(x1, v1, x2, v2)
print(res)