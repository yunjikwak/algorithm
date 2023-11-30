from collections import deque

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(x, y, target_x, target_y):
    visited = [[False] * I for _ in range(I)]  
    
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == target_x and y == target_y:
            return cnt
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if visited[nx][ny] == True:
                continue
            # if nx == target_x and ny == target_y:
            #     return cnt + 1
            
            queue.append((nx, ny, cnt+1))
            visited[nx][ny] = True

T = int(input())

for _ in range(T):
    I = int(input())
    cur = list(map(int, input().split()))
    target = list(map(int, input().split()))
    
    print(bfs(cur[0], cur[1], target[0], target[1]))