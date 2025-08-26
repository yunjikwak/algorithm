import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# U D L R
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = [[0] * N for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    cnt[a-1][b-1] = 1

def inRange(a,b):
    return 0<=a<N and 0<=b<N

def search_marble(arr):
    marble = []
    for i in range(N):
        for j  in range(N):
            if arr[i][j] == 1:
                marble.append((i, j))
    return marble

for _ in range(T):
    n_cnt = [[0] * N for _ in range(N)]
    marble = search_marble(cnt)

    for x, y in marble:
        cur = arr[x][y]
        a, b = x, y
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and arr[nx][ny] > cur:
                cur = arr[nx][ny]
                a, b = nx, ny
        n_cnt[a][b] += 1

    for r in range(N):
        for c in range(N):
            if n_cnt[r][c] > 1:
                cnt[r][c] = 0
            elif n_cnt[r][c] == 1:
                cnt[r][c] = 1
            else:
                cnt[r][c] = 0

result = 0
for i in range(N):
    for j in range(N):
        if cnt[i][j] == 1:
            result += 1
print(result)