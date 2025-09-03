import sys
input = sys.stdin.readline

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

N, M, T = map(int, input().split())
marble = []
for i in range(M):
    r, c, d, w = input().split()

    if d == 'U': d = 0
    elif d == 'D': d = 1
    elif d == 'L': d = 2
    elif d == 'R': d = 3

    marble.append([int(r)-1, int(c)-1, d, int(w), i])

for _ in range(T):
    if not marble:
        break
    
    # n_cnt = [[[None] for _ in range(N)] for _ in range(N)]
    n_cnt = [[None] * N for _ in range(N)]

    for x, y, d, w, num in marble:
        nx = x+dx[d]
        ny = y+dy[d]

        if inRange(nx, ny):
            if n_cnt[nx][ny] is None:
                n_cnt[nx][ny] = [[nx, ny, d, w, num]]
            else:
                n_cnt[nx][ny].append([nx, ny, d, w, num])
        else: # 벽에 막힘 -> 뒤집힘(방향 변경, 1초 소요)
            nd = opposite(d)
            if n_cnt[x][y] is None:
                n_cnt[x][y] = [[x, y, nd, w, num]]
            else:
                n_cnt[x][y].append([x, y, nd, w, num])

    n_marble = []
    for r in range(N):
        for c in range(N):
            if n_cnt[r][c] is None:
                continue
            cur = n_cnt[r][c]

            if len(cur) == 1:
                n_marble.append(cur[0])    
            elif len(cur) > 1:
                n_cnt[r][c].sort(key=lambda x: -x[4])
                cur_d, cur_num = n_cnt[r][c][0][2], n_cnt[r][c][0][4]
                cur_w = 0

                for _, _, _, w, _ in n_cnt[r][c]:
                    cur_w += w
                n_marble.append([r, c, cur_d, cur_w, cur_num])

    marble = n_marble

marble.sort(key=lambda x: -x[3]) 
print(len(marble), marble[0][3]) # 남은 구술 수, 가장 무거운 구슬 무게