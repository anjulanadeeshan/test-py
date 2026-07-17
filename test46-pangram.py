def check_pangram(inp):
    
    x = set(inp.lower())
    y = []
    for ch in x:
        if ch.isalpha():
            y.append(ch)
        
    if len(y) == 26:
        return 'pangram'

    return 'not pangram'

inp = input()

print(check_pangram(inp))
