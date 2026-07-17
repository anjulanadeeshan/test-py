def check_panagram(s) :
    s.lower()
    n = set(s)

    for ch in n:
        if not ch.isalpha():
            n.pop(ch)

    if len(n) == 26:
        return 'pangram'
    
    return 'not pangram'

inp = input()

print(check_panagram(inp))