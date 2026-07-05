def get_money(key, drivers, b) :
    max_v = -1
    for i in key:
        for d in drivers:
            tot = i + d
            if tot > max_v and tot <= b:
                max_v = tot


    return max_v


first_inp = list(map(int, input().rstrip().split()))
b = first_inp[0]
n = first_inp[1]
m = first_inp[2]

key = list(map(int, input().rstrip().split()))
drivers = list(map(int, input().rstrip().split()))

print(get_money(key,drivers,b))