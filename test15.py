def grading_stu(ar) :
    aft_grading = []
    for i in range(len(ar)):
        if ar[i] >= 38:
            mul = ar[i]//5
            mul += 1
            if (mul*5 - ar[i]) < 3: 
                aft_grading.append(mul*5)

            else : 
                aft_grading.append(ar[i])
        else :
            aft_grading.append(ar[i])

    return aft_grading

    

n = int(input().rstrip())

ar = []

for i in range(n) :
    ar.append(int(input().rstrip()))

after_grading =grading_stu(ar)

for i in after_grading:
    print(i)
