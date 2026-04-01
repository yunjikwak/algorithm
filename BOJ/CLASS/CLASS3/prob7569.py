from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]
queue = deque()

for h in range(H):
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m))
        graph[h].append(row)

dh = [1, -1, 0, 0, 0, 0]  # front, back
dx = [0, 0, -1, 1, 0, 0]  # left, right
dy = [0, 0, 0, 0, -1, 1]  # up, down


def bfs():
    # queue = deque()
    # queue.append((h, x, y))

    while queue:
        h, x, y = queue.popleft()
        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nh < 0 or nh >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nh][nx][ny] == 0:
                graph[nh][nx][ny] = graph[h][x][y] + 1
                queue.append((nh, nx, ny))
            # if graph[nh][nx][ny] == -1 or graph[nh][nx][ny] == 1:
            #     continue
            # if graph[nh][nx][ny] == 0 or graph[nh][nx][ny] > cur:
            #     graph[nh][nx][ny] = cur + 1
            #     queue.append((nh, nx, ny))


bfs()

result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                print(-1)
                exit()
            result = max(result, graph[h][n][m])

print(result-1)

# def bfs(h, x, y):
#     q = deque()
#     q.append((h,x,y))

#     while q:
#         h, x, y = q.popleft()

#         for i in range(6):
#             nh = h + dh[i]
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nh < 0 or nx < 0 or ny < 0 or nh >= H or nx >= N or ny >= M:
#                 continue
#             if graph[nh][nx][ny] != 0: # -1, 1 이상이 걸려야함 -> 이미 방문했거나 이미 익음 => 0만 통과
#                 continue

#             graph[nh][nx][ny] = graph[h][x][y] + 1
#             q.append((nh, nx, ny))

#     return graph[h][x][y]

# result = 0
# for height in range(H):
#     for row in range(N):
#         for col in range(M):
#             if graph[height][row][col] == 1:
#                 day = bfs(height, row, col)
#                 if day > result:
#                     result = day

# for i in graph:
#     for j in i:
#         for k in j:
#             if k == 0:
#                 print(-1)
#                 exit()

# print(result-1)

"""
from collections import deque

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]

for h in range(H):
    for _ in range(N):
        graph[h].append(list(map(int, input().split())))

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dh = [1, -1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

def bfs(h, x, y):
    q = deque()
    q.append((h,x,y))
    visited[h][x][y] = True

    # cnt = 0

    while q:
        # cnt += 1
        h, x, y = q.popleft()
        # print("h, x, y ", h, x, y)
        # print("cnt ", cnt)

        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nh < 0 or nx < 0 or ny < 0 or nh >= H or nx >= N or ny >= M:
                continue
            if visited[nh][nx][ny] == True or graph[nh][nx][ny] != 0: # -1, 1 이상이 걸려야함 -> 이미 방문했거나 이미 익음 => 0 통과
                continue

            graph[nh][nx][ny] = graph[h][x][y] + 1
            q.append((nh, nx, ny))
            visited[nh][nx][ny] = True

    return graph[h][x][y]
            # print(nh, nx, ny)
        # cnt += 1
    # return cnt

result = 0
for height in range(H):
    for row in range(N):
        for col in range(M):
            if graph[height][row][col] == 1 and visited[height][row][col] == False:
                day = bfs(height, row, col)
                if day > result:
                    result = day

for i in graph:
    for j in i:
        for k in j:
            if k < 1 and k != -1:
                print(-1)
                exit()

print(result-1)
# print("graph", graph)
# print("visited", visited)
"""
