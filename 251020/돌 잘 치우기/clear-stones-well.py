from collections import deque

N, K, M = map(int, input().split())
arr = []
stone = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for idx, val in enumerate(arr[-1]):
        if val == 1:
            stone.append((i, idx))

start = []
for _ in range(K):
    a, b = map(int, input().split())
    start.append((a-1, b-1))

remove = []
result = 0

def choose(idx):
    global result

    if len(remove) == M:
        cur = 0
        visited = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(M):
            a, b = remove[i]
            visited[a][b] = 2 # 무시 가능 돌 표시

        # print(visited)
        for i in range(K):
            x, y = start[i]
            cur += bfs(visited, x, y)
            # print(x, y, cur)
        
        result = max(result, cur)
        return
    
    for i in range(idx, len(stone)):
        remove.append(stone[i])
        choose(i+1)
        remove.pop()
    return

def in_range(a, b):
    return 0<=a<N and 0<=b<N

dx, dy = [-1,0,1,0], [0,-1,0,1]

def bfs(visited, x, y):
    q = deque()
    if visited[x][y] == 1:
        return 0
    visited[x][y] = 1
    q.append((x, y))
    cnt = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]

            if not in_range(nx, ny) or visited[nx][ny] == 1:
                continue
            if arr[nx][ny] == 1:
                if not visited[nx][ny] == 2:
                    continue

            visited[nx][ny] = 1
            q.append((nx, ny))
            cnt += 1
    return cnt

choose(0)
print(result)