from collections import deque

N, H, M = map(int, input().split())

arr = []
step = [[-1] * N for _ in range(N)]
people = []
rain = []

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 2:
            people.append((i, j))
        elif arr[i][j] == 3:
            rain.append((i, j))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def bfs():
    q = deque()
    for x, y in rain:
        q.append((x, y))
        step[x][y] = 0
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if not in_range(nx, ny) or arr[nx][ny] == 1:
                continue
            if step[nx][ny] == -1:
                step[nx][ny] = step[a][b] + 1
                q.append((nx, ny))

bfs()

graph = [[0] * N for _ in range(N)]
for x, y in people:
    if step[x][y] != -1:
        graph[x][y] = step[x][y]
    else:
        graph[x][y] = -1

for i in range(N):
    print(*graph[i])
