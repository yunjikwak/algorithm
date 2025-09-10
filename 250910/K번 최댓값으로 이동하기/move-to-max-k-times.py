from collections import deque

N, K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

r, c = map(int, input().split())
r -= 1
c -= 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(a, b):
    return 0<=a<N and 0<=b<N

def bfs(x,y):
    visited[x][y] = True
    q = deque()
    q.append((x,y))

    val = graph[x][y]

    cur_x, cur_y = -1, -1

    # print("start", x, y, val)

    while q:
        a, b = q.popleft()
        
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]

            if not in_range(nx, ny) or visited[nx][ny]:
                continue
            if graph[nx][ny] >= val:
                continue

            # print(a,b, nx, ny, cur_x, cur_y, val, graph[nx][ny])

            visited[nx][ny] = True
            q.append((nx, ny))

            if cur_x == -1 and cur_y == -1:
                cur_x = nx
                cur_y = ny
            elif graph[nx][ny] == graph[cur_x][cur_y]:

                if nx == cur_x:
                    if ny < cur_y:
                        cur_y = ny
                elif nx < cur_x:
                    cur_x = nx
                    cur_y = ny
            elif graph[nx][ny] > graph[cur_x][cur_y]:
                cur_x = nx
                cur_y = ny
    return cur_x, cur_y

for _ in range(K):
    # print(r, c)
    visited = [[False] * N for _ in range(N)]
    nr, nc = bfs(r, c)
    
    if nr == -1 or nc == -1:
        break
    else:
        r, c = nr, nc
print(r+1, c+1)