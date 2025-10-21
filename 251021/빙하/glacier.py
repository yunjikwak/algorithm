from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs_air():
    visited = [[False]*M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 1:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    return visited

time = 0
last_count = 0

while True:
    boundary = bfs_air()
    melting = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if in_range(nx, ny) and boundary[nx][ny]:
                        melting.append((i, j))
                        break
    if not melting:
        break
        
    last_count = len(melting)
    for x, y in melting:
        arr[x][y] = 0
    time += 1

print(time, last_count)
