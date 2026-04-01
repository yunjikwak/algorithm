from collections import deque

n, m = map(int, input().split())
graph = []
queue = deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            row[j] = 0
            queue.append((i, j))
        elif row[j] == 1:  # 방문 가능인데 아직 방문 전
            row[j] = -1
    graph.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs()

# 마지막에 바꾸면 그 전에 거쳐온 것들은 바꿀 수 X
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             graph[i][j] = -1

for row in graph:
    print(" ".join(map(str, row)))
