ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left  = 0
right = len(ar) - 1

while left < right:
    print(ar[left], ar[right])
    left  += 1
    right -= 1