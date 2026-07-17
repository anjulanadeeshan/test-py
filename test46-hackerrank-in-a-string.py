def check_the_word (s) :
    w = 'hackerrank'
    
    p = 0

    for ch in s:
        if ch == w[p] :
            p+=1
        
        if p == len(w):
            return 'YES'
    return 'NO'

n = int(input())
inp = ['']*n
for i in range(n) :
    inp[i] = str(input())

for i in inp:
    print(check_the_word(i))

