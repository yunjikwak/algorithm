N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for r in row:
        arr[i].append([r, -1])

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        arr[i][j][1] = row[j]

r, c = map(int, input().split())

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

result = 0

def in_range(x, y, val):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if arr[x][y][0] <= val:
        return False
    return True

def bak(x, y, ans):
    global result
    cur, d = arr[x][y]
    result = max(result, ans)

    for i in range(1, N):
        nx, ny = x+dx[d-1]*i, y+dy[d-1]*i
        if in_range(nx, ny, cur):
            bak(nx, ny, ans+1)
    
    return

bak(r-1, c-1, 0)
print(result)