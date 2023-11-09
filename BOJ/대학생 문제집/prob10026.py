from collections import deque

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(color, x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == True or arr[nx][ny] != color:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    return True

# print(arr)
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            if bfs(arr[i][j], i, j):
                cnt += 1
print(cnt, end=' ')

cnt = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == "G":
            arr[i][j] = "R"
            
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            if bfs(arr[i][j], i, j):
                cnt += 1
print(cnt)