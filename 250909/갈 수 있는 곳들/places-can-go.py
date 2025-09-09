from collections import deque

N, K = map(int, input().split())

graph = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

start = []
for _ in range(K):
    start.append(tuple(map(int, input().split())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def bfs(x,y):
    if visited[x][y] or graph[x][y] == 1:
        return 0

    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
    
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]

            if not in_range(nx, ny) or visited[nx][ny] or graph[nx][ny] == 1:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
            cnt += 1
    return cnt

total = 0
for x, y in start:
    x -= 1
    y -= 1
    total += bfs(x, y)
print(total)