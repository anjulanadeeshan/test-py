def reduce_string(s) :
    stack = []
    for ch in s:
        if stack and stack[-1] == ch :
            stack.pop()
        else :
            stack.append(ch)

    return ''.join(stack) if stack else "Empty String"

word = str(input().rstrip())
print(reduce_string(word))