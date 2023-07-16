from collections import deque

M, N = map(int, input().split())
graph = []
ripe_tomatoes = deque() # 익은 토마토 큐에 저장

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] == 1:
            ripe_tomatoes.append((i, j))
# print(graph, ripe_tomatoes)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while ripe_tomatoes:
        x, y = ripe_tomatoes.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                ripe_tomatoes.append((nx, ny))

# 이렇게 전체로 돌면 시간 초과
# # result = 0
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             bfs(i, j)

# 익은 토마토를 큐에 저장해서 그 큐에 대해 bfs 수행
bfs()

result = 0
for row in graph:
    if 0 in row:
        print("-1")
        exit()
    result = max(result, max(row))
print(result-1) # bfs 결과를 result에 주는데 bfs는 1인 자리부터 더하여 나가기 때문에 -1 해줌