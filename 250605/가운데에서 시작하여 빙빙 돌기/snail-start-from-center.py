import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N
dir_num = 0

N = int(input())

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
answer = [[0] * N for _ in range(N)]
dir_num = 0
cnt = 1
cur = 0

x, y = N//2, N//2
answer[x][y] = 1

for i in range(1, N*N):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if not in_range(nx, ny) or cur >= cnt or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        if dir_num == 0 or dir_num == 2:
            cnt += 1
        cur = 0
    
    x, y = x + dx[dir_num], y + dy[dir_num]
    answer[x][y] = i+1
    cur += 1

for i in range(N):
    for j in range(N):
        print(answer[i][j], end = ' ')
    print()
