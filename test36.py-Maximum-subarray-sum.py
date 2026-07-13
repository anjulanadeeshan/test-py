#kadane's Algorithm

def sub_arry(ar) :
    max_sum = ar[0]
    curr_sum = ar[0]
    s = 0
    best_st, best_end = 0,0

    for i in range(1,len(ar)) :
        if curr_sum < 0:
            curr_sum = ar[i]
            s = i
        else :
            curr_sum += ar[i]


        if curr_sum > max_sum:
            max_sum = curr_sum
            best_st, best_end = s, i


    return max_sum, ar[best_st:best_end+1]

ar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sub,arr = sub_arry(ar)
print(max_sub)
print(arr)
