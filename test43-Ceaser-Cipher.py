n = int(input())

s = input().rstrip()

shi = int(input())

word = ''
for ch in s:
    if ch.islower() : 
        new_ch = chr((ord(ch)-ord('a')+shi)%26+ord('a'))
    elif ch.isupper() :
        new_ch = chr((ord(ch)-ord('A')+shi)%26+ord('A'))
    else:
        new_ch = ch

    word+=new_ch

print(word)