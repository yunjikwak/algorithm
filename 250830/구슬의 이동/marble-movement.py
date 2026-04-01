import sys
input = sys.stdin.readline

N, M, T, K = map(int, input().split())

marble = []
for i in range(M):
    r, c, d, v = input().split()

    if d == 'U': d = 0
    elif d == 'D': d = 1
    elif d == 'L': d = 2
    elif d == 'R': d = 3

    marble.append([int(r)-1, int(c)-1, d, int(v), i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def inRange(a,b):
    return 0<=a<N and 0<=b<N

def opposite(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    elif d == 3: return 2

for _ in range(T):
    # cnt = [[0]*N for _ in range(N)]
    cnt = [[list() for _ in range(N)] for _ in range(N)]

    for x, y, d, v, idx in marble:
        nx, ny, nd = x, y, d
        for _ in range(v):
            nx += dx[nd]
            ny += dy[nd]
            if not inRange(nx, ny):
                nx -= dx[nd]
                ny -= dy[nd]
                nd = opposite(nd)
                nx += dx[nd]
                ny += dy[nd]
        cnt[nx][ny].append((nd, v, idx))
    
    n_marble = []
    for r in range(N):
        for c in range(N):
            cur = len(cnt[r][c])

            if cur > K:
                cnt[r][c].sort(key=lambda x: (-x[1], -x[2])) # v로 내림차순 정렬 -> 번호에 대한 내림차순
                cnt[r][c] = cnt[r][c][:K]

                for d, v, idx in cnt[r][c]:
                    n_marble.append((r, c, d, v, idx))
            else:
                for d, v, idx in cnt[r][c]:
                    n_marble.append((r, c, d, v, idx))
    marble = n_marble

print(len(marble))