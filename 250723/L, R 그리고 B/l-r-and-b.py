from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = 10, 10
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

x,y = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            x = i
            y = j
            break

def bfs():
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        a, b, cnt = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 'R':
                if graph[nx][ny] == 'B':
                    return cnt

                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt+1))

print(bfs())