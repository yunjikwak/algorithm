N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

limit = 4
dxs, dys = [-1,1,0,0], [0,0,-1,1]
visited = [[False for _ in range(N)] for _ in range(N)]

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def dfs(x, y, cur):
    visited[x][y] = True
    cnt = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        
        if not in_range(nx, ny) or visited[nx][ny]:
            continue
        if cur == arr[nx][ny]:
            cnt += dfs(nx, ny, cur)
    return cnt

max_block = 0
block_cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cur = dfs(i, j, arr[i][j])

            if cur >= limit: # 터지는 블럭 개수
                block_cnt += 1

            if cur > max_block: # 가장 큰 블럭 크기
                max_block = cur
print(block_cnt, max_block)