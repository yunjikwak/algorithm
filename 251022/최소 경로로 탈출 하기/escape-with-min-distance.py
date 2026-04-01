from collections import deque

N, M = map(int, input().split())

graph = []
visited = [[False] * M for _ in range(N)]
step = [[-1] * M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < M

def bfs():
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 1:
                push(nx, ny, step[a][b] + 1)
    
q = deque()
push(0, 0, 0)
bfs()

print(step[N-1][M-1])