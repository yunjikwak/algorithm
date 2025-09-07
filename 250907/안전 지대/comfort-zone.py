N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

start = float('inf')
end = float('-inf')

for i in range(N):
    for j in range(M):
        cur = arr[i][j]
        if cur < start: start = cur
        if cur > end: end = cur

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def dfs(x, y, k):
    global visited

    visited[x][y] = True
    cnt = 1
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        
        if not in_range(nx, ny) or visited[nx][ny]:
            continue

        if arr[nx][ny] > k:
            cnt += 1
            dfs(nx, ny, k)
    return cnt

max_region = []
cur = 0
for k in range(start, end+1):
    cur_region = []
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] > k and not visited[i][j]:
                cur_region.append(dfs(i, j, k))
    
    if len(max_region) < len(cur_region):
        max_region = cur_region
        cur = k

print(cur, len(max_region))