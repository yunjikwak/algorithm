import sys
input = sys.stdin.readline

T = int(input())

# U D L R
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
    N, M = map(int, input().split())
    marble = []
    # cnt = [[[0,0] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, d = input().split()
        if d == 'U': d = 0
        elif d == 'D': d = 1
        elif d == 'L': d = 2
        elif d == 'R': d = 3
        # cnt[int(x)-1][int(y)-1] = [1, d]
        marble.append([int(x)-1, int(y)-1, d])

    for _ in range(2 * N): # 왜 2 * N -> 구슬의 한 줄 왕복이 모든 경우의 수임 
        if not marble:
            break

        # n_cnt = [[[0,0] for _ in range(N)] for _ in range(N)]
        n_cnt = {}

        for x, y, d in marble:
            nx = x+dx[d]
            ny = y+dy[d]

            if inRange(nx, ny):
                if (nx,ny) not in n_cnt:
                    n_cnt[(nx, ny)] = []
                n_cnt[(nx, ny)].append(d)
                # n_cnt[nx][ny][0] += 1
                # n_cnt[nx][ny][1] = d
            else:
                if (x,y) not in n_cnt:
                    n_cnt[(x, y)] = []
                n_cnt[(x, y)].append(opposite(d))
                # n_cnt[x][y][0] += 1
                # n_cnt[x][y][1] = opposite(d)

        n_marble = []
        for (x,y), dirs in n_cnt.items():
            if len(dirs) == 1:
                n_marble.append((x,y,dirs[0]))
        # for r in range(N):
        #     for c in range(N):
        #         if n_cnt[r][c][0] == 1:
        #             nd = n_cnt[r][c][1]
        #             n_marble.append([r, c, nd])

        marble = n_marble
        
    print(len(marble))
