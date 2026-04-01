import sys
input = sys.stdin.readline

N = int(input())
maps = []

# \ : 3 - dir, 30 12
# / : (5 - dir) % 4  32 10
# 3 0 1 2 => 3 - dir
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(N):
    maps.append(list(input().strip()))
K = int(input())

side   = (K - 1) // N
offset = (K - 1) %  N

d = (side + 1) % 4
r, c = 0, 0

if side == 0:
    r = 0
    c = offset
elif side == 1:
    r = offset
    c = N-1
elif side == 2:
    r = N-1
    c = N-1-offset
elif side == 3:
    r = N-1-offset
    c = 0

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

cnt = 0
while in_range(r,c):
    ch = maps[r][c]
    cnt += 1

    if ch == '/':
        d = 3 - d
    elif ch == '\\':
        d = (5 - d) % 4
    r, c = r + dx[d], c + dy[d]

print(cnt)