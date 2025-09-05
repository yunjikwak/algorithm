N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

def dfs(x,y):
    visited[x][y] = True

    for dx, dy in [(1,0), (0,1)]:
        nx, ny = x+dx, y+dy

        if can_go(nx, ny):
            dfs(nx, ny)

visited = [[False]*M for _ in range(N)]
dfs(0, 0)

if visited[N-1][M-1]:
    print(1)
else:
    print(0)