import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
blow = [list(map(int, input().split())) for _ in range(Q)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def shift(r1,c1,r2,c2):
    _r1, _c1, _r2, _c2 = r1-1, c1-1, r2-1, c2-1

    tmp = graph[_r1][_c1]

    for r in range(_r1, _r2):
        graph[r][_c1] = graph[r+1][_c1]
    for c in range(_c1, _c2):
        graph[_r2][c] = graph[_r2][c+1]
    for r in range(_r2, _r1, -1):
        graph[r][_c2] = graph[r-1][_c2]
    for c in range(_c2, _c1, -1):
        graph[_r1][c] = graph[_r1][c-1]

    graph[_r1][_c1+1] = tmp

def is_valid(x,y):
    return 0 <= x < N and 0 <= y < M

def cal_m(r1,c1,r2,c2):
    _r1, _c1, _r2, _c2 = r1-1, c1-1, r2-1, c2-1
    
    g = [row[:] for row in graph]
    for i in range(_r1, _r2+1):
        for j in range(_c1, _c2+1):
            cnt = 1
            cur = graph[i][j]

            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]

                if is_valid(nx, ny):
                    cnt += 1
                    cur += graph[nx][ny]
            
            g[i][j] = cur // cnt
    
    for i in range(_r1, _r2 + 1):
        for j in range(_c1, _c2 + 1):
            graph[i][j] = g[i][j]

for r1,c1,r2,c2 in blow:
    shift(r1,c1,r2,c2)
    cal_m(r1,c1,r2,c2)

for row in graph:
    print(*row)