def count_no(s,t,a,b,m,n,apple, orange) :
    res = [0,0]
    for i in range(m) :
        apple[i] += a

    for i in range(n):
        orange[i] += b

    for i in apple:
        if i >= s and i <= t:
            res[0]+=1

    for i in orange:
        if i>=s and i<=t:
            res[1]+=1
        
    return res


    

first_inp = list(map(int, input().strip().split()))
s = first_inp[0]
t = first_inp[1]

sec_inp = list(map(int, input().strip().split()))
a = sec_inp[0]
b = sec_inp[1]

third_inp = list(map(int, input().strip().split()))
m = third_inp[0]
n = third_inp[1]

apple = list(map(int, input().strip().split()))
orange = list(map(int, input().strip().split()))

res = count_no(s,t,a,b,m,n,apple, orange)

for i in res:
    print(i)
