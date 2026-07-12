arr  = list(map(int, input().rstrip().split()))
k = arr[1] 

hurdles = list(map(int, input().rstrip().split()))

if k >= max(hurdles) :
    print(0)
else:
    print(max(hurdles)-k)