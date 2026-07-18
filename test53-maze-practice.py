from collections import deque

def maze(n,m,k,grid) :
    st = (0,0)
    end = (n-1,m-1)
    queue = deque([(0,0,0,0)])
    visited = set()
    visited.add((0,0,0))

    dir = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue :
        r,c,w,step = queue.popleft()
        if (r,c) == end:
            print(visited)
            return step
        
        for dr, dc in dir:
            nr,nc = dr+r, dc+c
            if 0<= nr < n and 0<= nc < m:
                if (nr,nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr,nc))
                    queue.append((nr,nc,w,step+1))
                elif (nr,nc) not in visited and grid[nr][nc] == 1 and w<k:
                    visited.add((nr,nc))
                    queue.append((nr,nc,w+1,step+1))

    
    return -1
n,m,k = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(n)]

print(maze(n,m,k,grid))