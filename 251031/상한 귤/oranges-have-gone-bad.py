from collections import deque

N, K = map(int, input().split())
arr = []
start = []
visited = [[-2] * N for _ in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[-1][j] == 2:
            start.append((i, j))

def in_range(a, b):
    return 0<=a<N and 0<=b<N

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            nx,ny = a+dx[i], b+dy[i]

            if in_range(nx, ny) and arr[nx][ny] == 1:
                if visited[nx][ny] == -2 or visited[nx][ny] > visited[a][b] + 1:
                    visited[nx][ny] = visited[a][b]+1
                    q.append((nx, ny))
    return

for i in range(len(start)):
    a, b = start[i]
    bfs(a, b)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            visited[i][j] = -1
    
for i in range(N):
    print(*visited[i])