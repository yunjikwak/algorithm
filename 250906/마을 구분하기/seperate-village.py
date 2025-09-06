N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def dfs(x, y):
    visited[x][y] = True
    cnt = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 0:
            continue
        if arr[nx][ny] == 1:
            cnt += dfs(nx, ny)

    return cnt

village = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            village.append(dfs(i, j))
print(len(village))
for c in sorted(village):
    print(c)