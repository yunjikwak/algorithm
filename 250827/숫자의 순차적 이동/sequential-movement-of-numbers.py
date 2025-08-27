import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

arr = [list(map(int, input().split())) for _ in range(N)]

def inRange(a, b):
    return 0 <= a < N and 0 <= b < N

for _ in range(M):
    seq = [None] * (N*N)

    for i in range(N):
        for j in range(N):
            seq[arr[i][j]-1] = (i, j)
    print(seq)

    for x, y in seq:
        max_num = 0
        a, b = -1, -1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if inRange(nx, ny) and max_num < arr[nx][ny]:
                max_num = arr[nx][ny]
                a = nx
                b = ny
        print(arr[x][y], arr[a][b])
        tmp = arr[x][y]
        arr[x][y] = max_num
        arr[a][b] = tmp

for row in arr:
    print(*row)