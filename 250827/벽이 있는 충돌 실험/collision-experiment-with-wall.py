import sys
from collections import defaultdict
input = sys.stdin.readline

DIR_MAP = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]
OPPOSITE = [1, 0, 3, 2]

def solve():
    N_str, M_str = input().split()
    N, M = int(N_str), int(M_str)

    marbles = []
    for _ in range(M):
        x_str, y_str, d_str = input().split()
        d = DIR_MAP[d_str.rstrip()]
        marbles.append([int(x_str) - 1, int(y_str) - 1, d])

    for _ in range(2 * N):
        if not marbles:
            break

        landing_spots = defaultdict(list)
        
        for r, c, d in marbles:
            nr, nc = r + DX[d], c + DY[d]

            if 0 <= nr < N and 0 <= nc < N:
                landing_spots[(nr, nc)].append(d)
            else:
                nd = OPPOSITE[d]
                landing_spots[(r, c)].append(nd)
        
        marbles.clear()
        for (r, c), dirs in landing_spots.items():
            if len(dirs) == 1:
                marbles.append([r, c, dirs[0]])
    
    print(len(marbles))

T_str = input()
if T_str:
    T = int(T_str)
    for _ in range(T):
        solve()