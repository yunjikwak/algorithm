import sys
input = sys.stdin.readline
maps = []

for _ in range(19):
    maps.append(list(map(int, input().split())))

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1] 

win = 0
x = 0
y = 0

def in_range(a,b):
    return 0 <= a < 19 and 0 <= b < 19

for i in range(19):
    for j in range(19):
        if maps[i][j] != 0:
            cur = maps[i][j]

            for d in range(4):
                cnt = 1

                for k in range(1, 5):
                    nx, ny = i + dx[d]*k, j+dy[d]*k

                    if not in_range(nx, ny) or maps[nx][ny] != cur:
                        break
                    cnt += 1
                    
                if cnt == 5:
                    x = i+dx[d]*2+1
                    y = j+dy[d]*2+1
                    win = cur
                    print(win)
                    print(x, y)
                    sys.exit(0)
print(0)