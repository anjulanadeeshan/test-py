def drawing_book(n, p):
    from_front = p // 2

    if n % 2 == 0:
        from_back = (n - p + 1) // 2   # ← shift by 1 for even n
    else:
        from_back = (n - p) // 2

    return min(from_front, from_back)

n = int(input())
p = int(input())
print(drawing_book(n, p))