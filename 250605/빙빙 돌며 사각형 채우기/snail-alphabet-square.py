import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 3 0 1 2

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M
dir_num = 0

answer = [[0] * M for _ in range(N)]

x, y = 0, 0
ascii_num = 65
answer[x][y] = chr(ascii_num)

for i in range(1, N*M):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dx[dir_num], y + dy[dir_num]
    ascii_num += 1
    answer[x][y] = chr(ascii_num)

for i in range(N):
    for j in range(M):
        print(answer[i][j], end = ' ')
    print()
