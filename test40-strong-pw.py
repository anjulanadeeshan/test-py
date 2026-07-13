def camel(s):
    ar = [0]*4 #ar = [digit, lowercase, uppercase, special_char]

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    for ch in s:
        if ch in numbers and ar[0] == 0:
            ar[0] = 1
        elif ch in lower_case and ar[1] == 0:
            ar[1] = 1
        elif ch in upper_case and ar[2] == 0:
            ar[2] = 1
        elif ch in special_characters and ar[3] == 0:
            ar[3] = 1
    
    if len(s) < 6:
        if (4-sum(ar)) > 6-len(s):
            return (4-sum(ar))
        else :
            return (6-len(s))
        
    else:
        return (4-sum(ar))
        
    

n = int(input().rstrip())
s = input()

print(camel(s))
