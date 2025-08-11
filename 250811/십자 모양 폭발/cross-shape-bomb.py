import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
r,c = map(int, input().split())

size = graph[r-1][c-1]
half = size-1

col = []
for i in range(N):
    col.append(graph[i][c-1])

if (size*2-1) < N:
    if (r-1-half) < 0:
        times = r + half
        col = [0 for _ in range(times)] + col[times:]
    elif (r-1+half) >= N:
        col = col[:r-1-half]
        col = [0 for _ in range(N-len(col))] + col
    else:
        col = col[:r-1-half] + col[r+half:]
        col = [0 for _ in range(N-len(col))] + col
else:
    col = [0 for _ in range(N)]

# print(col)

for i in range(N-1, -1, -1):
    for j in range(N):
        if j == c-1: # 터진 열
            graph[i][j] = col[i]
            continue
        elif i > r-1 or j < (c-1-half) or j > c-1+half: # 범위 밖
            continue
        
        if i == 0:
            graph[i][j] = 0
        else:
            graph[i][j] = graph[i-1][j]
# print(graph)
for r in graph:
    print(*r)