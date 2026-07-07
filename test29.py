def find_min_cost(s) :
    magic_squares = [
        [[2,7,6],[9,5,1],[4,3,8]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[8,3,4],[1,5,9],[6,7,2]]
    ]

    min_cost = float('inf')

    for m in magic_squares:
        cost = 0
        for r in range(3):
            for c in range(3):
                cost += abs(s[r][c]-m[r][c])
        min_cost = min(min_cost,cost)

    
    return min_cost


s = []
for i in range(3) :
    s.append(list(map(int, input().split())))

res = find_min_cost(s)
print(res)