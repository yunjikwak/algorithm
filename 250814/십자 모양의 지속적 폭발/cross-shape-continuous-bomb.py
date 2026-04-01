import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

c = [int(input()) for _ in range(M)]

def theHightest(c):
    for i in range(N):
        if arr[i][c] != 0:
            return i
    return -1

def bomb(r, c):
    # print(r,c, arr[r][c])
    if arr[r][c] > 0:
        bomb_size = arr[r][c]
        arr[r][c] = 0

        for i in range(1, bomb_size):
            if r - i >= 0: arr[r - i][c] = 0
            if r + i < N: arr[r + i][c] = 0
            if c - i >= 0: arr[r][c - i] = 0
            if c + i < N: arr[r][c + i] = 0

for col in c:
    col -= 1
    row = theHightest(col)
    if row == -1:
        continue
    bomb(row, col)
    
    tmp = [[0] * N for _ in range(N)]

    for j in range(N):
        r_idx = N - 1
        for i in range(N - 1, -1, -1):
            if arr[i][j] != 0:
                tmp[r_idx][j] = arr[i][j]
                r_idx -= 1
    arr = tmp
    # print(tmp)

for r in arr:
    print(*r)