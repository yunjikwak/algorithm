import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []

for _ in range(N):
    maps.append(list(input().strip()))

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def in_range(a,b):
    return 0 <= a < N and 0 <= b < M

result = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            for d in range(8):
                cnt = 1
                for k in range(1,3):
                    nx, ny = i + dx[d]*k, j+dy[d]*k
                    if not in_range(nx, ny) or maps[nx][ny] != 'E':
                        break
                    cnt += 1
                if cnt == 3:
                    result += 1
print(result)