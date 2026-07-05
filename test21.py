def day_of_programmer(y) :
    leap = [31,29,31,30,31,30,31,31] #244 
    not_leap = [31,28,31,30,31,30,31,31] #243 
    date = [0,0,y]
    if y > 1918 and y < 2700:
        if (y%400 == 0) or ( y%4 == 0 and y%100 != 0 ):
            date[1] = 9
            date[0] = 256-sum(leap) 

        else :
            date[1] = 9
            date[0] = 256-sum(not_leap)
    elif y >= 1700 and y < 1918 :
        if(y%4 == 0) :
            date[1] = 9
            date[0] = 256-sum(leap)
        else :
            date[1] = 9
            date[0] = 256-sum(not_leap)     

    elif y == 1918:
        date[1] = 9
        date[0] = 26

    return date
 
y = int(input().rstrip())

res = day_of_programmer(y)

print(f"{res[0]}.0{res[1]}.{res[2]}")
