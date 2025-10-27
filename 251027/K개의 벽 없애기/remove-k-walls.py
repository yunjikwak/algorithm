from collections import deque

N, K = map(int, input().split())
arr = []
block = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[-1][j] == 1:
            block.append((i,j))

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

select = []
result = N*N*N
def select_K_block(idx):
    global result

    if len(select) == K:
        cur = bfs(select)
        if cur != -1:
            result = min(result, cur)
        return
    
    for i in range(idx, len(block)):
        select.append(block[i])
        select_K_block(idx+1)
        select.pop()
    return

dx, dy = [-1,0,1,0], [0,1,0,-1]

def in_range(a,b):
    return 0<=a<N and 0<=b<N

def bfs(select):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    q.append((r1, c1))
    # t = 0
    visited[r1][c1] = 0

    while q:
        a, b = q.popleft()
        # visited[a][b] = t
        # t += 1

        if (a, b) == (r2, c2):
            return visited[r2][c2]

        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]

            if in_range(nx, ny) and visited[nx][ny] == -1:
                # if arr[nx][ny] == 0 
                if arr[nx][ny] == 1 and (nx, ny) not in select:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = visited[a][b] + 1
    
    return visited[r2][c2]

select_K_block(0)
if result == N*N*N:
    print(-1)
else:
    print(result)