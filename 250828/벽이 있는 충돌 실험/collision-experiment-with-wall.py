import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

# U D L R
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def inRange(a,b):
#     return 0<=a<N and 0<=b<N

# def search_marble(arr):
#     marble = []
#     for i in range(N):
#         for j  in range(N):
#             if arr[i][j][0] == 1:
#                 marble.append((i, j, arr[i][j][1]))
#     return marble

DIR_MAP = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
OPPOSITE = [1, 0, 3, 2]
# def opposite(d):
#     if d == 0: return 1
#     elif d == 1: return 0
#     elif d == 2: return 3
#     elif d == 3: return 2

for _ in range(T):
    N, M = map(int, input().split())
    marble = []
    # cnt = [[[0,0] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, d_str = input().split()
        d = DIR_MAP[d_str.rstrip()]
        # if d == 'U': d = 0
        # elif d == 'D': d = 1
        # elif d == 'L': d = 2
        # elif d == 'R': d = 3
        # cnt[int(x)-1][int(y)-1] = [1, d]
        marble.append([int(x)-1, int(y)-1, d])

    for _ in range(2 * N): # 왜 2 * N -> 구슬의 한 줄 왕복이 모든 경우의 수임 
        if not marble:
            break

        landing_spots = defaultdict(list)
        # n_cnt = [[[0,0] for _ in range(N)] for _ in range(N)]

        for x, y, d in marble:
            nx = x+dx[d]
            ny = y+dy[d]

            if (0 <= nx < N and 0 <= ny < N):
                # n_cnt[nx][ny][0] += 1
                # n_cnt[nx][ny][1] = d
                landing_spots[(nx, ny)].append(d)
            else:
                nd = OPPOSITE[d]
                landing_spots[(x, y)].append(nd)
                # n_cnt[x][y][0] += 1
                # n_cnt[x][y][1] = opposite(d)

        # n_marble = []
        marble.clear()
        for (r, c), dirs in landing_spots.items():
            if len(dirs) == 1:
                marble.append([r, c, dirs[0]])

        # for r in range(N):
        #     for c in range(N):
        #         if n_cnt[r][c][0] == 1:
        #             nd = n_cnt[r][c][1]
        #             n_marble.append([r, c, nd])

        # marble = n_marble
        
    print(len(marble))
