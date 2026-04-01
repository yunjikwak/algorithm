import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
r, c, m1, m2, m3, m4, _dir = map(int, input().split())

count = [m1, m2, m3, m4]

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

x = r-1
y = c-1

path = []
for i in range(4):
    for _ in range(count[i]):
        path.append((x, y))
        x += dx[i]
        y += dy[i]

path_val = []
for x, y in path:
    path_val.append(graph[x][y])

if _dir == 0:
    rotate = [path_val[-1]] + path_val[:-1]
else: 
    rotate = path_val[1:] + [path_val[0]]

for i in range(len(path)):
    px, py = path[i]
    graph[px][py] = rotate[i]

for row in graph:
    print(*row)