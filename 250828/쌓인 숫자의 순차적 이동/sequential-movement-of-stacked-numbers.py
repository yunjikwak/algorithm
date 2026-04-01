import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[[x] for x in map(int, input().split())] for _ in range(N)]

move = list(map(int, input().split()))

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

seq = [None] * (N*N+1)
for i in range(N):
    for j in range(N):
        seq[arr[i][j][0]] = (i, j)

def inRange(a, b):
    return 0 <= a < N and 0 <= b < N

for m in move:
    x, y = seq[m]
    moving_num = []

    for idx, s in enumerate(arr[x][y]):
        if s == m:
            moving_num = arr[x][y][idx:]
            arr[x][y] = arr[x][y][:idx]
            break
    
    max_num = 0
    a, b = x, y
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if inRange(nx, ny) and len(arr[nx][ny]) > 0:
            for num in arr[nx][ny]:
                if max_num < num:
                    max_num = num
                    a = nx
                    b = ny
                    
    arr[a][b].extend(moving_num)
    for m in moving_num:
        seq[m] = (a, b)

for i in range(N):
    for j in range(N):
        if len(arr[i][j]) == 0:
            print(None)
        else:
            print(*arr[i][j][::-1])