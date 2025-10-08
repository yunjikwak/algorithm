N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        arr[i].append([row[j], -1])
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        arr[i][j][1] = row[j]-1

r,c = map(int, input().split())

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

result = 0

def can(a, b, num):
    if a < 0 or a >= N or b < 0 or b >= N:
        return False
    if arr[a][b][0] <= num:
        return False
    return True

def bt(x, y, num):
    global result
    result = max(result, num)
    cur_num, d = arr[x][y]

    for i in range(1, N):
        nx, ny = x+dx[d]*i, y+dy[d]*i
        
        if can(nx, ny, cur_num):
            bt(nx, ny, num+1)

    return

bt(r-1, c-1, 0)
print(result)