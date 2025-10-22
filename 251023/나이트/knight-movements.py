from collections import deque

N = int(input())

r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

vistied = [[False] * N for _ in range(N)] 
step = [[-1] * N for _ in range(N)]

q = deque()

def push(x, y, s):
    vistied[x][y] = True
    step[x][y] = s
    q.append((x, y))

dx, dy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

def in_range(a, b):
    return 0<=a<N and 0<=b<N

def bfs():
    while q:
        a, b = q.popleft()

        for i in range(8):
            nx, ny = a+dx[i], b+dy[i]

            if not in_range(nx, ny) or vistied[nx][ny]:
                continue
            push(nx, ny, step[a][b]+1)
        
    return

push(r1, c1, 0)
bfs()
print(step[r2][c2])