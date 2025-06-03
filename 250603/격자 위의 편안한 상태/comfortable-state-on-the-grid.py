import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
maps = [[0] * (N+1) for _ in range(N+1)]

def in_range(a, b):
    return 0 <= a < (N+1) and 0 <= b < (N+1)

for _ in range(M):
    r, c = map(int, input().split())
    maps[r][c] = 1

    cnt = 0
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]

        if not in_range(nx, ny):
            continue
        if maps[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)